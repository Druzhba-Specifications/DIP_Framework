import sys
import os
import json
import requests
import xml.etree.ElementTree as ET
import csv
import time

@staticmethod
def openlink(url):
    try:
        if sys.platform.startswith("linux"):
            os.system(f"xdg-open {url}")
        elif sys.platform.startswith("windows"):
            os.system(f"start {url}")
        elif sys.platform.startswith("macos"):
            os.system(f"open {url}")
    except Exception as e:
        raise print("exception: ",e)

class grabexternal:

    class parse:

        @staticmethod
        def json(url):
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    parseddata = json.loads(response.text)
                    return parseddata
                except Exception as e:
                    print(f"Exception: {e}")
            else:
                print("Error:", response.status_code)

        @staticmethod
        def xml(url):
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    parseddata = ET.fromstring(response.text)
                    return parseddata
                except Exception as e:
                    print(f"Exception: {e}")
            else:
                print("Error:", response.status_code)

class parse:

    @staticmethod
    def json(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                parseddata = json.load(file)
                return parseddata
        except FileNotFoundError:
            print(f"File '{filepath}' not found.")
        except json.JSONDecodeError as e:
            print("Invalid JSON in file:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)

    @staticmethod
    def xml(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                parseddata = ET.fromstring(content)
                return parseddata
        except FileNotFoundError:
            print(f"File '{filepath}' not found.")
        except ET.ParseError as e:
            print("Invalid XML in file:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)