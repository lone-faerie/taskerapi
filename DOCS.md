## Endpoints

| Path | Method | Params/Body | Response | Description |
| ---- | ------ | ----------- | -------- | ----------- |
| `/api/auth` | GET | None | `auth` object | Authorize connection and create API key |
| `/api/auth/refresh` | GET | `token`: API key| `auth` object | Refresh an API key |
| `/api/stats` | GET | None | `stats` object | Get statistics for Tasker |
| `/api/profiles` | GET | `name`: Name of profile (optional, repeated) | `profile` objects | Get a list of Tasker profiles |
| `/api/profiles` | POST | `profile` object(s) | `profile` object(s) | Set the status of Tasker profiles |
| `/api/tasks` | GET | `name`: Name of task (optional, repeated) | `task` objects | Get a list of Tasker tasks |
| `/api/tasks` | POST | `task` object | Task return value | Perform a Tasker task |
| `/api/scenes` | GET | `name`: Name of scene (optional, repeated) | `scene` objects | Get a list of Tasker scenes |
| `/api/scenes` | POST | `scene` object(s) | `scene` object(s) | Show/hide/destroy Tasker scenes |
| `/api/globals` | GET | `name`: Name of global (optional, repeated) | `global` objects | Get a list of Tasker globals |
| `/api/globals` | POST | `global` object(s) | `global` object(s) | Set the value of Tasker globals |
| `/api/commands` | GET | `clear`: Clear the queue | list of `string` | Get a list of queued Tasker commands |
| `/api/commands` | POST | list of `string` | count: # of commands sent | Send Tasker commands |
| `/api/import` | POST | Task XML | `task` object | Import a Tasker task |
| `/api/file/<filepath>` | GET | None | File data | Get a file from the Tasker device |
| `/api/file/<filepath>` | DELETE | None | None | Delete a file from the Tasker device |

## Objects

### Auth

| Field | Type | Description |
| ----- | ---- | ----------- |
| `key` | string | API key |
| `authorized` | bool | Request was authorized |

### Stats

| Field | Type | Description |
| ----- | ---- | ----------- |
| `active_profiles` | int | # of active profiles |
| `total_profiles` | int | Total # of profiles |
| `total_tasks` | int | Total # of tasks |
| `total_scenes` | int | Total # of scenes |
| `total_globals` | int | Total # of user-defined globals |
| `version` | string | Tasker app version |

### Profile

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | string | Name of the profile |
| `enabled` | bool | Profile is enabled |
| `active` | bool | Profile is active |

### Task

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | string | Name of the task |
| `running` | bool | Task is running |

### Scene

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | string | Name of the scene |
| `status` | string | Status of the scene |
| `position` | (int, int) | Position of the scene (x, y) |
| `size` | (int, int) | Size of the scene (w, h) |

### Global

| Field | Type | Description |
| ----- | ---- | ----------- |
| `name` | string | Name of the global |
| `value` | any | Value of the global |





