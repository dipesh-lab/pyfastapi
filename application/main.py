import logging

import uvicorn
from fastapi import FastAPI, Response, status

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
ACCESS_LOG_FORMAT = (
    "%(asctime)s|%(levelname)s|%(client_addr)s|%(name)s|"
    "'%(request_line)s'|%(status_code)s"
)
DEFAULT_LOG_FORMAT = "%(asctime)s|%(levelname)s|%(name)s|%(message)s"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": DEFAULT_LOG_FORMAT,
            "datefmt": DATE_FORMAT,
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": ACCESS_LOG_FORMAT,
            "datefmt": DATE_FORMAT,
            "use_colors": None,
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
        "main": {"handlers": ["default"], "level": "INFO", "propagate": False},
    },
}

app = FastAPI(title="API microservice")

logger = logging.getLogger("main")

@app.get("/")
async def root(response: Response):
    logger.info("Root endpoint called")
    response.headers["Content-Type"] = "application/json"
    response.status_code = status.HTTP_200_OK
    return {"message": "API microservice"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=LOGGING_CONFIG)