import configparser
import os
import sys

import pytest

from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.ui.app import Application


def read_ini():
    config_file_name = os.environ.get("config-file", "project-config.ini")
    root_path = os.path.join(sys.path[0], config_file_name)
    parser = configparser.ConfigParser()
    parser.read(root_path)
    return parser


def get_config():
    return read_ini()


def get_seed():
    return get_config()["DEFAULT"]["polkawallet_seed"]


@pytest.fixture(scope="session")
def run_browser():
    # config = get_config()
    driver = ChromeDriverManager().install()
    extension_path = "~/Projects/acala_trial/acala_testnet/extensions/polkadot_0_40_1.crx"
    options = webdriver.ChromeOptions()
    options.add_extension(extension_path)
    driver = webdriver.Chrome(
        executable_path=driver,
        options=options)

    browser.config.driver = driver
    # browser.config.base_url = "https://apps.acala.network"

    yield browser
    browser.clear_session_storage()


@pytest.fixture(scope="session")
def app(run_browser):
    return Application(run_browser)
