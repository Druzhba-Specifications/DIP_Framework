import webbrowser
import json
import requests
import xml.etree.ElementTree
import csv
global parseddata

def openlink(url):
    webbrowser.open(url)
class grabexternal:
    class parse:
        def json(url):
            response = requests.get(url)

            if response.status_code == 200:
                try:
                    parseddata = json.load(response.text)
                except Exception as e:
                    print("Exception: {e}")
            else:
                print("Error:", response.status_code)
        def xml(url):
            response = requests.get(url)

            if response.status_code == 200:
                try:
                    parseddata = xml.etree.ElementTree.fromstring(response.text)
                except Exception as e:
                    print("Exception: {e}")
            else:
                print("Error:", response.status_code)
class parse:
    def json(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                parseddata = json.load(file)
                
        except FileNotFoundError:
            print(f"File '{filepath}' not found.")
        except json.JSONDecodeError as e:
            print("Invalid JSON in file:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)
    def xml(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                parseddata = xml.etree.ElementTree.fromstring(file)
        except FileNotFoundError:
            print(f"File '{filepath}' not found.")
        except xml.etree.ElementTree.ParseError as e:
            print("Invalid XML in file:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)