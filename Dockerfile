FROM python:3.10

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY pyproject.toml pyproject.toml
COPY steak_project_api steak_project_api
RUN python -m pip install .

CMD ["uvicorn", "steak_project_api.app:app", "--host", "0.0.0.0", "--port", "8000"]
