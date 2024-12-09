LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            'format': '%(asctime)s %(filename)s %(lineno)s %(levelname)s %(message)s',
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "filename": "app.log",
            "encoding": "utf-8",
            "formatter": "default"
        }
        # ,
        # "file": {
        #     "class": "logging.handlers.TimedRotatingFileHandler",
        #     "level": "INFO",
        #     "filename": "log/app.log",
        #     "when": "midnight",
        #     "encoding": "utf-8",
        #     "formatter": "default",
        # }
    },
    "loggers": {
        "main": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        }
    },
    "disable_existing_loggers": True,
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO"
    }
}
