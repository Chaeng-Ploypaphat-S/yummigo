FROM python:3.11-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Install the export plugin
RUN poetry self add poetry-plugin-export

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]