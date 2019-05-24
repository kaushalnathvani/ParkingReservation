import os
from ConfigParser import SafeConfigParser
CONFIG_PATH = str(os.path.realpath(__file__))
CONFIG_PATH = CONFIG_PATH.replace("config_reader.pyc", "")
CONFIG_PATH = CONFIG_PATH.replace("config_reader.pyo", "")
CONFIG_PATH = CONFIG_PATH.replace("config_reader.py", "")
CONFIG_PATH = CONFIG_PATH.replace("/classes","")
CONFIG_PATH = CONFIG_PATH.replace("\classes","")
CONFIG_PATH = os.path.join(CONFIG_PATH, "config")


class ReadConfig:
    def __init__(self):
        pass

    def read(self):
        config = SafeConfigParser()
        CONFIG_FILE = "config.ini"
        config.read(os.path.join(CONFIG_PATH, CONFIG_FILE))

        return config