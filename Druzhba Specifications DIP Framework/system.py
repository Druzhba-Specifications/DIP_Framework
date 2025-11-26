import webbrowser
import json
import requests

class System:
    def openlink(url):
        webbrowser.open(url)
    class grabexternal:
        class parse:
            def json(url):
                response = requests.get(url)

                if response.status_code == 200:
                    print(response.text)
                else:
                    print("Error:", response.status_code)
    class parse:
        def json(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    parsed-data = json.load(file)  # Parses directly from file
                    
            except FileNotFoundError:
                print(f"File '{filepath}' not found.")
            except json.JSONDecodeError as e:
                print("Invalid JSON in file:", e)
            except Exception as e:
                print("An unexpected error occurred:", e)