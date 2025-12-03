import datetime, sys, os, json, requests, xml.etree.ElementTree as ET, csv, yaml, time, io, psutil, platform, subprocess

DIP_FRAMEWORK_VERSION = 1.0

time_var = datetime.datetime.now().time() #added/implemented all variables to make my(our) life easier
date_var = datetime.datetime.now().date()
date_now = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

#im too lazy to implement, please someone implement

def retEx(e):
    return Exception("exception: ", e)

def module(module, moduledir):
    try:
        module = "{module}.py"
        if moduledir != "":
            module_path = os.path.join("modules", moduledir, module)
        else:
            module_path = os.path.join("modules", module)
        try:
            if os.path.exists(module_path):
                with open(module_path, "r") as f:
                    exec(f.read())
        except Exception as e:
            retEx(e)
    except Exception as e:
        retEx(e)

class sysIf:
    @staticmethod
    def ifTimeIs(time):
        try:
            if datetime.datetime.time(time):
                return True
            else: 
                return False
        except Exception as e:
            retEx(e)

    @staticmethod
    def ifTimeIsBefore(time):
        try:
            if time < time_var :
                return True
            else: 
                return False
        except Exception as e:
            retEx(e)

    @staticmethod
    def ifTimeIsAfter(time):
        try:
            if time > time_var:
                return True
            else: 
                return False
        except Exception as e:
            retEx(e)
            

class computer:
    @staticmethod
    def sleep():
        try:
            if sys.platform.startswith('windows') or sys.platform.startswith('win'):
                subprocess.run(['shutdown', '/h'])
            elif sys.platform.startswith('linux'):
                subprocess.run(['systemctl', 'suspend'])
            elif sys.platform.startswith('darwin'):
                subprocess.run(['pmset', 'sleepnow'])
            else: retEx("Unsupported Operating System")
        except Exception as e:
            retEx(e)
    #yet again added sleep so that ppl can easily make computer sleep, might need to be tested on all three, as I own windows but am currently developing in the web
    @staticmethod
    def reboot():
        try:
            if sys.platform.startswith('windows'):
                os.system('shutdown /r')
            else:
                subprocess.run(['sudo', 'shutdown', '-r', 'now'])
        except Exception as e:
            retEx(e)
    #added reboot bc ppl are still needing help with ts
    @staticmethod
    def shutdown():
        try:
            if sys.platform.startswith("windows"):
                os.system('shutdown /s')
            else:
                subprocess.run(['sudo', 'shutdown', '-h', 'now'])
        except Exception as e:
            retEx(e)
#shutdown made to work multi-platform bc ppl can be too lazy to figure out which one is which


def openlink(url):
    try:
        if sys.platform.startswith("linux"):
            os.system(f"xdg-open {url}")
        elif sys.platform.startswith("windows"):
            os.system(f"start {url}")
        elif sys.platform.startswith("darwin"):
            os.system(f"open {url}")
        else:
            retEx("Unsupported Operating System")
    except Exception as e:
        retEx(e)

def info():
    print(f"OS: {sys.platform}, OS VERSION: {platform.platform} DIP FRAMEWORK VERSION: {DIP_FRAMEWORK_VERSION}, CPU TEMP: {psutil.sensors_temperatures()} CPU: {platform.processor()} PYTHON VERSION: {sys.version}")

def log(log):
    log_dir = "DIP_Framework"
    log_file = os.path.join(log_dir, "log.txt")
    os.makedirs(log_dir, exist_ok=True)
    try:
        if os.path.exists(log_file):
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"{date_now} || {log}\n")
                
        else:
            with open(log_file, "w", encoding="utf-8") as f:
                f.write(f'DIP LOG v{DIP_FRAMEWORK_VERSION} \nLog created {date_now} \n {date_now} || {log}\n')
                f.write(f"{date_now} || {log}\n")
    except Exception as e:
        retEx(e)

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
                    retEx(e)
            else:
                raise Exception("Error:", response.status_code)

        @staticmethod
        def xml(url):
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    parseddata = ET.fromstring(response.text)
                    return parseddata
                except Exception as e:
                    retEx(e)
            else:
                raise Exception("Error:", response.status_code)
        
        @staticmethod
        def csv(url):
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    reader = csv.DictReader(io.StringIO(response.text))
                    return [row for row in reader]
                except Exception as e:
                    retEx(e)
            else:
                raise Exception("Error:", response.status_code)
        
        @staticmethod
        def yaml(url):
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    parseddata = yaml.safe_load(response.text)
                    return parseddata
                except Exception as e:
                    retEx(e)
            else:
                raise Exception("Error:", response.status_code)

class parse:

    @staticmethod
    def json(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                parseddata = json.load(file)
                return parseddata
        except FileNotFoundError:
            raise Exception(f"File '{filepath}' not found.")
        except json.JSONDecodeError as e:
            raise Exception("Invalid JSON in file:", e)
        except Exception as e:
            retEx(e)

    @staticmethod
    def csv(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            raise Exception(f"File '{filepath}' not found.")
        except Exception as e:
            retEx(e)
        except csv.Error as e:
            raise Exception("csv error yoo! ", e)
        
    @staticmethod
    def yaml(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                parseddata = yaml.safe_load(file)
                return parseddata
        except FileNotFoundError:
            raise Exception(f"File '{filepath}' not found.")
        except Exception as e:
            retEx(e)
        except yaml.YAMLError as e:
            raise Exception("yaml error yoo! ", e)

    @staticmethod
    def xml(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                parseddata = ET.fromstring(content)
                return parseddata
        except FileNotFoundError:
            raise Exception(f"File '{filepath}' not found.")
        except ET.ParseError as e:
            raise Exception("Invalid XML in file:", e)
        except Exception as e:
            retEx(e)