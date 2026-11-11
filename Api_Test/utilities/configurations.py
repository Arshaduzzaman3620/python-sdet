"""Reads settings from config/properties.ini and secrets from environment variables."""
import configparser
import os
from pathlib import Path

# Project root = the Api_Test folder (one level above utilities/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = PROJECT_ROOT / "config" / "properties.ini"
TEST_DATA_DIR = PROJECT_ROOT / "test_data"


def getConfig():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)  # absolute path, so it works from any folder
    return config


def getPassword():
    # Never hard-code passwords. Set it in your terminal first:
    #   export GITHUB_PASSWORD="your-token"
    return os.environ.get("GITHUB_PASSWORD", "")
