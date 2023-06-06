"""Helper functions for taskerapi"""
import csv
from functools import lru_cache
import logging
import re
from typing import Any

import orjson
import xmltodict

from .const import (
    TaskerStructure,
    TaskerDeviceInfo,
    TASK_DEVICE_INFO,
    XML_DEVICE_INFO,
)

_LOGGER = logging.getLogger(__name__)

_RE_TASKER_XML_NAME = re.compile(
    "(<TaskerData.*>.*)<nme>(.*)</nme>", re.DOTALL
)

def maybe_cast(value):
    """Maybe cast a value to str, bool, int, or float"""
    try:
        if value is None:
            return ""
        elif (lower := value.lower()) == "null":
            return ""
        elif lower == "true":
            return True
        elif lower == "false":
            return False
        elif value.isdigit():
            return int(value)
        else:
            return float(value)
    except:
        return value
        
def csv_to_dict(text: str) -> dict[str, Any]:
    """Return a dict parsed from CSV data"""
    reader = csv.DictReader(
        text.strip().splitlines(),
        delimiter=","
    )
    out: dict[str, Any] = {}
    for line in reader:
        for k, v in line.items():
            if k is None:
                continue
            v = maybe_cast(v)
            if k in out:
                out[k].append(v)
            else:
                out[k] = [v]
    if not out:
        raise csv.Error("Not CSV")
    return out
    
def parse_tasker_output(
    data: bytes | str | None,
    encoding: str = "utf-8",
    structure_output: bool = True,
) -> TaskerStructure:
    """Return Tasker structure parsed from data"""
    if data is None:
        return None
    if not structure_output:
        return data.decode(encoding) if type(data) is bytes else data
    try:
        _LOGGER.info(f"Trying JSON for {data}")
        return orjson.loads(data)
    except:
        try:
            _LOGGER.info(f"Trying XML for {data}")
            return xmltodict.parse(
                data,
                postprocessor=lambda path, key, val: (key, maybe_cast(val))
            )
        except:
            text = data.decode(encoding) if type(data) is bytes else data
            try:
                _LOGGER.info(f"Trying CSV for {data}")
                return csv_to_dict(text)
            except:
                _LOGGER.info(f"Maybe casting {data}")
                return maybe_cast(text)
                
def rename_tasker_xml(name: str, data: str) -> str:
    """Rename a Tasker task before importing"""
    def replace(matchobj):
        return f"{matchobj.group(1)}<nme>{name}</nme>"
    return _RE_TASKER_XML_NAME.sub(
        f"\g<1><nme>{name}</nme>", data, 1
    )
    
def tasker_pattern_to_regex(pattern: str) -> tuple[str, bool]:
    if invert := (pattern and pattern[0] == '!'):
        pattern = pattern[1:]
    return '|'.join(
        [
            "^" + re.escape(p).replace('\*', '.*').replace('\+', '.+') + "$"
            for p in pattern.split('/') if p
        ]
    ), invert
    
@lru_cache
def tasker_pattern_to_regex_compile(pattern: str) -> tuple[re.Pattern, bool]:
    regex, invert = tasker_pattern_to_regex(pattern)
    return re.compile(regex, re.I if pattern.islower() else 0), invert
    
def tasker_pattern_match(pattern: str, string: str) -> bool:
    if not pattern:
        return True
    regex, invert = tasker_pattern_to_regex_compile(pattern)
    is_match = regex.match(string) is not None
    if invert:
        return not is_match
    return is_match