Pokemon Near You (pnu, pronounced "new")
=======================

## Logging ##
At the top of each file put
```python
import logging
logger = logging.getLogger(__name__)
```

If the file has an `if __name__ == "__main__":` line, add:
```python
import logging.config
logging.config.fileConfig(pub_config['logging']['location'],
        disable_exisiting_loggers=False)
logging.info("Beginning " + __name__)
```

as long as that file also has `from config import pub_config` you
should be all set to go!
