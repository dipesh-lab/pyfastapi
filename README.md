

### Setup for jenkins

```pip install poetry```
```poetry new pyfastapi```

### Add new dependency

```poetry add httpx@0.28.1```

### Build and create .whl file

```poetry build```

### Run single class by poetry

```poetry run uvicorn application/main.py --reload``` # For dev

```poetry run uvicorn application/main.py``` # For prod