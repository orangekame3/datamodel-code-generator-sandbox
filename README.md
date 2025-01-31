# datamodel-code-generator-sandbox

## Getting Started

### Install

```bash
uv sync
```

### Generate Schema

```bash
make generate-schema
```

### Run FastAPI

```bash
make run
```

Check the following URL: http://127.0.0.1:8000/docs

### Curl Example

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/hello/Tom' \
  -H 'accept: application/json'
```
