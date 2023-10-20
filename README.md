[![Tests](https://github.com/matt-plank/steak-project-api/actions/workflows/tests.yaml/badge.svg)](https://github.com/matt-plank/steak-project-api/actions/workflows/tests.yaml)

# steak-project-api

The back-end of my website - The Steak Project - available at [thesteakproject.com](https://thesteakproject.com).

## Setting Up

Clone the repository

```bash
$ git clone https://github.com/matt-plank/steak-project-api.git
```

Install dependencies

```bash
# In repo root
$ pip install -r requirements.txt
$ pip install -e .
```

Run tests to make sure everything is installed

```bash
# In repo root
$ python -m pytest
```

## Running

For development

```bash
# In repo root
$ uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload
```

For production

```bash
$ uvicorn app.app:app --host 0.0.0.0 --port 8000
```
