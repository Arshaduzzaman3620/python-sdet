# Python API Testing — Study Project

Learning API automation with Python `requests`, step by step.

## Project structure

```
Api_Test/
├── README.md              ← you are here (study roadmap)
├── requirements.txt       ← libraries to install
├── config/
│   └── properties.ini     ← base URL / environment settings
├── utilities/             ← reusable helper code
│   ├── configurations.py  ← reads config + secrets (env vars)
│   ├── resources.py       ← API paths (/Library/Addbook.php ...)
│   └── payloads.py        ← request bodies (JSON) builders
├── test_data/             ← JSON files used by lessons/tests
│   ├── course.json
│   └── course1.json
├── lessons/               ← study scripts, in order
│   ├── 01_json_parsing.py
│   ├── 02_get_api_validations.py
│   ├── 03_post_and_delete_api.py
│   ├── 04_authentication.py
│   └── 05_miscellaneous.py
└── tests/                 ← real pytest tests (coming later)
```

**Rule of thumb:** a URL, path, body or password should be written in *one* place
(config / resources / payloads / env var) — lesson and test files only *use* them.

## Setup (one time, macOS)

```bash
cd Api_Test
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run a lesson

Always run from the `Api_Test` folder, using `-m` so `utilities` can be imported:

```bash
python -m lessons.01_json_parsing
python -m lessons.02_get_api_validations
python -m lessons.03_post_and_delete_api
export GITHUB_PASSWORD="your-token" && python -m lessons.04_authentication
```

## Study roadmap

| # | Topic | Status |
|---|-------|--------|
| 01 | JSON parsing (`json.loads`, `json.load`, compare files) | ✅ |
| 02 | GET request, params, status code, headers, validate body | ✅ |
| 03 | POST add book → delete book (chaining requests) | ✅ |
| 04 | Authentication (basic auth, secrets in env vars) | ✅ |
| 05 | Miscellaneous | ⏳ next |
| —  | Move lessons into pytest tests in `tests/` | 🔜 |
