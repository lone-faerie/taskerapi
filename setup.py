"""Setup module for taskerapi"""
from pathlib import Path
from setuptools import setup

PROJECT_DIR = Path(__file__).parent.resolve()
README_FILE = PROJECT_DIR / "README.md"
VERSION = "0.0.3"
INSTALL_REQUIREMENTS = [
    "aiohttp==3.8.4",
    "async_timeout==4.0.2",
    "orjson==3.8.12",
    "typing-extensions>=4.5.0,<5.0",
    "xmltodict=0.13.0"
]

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="taskerapi",
    version=VERSION,
    url="https://github.com/lone-faerie/taskerapi",
    download_url="https://github.com/lone-faerie/taskerapi",
    author="Lone Faerie",
    author_email="lone.faerie@gmail.com",
    description="Library to control Tasker Android app",
    long_description=README_FILE.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    license="GPLv3",
    packages=["taskerapi"],
    python_requires=">=3.9",
    install_requirements=INSTALL_REQUIREMENTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_data={"taskerapi.data": ["*.xml"]}
)