import datetime, sys, os, json, requests, xml.etree.ElementTree as ET, csv, yaml, io, psutil, platform, subprocess, time, vlc, freecurrencyapi, urllib
from playsound3 import playsound
from plyer import notification

DIP_FRAMEWORK_VERSION = 1.0

client = freecurrencyapi.Client('fca_live_Wka6rbO1pD7fslnGeLLxUkhczd94oC0BfGzIK7fL')

class time:
    #actually fixed it lol
    @staticmethod
    def time_var():
        return datetime.datetime.now().time() #added/implemented all variables to make my(our) life easier
    @staticmethod
    def date_var():
        return datetime.datetime.now().date()
    @staticmethod
    def date_now():
        return datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

def retEx(e):
    return Exception("exception: ", e)

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
            if time < datetime.datetime.now().time():
                return True
            else:
                return False
        except Exception as e:
            retEx(e)

    @staticmethod
    def ifTimeIsAfter(time):
        try:
            if time > datetime.datetime.now().time():
                return True
            else:
                return False
        except Exception as e:
            retEx(e)


class computer:
    class file:
        class write:
            @staticmethod
            def write_file(filepath, content):
                try:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                except Exception as e:
                    retEx(e)
            @staticmethod
            def write_json(path, json_data):
                with open(path, "w", encoding="utf-8") as f:
                    f.write(json.dump(json_data, f))
            @staticmethod
            def write_csv(path, csv_data):
                with open(path, "w", encoding="utf-8") as f:
                    csv_writer = csv.writer(f, delimiter=',')
                    for row in csv_data:
                        csv_writer.writerow(row)
                        #Data is meant to be saved like this in this framework:
                        #data = [
                        #['Name', 'Department', 'Birthday Month'],
                        #['John Smith', 'Accounting', 'November'],
                        #['Erica Meyers', 'IT', 'March']
                        #]
            @staticmethod
            def write_yaml(path, yaml_data):
                with open(path, 'w', encoding="utf-8") as f:
                    f.write(yaml.dump(yaml_data, f, default_flow_style=False))

        class read:
            @staticmethod
            def read_file(path):
                try:
                    if computer.file.ensure_dir(path, False):
                        with open(path, "r", encoding="utf-8") as f:
                            return f.read
                    else:
                        return None
                except Exception as e:
                    retEx(e)
        @staticmethod
        def ensure_dir(directory, answer):
            try:
                if os.path.exists(directory):
                    return True
                else:
                    if answer == True:
                        os.makedirs(directory)
                        return True
                    else:
                        return False
            except Exception as e:
                retEx(e)

    @staticmethod
    def notify(title, message, appname):
        notification.notify(
            title=title,
            message=message,
            app_name=appname,
            timeout='10'
        )
    @staticmethod
    def playsound(location):
        try:
            playsound(location)
        except Exception as e:
            retEx(e)
    @staticmethod
    def playvideo(location):
        try:
            instance = vlc.Instance()
            player = instance.media_player_new()
            media = instance.media_new(location)
            player.set_media(media)
            player.play()

            # DO NOT REMOVE! KEEPS SCRIPT RUNNING WHILE VIDEO PLAYING TO NOT
            # STOP SCRIPT, BUT CAN BE DISABLED BY PUTTING "disable" INTO THE
            # SECOND PROMPT
            while player.is_playing():
                 time.sleep(1)
        except Exception as e:
            retEx(e)
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
    #yet again added sleep so that ppl can easily make computer sleep,
    # might need to be tested on all three, as I own windows but am currently developing in the web
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
#shutdown made to work multi-platform bc ppl can be too lazy
#to figure out which one is which


def openbrowserlink(url):
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
                f.write(f"{datetime.datetime.now()} || {log}\n")

        else:
            with open(log_file, "w", encoding="utf-8") as f:
                f.write(f'DIP LOG v{DIP_FRAMEWORK_VERSION} \nLog created {datetime.datetime.now()} \n {datetime.datetime.now()} || {log}\n')
                f.write(f"{datetime.datetime.now()} || {log}\n")
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
    class file:
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

                #omg im so tired
                #Nick, stop complaining and get back to work

        @staticmethod
        def csv(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    return [row for row in reader]
            except FileNotFoundError:
                raise Exception(f"File '{filepath}' not found.")
            except csv.Error as e:
                raise Exception("csv error yoo! ", e)
            except Exception as e:
                retEx(e)

        @staticmethod
        def yaml(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    parseddata = yaml.safe_load(file)
                    return parseddata
            except FileNotFoundError:
                raise Exception(f"File '{filepath}' not found.")
            except yaml.YAMLError as e:
                raise Exception("yaml error yoo! ", e)
            except Exception as e:
                retEx(e)

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

class internet:
    @staticmethod
    def extract_domain(url):
        try:
            return urllib.parse.urlparse(url)

        except Exception as e:
            retEx(e)
    @staticmethod
    def convert_currency(amount, origional_currency, converted_currency):
        result = client.latest()
        result = result.get('data', {}).get(converted_currency.upper)
        return float(amount) * float(result)