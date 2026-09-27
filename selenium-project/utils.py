import os
import csv
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_DIR, "config.ini")

def get_config(key, fallback=""):
    """Read a setting from config.ini"""
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config.get("app", key, fallback=fallback)

def read_csv(file_name):
    """Read rows from a CSV file in the data/ folder (skipping header)"""
    file_path = os.path.join(BASE_DIR, "data", file_name)
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        return [row for row in reader]

def get_driver():
    """Initialize Chrome WebDriver using settings from config.ini"""
    options = Options()
    if get_config("headless", "true").lower() == "true":
        options.add_argument("--headless=new")
        
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver
