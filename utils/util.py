import csv
from datetime import datetime
import yaml
import json
import os

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

def read_json_file(file="config.json"):
    file_path = os.path.abspath(os.path.join(ROOT_PATH, file))
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def read_yaml_file(file="config.yml"):
    print("yaml-version: "+yaml.__version__)

    file_path= os.path.abspath(os.path.join(ROOT_PATH, file))
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except yaml.YAMLError as exc:
        print(f"Error reading YAML file: {exc}")
        return None

def take_screenshot(driver, file_path="screenshot.png"):
    driver.get_screenshot_as_file(file_path)
    print(f"Screenshot saved at: {file_path}")


def create_csv(products):
    with open("product_details.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price"])
        for name, price in products.items():
            writer.writerow([name, price])