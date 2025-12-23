# DIP Framework - Complete Documentation

**Version 1.0**

A comprehensive guide to all features, functions, and capabilities of the DIP Framework.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Console Module](#console-module)
4. [System Module](#system-module)
5. [Time Checking](#time-checking)
6. [Computer Control](#computer-control)
7. [Media Playback](#media-playback)
8. [Desktop Notifications](#desktop-notifications)
9. [File Operations](#file-operations-1)
10. [Currency Conversion](#currency-conversion-1)
11. [Internet Utilities](#internet-utilities)
12. [Data Parsing](#data-parsing)
13. [Logging System](#logging-system)
14. [Best Practices](#best-practices)
15. [Troubleshooting](#troubleshooting)
16. [Platform Support](#platform-support)

---

## Introduction

DIP Framework is a Python utility library that simplifies common programming tasks. It provides easy-to-use functions for system operations, file management, data parsing, and more.

### The Problem DIP Solves

Writing cross-platform Python code is annoying. Every simple task requires checking the OS and using different commands:

**Without DIP Framework:**
```python
import os
import sys

# Clear console - different for each OS
if sys.platform == "nt":
    os.system('cls')  # Windows
else:
    os.system('clear')  # Linux/Mac

# Open a URL - different for each OS
if sys.platform.startswith("linux"):
    os.system(f"xdg-open {url}")
elif sys.platform.startswith("windows"):
    os.system(f"start {url}")
elif sys.platform.startswith("darwin"):
    os.system(f"open {url}")
    
# Shutdown - completely different commands
if sys.platform.startswith("windows"):
    os.system('shutdown /s')
else:
    subprocess.run(['sudo', 'shutdown', '-h', 'now'])
```

**With DIP Framework:**
```python
import System
import Console

Console.clear()  # Works everywhere!
System.openbrowserlink(url)  # Works everywhere!
System.computer.shutdown()  # Works everywhere!
```

**That's it. One function. Any platform. No if statements. No headaches.**

### Design Philosophy

- **Simplicity First** - One or two lines of code for common tasks
- **Cross-Platform** - Write once, run anywhere (Windows, Mac, Linux)
- **No Platform Checks** - We handle all the OS-specific stuff for you
- **Beginner Friendly** - Clear function names and simple parameters
- **Well Organized** - Logical grouping of related functions

### Key Features

- Console management
- Time-based conditionals
- Media playback (audio and video)
- Desktop notifications
- File I/O operations
- System control (sleep, reboot, shutdown)
- Data format parsing (JSON, CSV, YAML, XML)
- Currency conversion
- URL parsing
- Persistent logging

---

## Installation

### Requirements

- Python 3.x or higher
- pip package manager

### Install Dependencies

```bash
pip install psutil requests pyyaml playsound3 python-vlc plyer freecurrencyapi
```

### Import the Framework

```python
import System
import Console
```

---

## Console Module

The Console module provides utilities for terminal/console management.

### `Console.clear()`

Clears all text from the terminal screen.

**Syntax:**
```python
Console.clear()
```

**Parameters:** None

**Returns:** None

**Example:**
```python
import Console

print("This will be cleared")
Console.clear()
print("Clean screen!")
```

**Platform Behavior:**
- Windows: Uses `cls` command
- Linux/Mac: Uses `clear` command

**What DIP Does For You:**
Instead of writing:
```python
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
```

You just write:
```python
Console.clear()
```

**Note:** Includes automatic exception handling.

---

## System Module

The System module contains most of the framework's functionality.

### `System.info()`

Displays comprehensive system information.

**Syntax:**
```python
System.info()
```

**Parameters:** None

**Returns:** None (prints to console)

**Output Includes:**
- Operating system name
- OS version
- DIP Framework version
- CPU temperature (if available)
- CPU model
- Python version

**Example:**
```python
System.info()
# Output: OS: win32, OS VERSION: Windows-10-10.0.19041-SP0 DIP FRAMEWORK VERSION: 1.0, ...
```

### `System.openbrowserlink(url)`

Opens a URL in the system's default web browser.

**Syntax:**
```python
System.openbrowserlink(url)
```

**Parameters:**
- `url` (string) - The URL to open

**Returns:** None

**Example:**
```python
System.openbrowserlink("https://www.github.com")
System.openbrowserlink("https://www.python.org")
```

**Platform Behavior:**
- Windows: Uses `start` command
- Linux: Uses `xdg-open` command
- Mac: Uses `open` command

**What DIP Does For You:**
Instead of writing:
```python
if sys.platform.startswith("linux"):
    os.system(f"xdg-open {url}")
elif sys.platform.startswith("windows"):
    os.system(f"start {url}")
elif sys.platform.startswith("darwin"):
    os.system(f"open {url}")
```

You just write:
```python
System.openbrowserlink(url)
```

### Global Variables

**`System.time_var`**
- Current time as a datetime.time object
- Updated when module is imported

**`System.date_var`**
- Current date as a datetime.date object
- Updated when module is imported

**`System.date_now`**
- Formatted string: "MM/DD/YYYY HH:MM:SS AM/PM"
- Updated when module is imported

**Example:**
```python
print(System.time_var)   # 14:30:45.123456
print(System.date_var)   # 2024-12-22
print(System.date_now)   # 12/22/2024 02:30:45 PM
```

---

## Time Checking

Time checking functions allow you to run code based on the current time.

### `System.sysIf.ifTimeIs(time)`

Checks if the current time matches a specific time.

**Syntax:**
```python
System.sysIf.ifTimeIs(time)
```

**Parameters:**
- `time` (datetime.time) - The time to check against

**Returns:** Boolean (True/False)

**Example:**
```python
import datetime

if System.sysIf.ifTimeIs(datetime.time(15, 30)):
    print("It's exactly 3:30 PM!")
```

### `System.sysIf.ifTimeIsBefore(time)`

Checks if the current time is before a specific time.

**Syntax:**
```python
System.sysIf.ifTimeIsBefore(time)
```

**Parameters:**
- `time` (datetime.time) - The time to check against

**Returns:** Boolean (True/False)

**Example:**
```python
if System.sysIf.ifTimeIsBefore(datetime.time(12, 0)):
    print("Good morning!")
```

### `System.sysIf.ifTimeIsAfter(time)`

Checks if the current time is after a specific time.

**Syntax:**
```python
System.sysIf.ifTimeIsAfter(time)
```

**Parameters:**
- `time` (datetime.time) - The time to check against

**Returns:** Boolean (True/False)

**Example:**
```python
if System.sysIf.ifTimeIsAfter(datetime.time(18, 0)):
    print("Good evening!")
    
# Schedule a task
if System.sysIf.ifTimeIsAfter(datetime.time(14, 30)):
    # Run afternoon tasks
    send_afternoon_report()
```

**Use Cases:**
- Scheduling tasks
- Time-based greetings
- Conditional execution based on time of day
- Business hours checking

---

## Computer Control

**⚠️ WARNING:** These functions actually control your computer. Use with caution!

### `System.computer.sleep()`

Puts the computer into sleep/suspend mode.

**Syntax:**
```python
System.computer.sleep()
```

**Parameters:** None

**Returns:** None

**Example:**
```python
System.computer.sleep()
```

**Platform Behavior:**
- Windows: Uses `shutdown /h` (hibernate)
- Linux: Uses `systemctl suspend`
- Mac: Uses `pmset sleepnow`

**What DIP Does For You:**
Instead of checking the platform and using different commands:
```python
if sys.platform.startswith('windows'):
    subprocess.run(['shutdown', '/h'])
elif sys.platform.startswith('linux'):
    subprocess.run(['systemctl', 'suspend'])
elif sys.platform.startswith('darwin'):
    subprocess.run(['pmset', 'sleepnow'])
```

You just write:
```python
System.computer.sleep()
```

**Requirements:**
- Windows: May need administrator privileges
- Linux/Mac: Requires sudo privileges

### `System.computer.reboot()`

Restarts the computer.

**Syntax:**
```python
System.computer.reboot()
```

**Parameters:** None

**Returns:** None

**Example:**
```python
# Save all work first!
System.log("Rebooting system...")
System.computer.reboot()
```

**Platform Behavior:**
- Windows: Uses `shutdown /r`
- Linux/Mac: Uses `sudo shutdown -r now`

**What DIP Does For You:**
No more writing platform-specific shutdown commands! DIP handles it automatically.

**⚠️ WARNING:** All unsaved work will be lost!

### `System.computer.shutdown()`

Shuts down the computer completely.

**Syntax:**
```python
System.computer.shutdown()
```

**Parameters:** None

**Returns:** None

**Example:**
```python
System.log("Shutting down...")
System.computer.shutdown()
```

**Platform Behavior:**
- Windows: Uses `shutdown /s`
- Linux/Mac: Uses `sudo shutdown -h now`

**What DIP Does For You:**
One simple function instead of messy platform checks and different commands for each OS.

**⚠️ WARNING:** All unsaved work will be lost!

---

## Media Playback

### `System.computer.playsound(location)`

Plays an audio file.

**Syntax:**
```python
System.computer.playsound(location)
```

**Parameters:**
- `location` (string) - Path to the audio file

**Returns:** None

**Supported Formats:**
- MP3
- WAV
- OGG
- Other formats supported by playsound3

**Example:**
```python
# Relative path
System.computer.playsound("sounds/notification.mp3")

# Absolute path
System.computer.playsound("C:/Users/You/Music/song.wav")

# Notification sound
System.computer.playsound("beep.wav")
```

**Requirements:**
- playsound3 library
- Working audio output device

### `System.computer.playvideo(location)`

Plays a video file using VLC media player.

**Syntax:**
```python
System.computer.playvideo(location)
```

**Parameters:**
- `location` (string) - Path to the video file

**Returns:** None

**Supported Formats:**
- MP4
- AVI
- MKV
- MOV
- Any format supported by VLC

**Example:**
```python
System.computer.playvideo("videos/tutorial.mp4")
System.computer.playvideo("C:/Videos/movie.avi")
```

**Important Notes:**
- Requires VLC media player installed on your system
- The script will pause and wait until the video finishes playing
- Video plays in a VLC window

**Requirements:**
- VLC media player installed
- python-vlc library

**Download VLC:** https://www.videolan.org/vlc/

---

## Desktop Notifications

### `System.computer.notify(title, message, appname)`

Displays a desktop notification to the user.

**Syntax:**
```python
System.computer.notify(title, message, appname)
```

**Parameters:**
- `title` (string) - The notification title
- `message` (string) - The notification message body
- `appname` (string) - Your application name

**Returns:** None

**Example:**
```python
System.computer.notify(
    "Download Complete",
    "Your file has been downloaded successfully!",
    "MyApp"
)

# Task completion
System.computer.notify(
    "Processing Done",
    "1000 records processed",
    "Data Processor"
)

# Alert
System.computer.notify(
    "Warning",
    "Disk space is running low",
    "System Monitor"
)
```

**Platform Behavior:**
- Windows: Uses Windows notification system
- Linux: Uses notification daemon (notify-send)
- Mac: Uses macOS notification center

**Note:** Duration is currently fixed at 10 seconds.

**Requirements:**
- Desktop environment (not available on headless servers)
- plyer library

---

## File Operations

File operations are organized under `System.computer.file`.

### Reading Files

#### `System.computer.file.read.read_file(path)`

Reads the contents of a text file.

**Syntax:**
```python
System.computer.file.read.read_file(path)
```

**Parameters:**
- `path` (string) - Path to the file

**Returns:** String (file contents) or None if file doesn't exist

**Example:**
```python
content = System.computer.file.read.read_file("document.txt")
if content:
    print(content)
else:
    print("File not found")
```

**Encoding:** UTF-8 by default

### Writing Files

#### `System.computer.file.write.write_file(filepath, content)`

Writes content to a text file (creates or overwrites).

**Syntax:**
```python
System.computer.file.write.write_file(filepath, content)
```

**Parameters:**
- `filepath` (string) - Path where to save the file
- `content` (string) - Content to write

**Returns:** None

**Example:**
```python
System.computer.file.write.write_file("output.txt", "Hello, World!")

# Multi-line content
content = """Line 1
Line 2
Line 3"""
System.computer.file.write.write_file("data.txt", content)
```

**Note:** Creates the file if it doesn't exist, overwrites if it does.

#### `System.computer.file.write.write_json(path, json_data)`

Writes data to a JSON file.

**Syntax:**
```python
System.computer.file.write.write_json(path, json_data)
```

**Parameters:**
- `path` (string) - Path where to save the JSON file
- `json_data` (dict/list) - Python data structure to save

**Returns:** None

**Example:**
```python
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
System.computer.file.write.write_json("config.json", data)
```

#### `System.computer.file.write.write_csv(path, csv_data)`

Writes data to a CSV file.

**Syntax:**
```python
System.computer.file.write.write_csv(path, csv_data)
```

**Parameters:**
- `path` (string) - Path where to save the CSV file
- `csv_data` (list of lists) - Data to write

**Returns:** None

**Data Format:**
```python
data = [
    ['Name', 'Department', 'Birthday Month'],
    ['John Smith', 'Accounting', 'November'],
    ['Erica Meyers', 'IT', 'March']
]
```

**Example:**
```python
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '25', 'Boston'],
    ['Bob', '30', 'Chicago']
]
System.computer.file.write.write_csv("people.csv", data)
```

**Note:** First row is typically headers.

#### `System.computer.file.write.write_yaml(path, yaml_data)`

Writes data to a YAML file.

**Syntax:**
```python
System.computer.file.write.write_yaml(path, yaml_data)
```

**Parameters:**
- `path` (string) - Path where to save the YAML file
- `yaml_data` (dict/list) - Python data structure to save

**Returns:** None

**Example:**
```python
config = {
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "debug": True
}
System.computer.file.write.write_yaml("config.yaml", config)
```

### Directory Management

#### `System.computer.file.ensure_dir(directory, answer)`

Checks if a directory exists, optionally creates it.

**Syntax:**
```python
System.computer.file.ensure_dir(directory, answer)
```

**Parameters:**
- `directory` (string) - Path to the directory
- `answer` (boolean) - If True, creates the directory; if False, just checks

**Returns:** Boolean (True if exists/created, False if doesn't exist when answer=False)

**Example:**
```python
# Just check if it exists
if System.computer.file.ensure_dir("data", False):
    print("Directory exists")
else:
    print("Directory doesn't exist")

# Create if it doesn't exist
System.computer.file.ensure_dir("output", True)

# Nested directories
System.computer.file.ensure_dir("data/processed/2024", True)
```

**Use Cases:**
- Ensuring output directories exist before saving files
- Checking for required folders
- Creating project structure

---

## Currency Conversion

### `System.internet.convert_currency(amount, original_currency, converted_currency)`

Converts money from one currency to another using live exchange rates.

**Syntax:**
```python
System.internet.convert_currency(amount, original_currency, converted_currency)
```

**Parameters:**
- `amount` (number) - Amount to convert
- `original_currency` (string) - Source currency code (ISO 4217)
- `converted_currency` (string) - Target currency code (ISO 4217)

**Returns:** Float (converted amount)

**Example:**
```python
# Convert 100 USD to EUR
result = System.internet.convert_currency(100, "USD", "EUR")
print(f"100 USD = {result} EUR")

# Convert 50 GBP to JPY
result = System.internet.convert_currency(50, "GBP", "JPY")
print(f"50 GBP = {result} JPY")

# Multiple conversions
currencies = ["EUR", "GBP", "JPY", "CAD"]
for currency in currencies:
    result = System.internet.convert_currency(100, "USD", currency)
    print(f"100 USD = {result} {currency}")
```

**Common Currency Codes:**
- USD - United States Dollar
- EUR - Euro
- GBP - British Pound
- JPY - Japanese Yen
- CAD - Canadian Dollar
- AUD - Australian Dollar
- CHF - Swiss Franc
- CNY - Chinese Yuan

**Requirements:**
- Internet connection
- freecurrencyapi library
- API key (included in framework)

**Notes:**
- Exchange rates are live/current
- Rates update automatically
- Free API has rate limits

---

## Internet Utilities

### `System.internet.extract_domain(url)`

Parses a URL and extracts its components.

**Syntax:**
```python
System.internet.extract_domain(url)
```

**Parameters:**
- `url` (string) - The URL to parse

**Returns:** ParseResult object with URL components

**Available Properties:**
- `scheme` - URL scheme (http, https, ftp, etc.)
- `netloc` - Network location (domain)
- `path` - Path to resource
- `params` - Parameters
- `query` - Query string
- `fragment` - Fragment identifier

**Example:**
```python
parsed = System.internet.extract_domain("https://www.github.com/user/repo?tab=readme")

print(parsed.scheme)    # https
print(parsed.netloc)    # www.github.com
print(parsed.path)      # /user/repo
print(parsed.query)     # tab=readme

# Extract just the domain
url = "https://api.example.com/v1/data"
domain = System.internet.extract_domain(url).netloc
print(domain)  # api.example.com
```

**Use Cases:**
- Extracting domain names from URLs
- Validating URL structure
- Parsing query parameters
- Security checks (verifying allowed domains)

---

## Data Parsing

DIP Framework supports parsing multiple data formats from both local files and external URLs.

### Local File Parsing

All local file parsing functions are under `System.parse.file`.

#### `System.parse.file.json(filepath)`

Parses a JSON file.

**Syntax:**
```python
System.parse.file.json(filepath)
```

**Parameters:**
- `filepath` (string) - Path to the JSON file

**Returns:** Python dict or list (parsed JSON data)

**Example:**
```python
# Simple JSON object
data = System.parse.file.json("config.json")
print(data["database"]["host"])

# JSON array
users = System.parse.file.json("users.json")
for user in users:
    print(user["name"])
```

**Error Handling:**
- FileNotFoundError - File doesn't exist
- JSONDecodeError - Invalid JSON format

#### `System.parse.file.csv(filepath)`

Parses a CSV file.

**Syntax:**
```python
System.parse.file.csv(filepath)
```

**Parameters:**
- `filepath` (string) - Path to the CSV file

**Returns:** List of dictionaries (one per row)

**Example:**
```python
data = System.parse.file.csv("contacts.csv")

# Each row is a dictionary
for row in data:
    print(f"{row['Name']}: {row['Email']}")

# Access specific column
emails = [row['Email'] for row in data]
```

**Note:** First row is treated as headers.

#### `System.parse.file.yaml(filepath)`

Parses a YAML file.

**Syntax:**
```python
System.parse.file.yaml(filepath)
```

**Parameters:**
- `filepath` (string) - Path to the YAML file

**Returns:** Python dict or list (parsed YAML data)

**Example:**
```python
config = System.parse.file.yaml("config.yaml")
print(config["database"]["host"])
print(config["debug"])
```

**Error Handling:**
- FileNotFoundError - File doesn't exist
- YAMLError - Invalid YAML format

#### `System.parse.file.xml(filepath)`

Parses an XML file.

**Syntax:**
```python
System.parse.file.xml(filepath)
```

**Parameters:**
- `filepath` (string) - Path to the XML file

**Returns:** ElementTree object

**Example:**
```python
tree = System.parse.file.xml("data.xml")
root = tree

# Find elements
for child in root:
    print(child.tag, child.text)

# Find specific elements
items = root.findall('.//item')
```

**Error Handling:**
- FileNotFoundError - File doesn't exist
- ParseError - Invalid XML format

### External URL Parsing

All external URL parsing functions are under `System.grabexternal.parse`.

#### `System.grabexternal.parse.json(url)`

Fetches and parses JSON from a URL.

**Syntax:**
```python
System.grabexternal.parse.json(url)
```

**Parameters:**
- `url` (string) - URL to fetch JSON from

**Returns:** Python dict or list (parsed JSON data)

**Example:**
```python
# API endpoint
weather = System.grabexternal.parse.json("https://api.weather.com/current")
print(weather["temperature"])

# Public data
data = System.grabexternal.parse.json("https://example.com/data.json")
```

**Requirements:** Internet connection

#### `System.grabexternal.parse.csv(url)`

Fetches and parses CSV from a URL.

**Syntax:**
```python
System.grabexternal.parse.csv(url)
```

**Parameters:**
- `url` (string) - URL to fetch CSV from

**Returns:** List of dictionaries (one per row)

**Example:**
```python
data = System.grabexternal.parse.csv("https://example.com/data.csv")
for row in data:
    print(row)
```

#### `System.grabexternal.parse.yaml(url)`

Fetches and parses YAML from a URL.

**Syntax:**
```python
System.grabexternal.parse.yaml(url)
```

**Parameters:**
- `url` (string) - URL to fetch YAML from

**Returns:** Python dict or list (parsed YAML data)

**Example:**
```python
config = System.grabexternal.parse.yaml("https://example.com/config.yaml")
```

#### `System.grabexternal.parse.xml(url)`

Fetches and parses XML from a URL.

**Syntax:**
```python
System.grabexternal.parse.xml(url)
```

**Parameters:**
- `url` (string) - URL to fetch XML from

**Returns:** ElementTree object

**Example:**
```python
feed = System.grabexternal.parse.xml("https://example.com/rss.xml")
```

**Common Errors:**
- HTTP errors (404, 500, etc.)
- Network errors (no internet, timeout)
- Parse errors (invalid format)

---

## Logging System

### `System.log(message)`

Writes a timestamped message to the log file.

**Syntax:**
```python
System.log(message)
```

**Parameters:**
- `message` (string) - The message to log

**Returns:** None

**Log Location:** `DIP_Framework/log.txt`

**Example:**
```python
System.log("Application started")
System.log("User logged in")
System.log("Processing 100 records")
System.log("Operation completed successfully")

# Log errors
try:
    risky_operation()
except Exception as e:
    System.log(f"Error: {e}")
```

**Log Format:**
```
DIP LOG v1.0
Log created 2024-12-22 14:30:00.123456
2024-12-22 14:30:00.123456 || Application started
2024-12-22 14:30:05.789012 || User logged in
```

**Features:**
- Automatic timestamp on each entry
- Creates log directory if it doesn't exist
- Creates log file if it doesn't exist
- Appends to existing log file

**Use Cases:**
- Debugging
- Tracking application flow
- Error logging
- Audit trails
- Performance monitoring

---

## Best Practices

### Error Handling

Always wrap potentially failing operations in try-except blocks:

```python
try:
    data = System.parse.file.json("config.json")
except Exception as e:
    System.log(f"Failed to load config: {e}")
    # Use default config
```

### File Paths

Use absolute paths when possible:

```python
import os

# Get absolute path
config_path = os.path.abspath("config.json")
data = System.parse.file.json(config_path)
```

### Logging

Log important events and errors:

```python
System.log("Application started")

try:
    process_data()
    System.log("Data processed successfully")
except Exception as e:
    System.log(f"Processing failed: {e}")
```

### Time Checks

Store time objects for reuse:

```python
morning_end = datetime.time(12, 0)
evening_start = datetime.time(18, 0)

if System.sysIf.ifTimeIsBefore(morning_end):
    # Morning tasks
    pass
elif System.sysIf.ifTimeIsAfter(evening_start):
    # Evening tasks
    pass
```

### System Control

Always warn users before system control operations:

```python
print("WARNING: This will reboot your computer!")
response = input("Continue? (yes/no): ")
if response.lower() == "yes":
    System.computer.reboot()
```

---

## Troubleshooting

### Module Not Found Error

**Problem:** `ModuleNotFoundError: No module named 'psutil'` (or other libraries)

**Solution:**
```bash
pip install psutil requests pyyaml playsound3 python-vlc plyer freecurrencyapi
```

### Video Playback Fails

**Problem:** Videos won't play

**Solution:**
- Install VLC media player from https://www.videolan.org/vlc/
- Ensure python-vlc is installed: `pip install python-vlc`

### Notifications Not Showing

**Problem:** Desktop notifications don't appear

**Solutions:**
- Ensure you have a desktop environment (not a headless server)
- On Linux, check if notification daemon is running
- Check system notification settings
- Verify plyer is installed: `pip install plyer`

### Permission Denied on System Control

**Problem:** Can't sleep/reboot/shutdown

**Solutions:**
- **Windows:** Run script as Administrator (right-click → Run as Administrator)
- **Linux/Mac:** Use sudo: `sudo python your_script.py`

### Currency Conversion Fails

**Problem:** Currency conversion returns errors

**Solutions:**
- Check internet connection
- Verify currency codes are valid (ISO 4217 codes like "USD", "EUR")
- API has rate limits - wait a moment and retry
- Ensure freecurrencyapi is installed

### File Not Found

**Problem:** Can't find files when parsing

**Solutions:**
- Use absolute paths: `os.path.abspath("file.json")`
- Check if file actually exists: `os.path.exists("file.json")`
- Verify spelling and file extension
- Check current working directory: `print(os.getcwd())`

### CSV Parsing Issues

**Problem:** CSV data looks wrong

**Solutions:**
- Check file encoding (should be UTF-8)
- Verify CSV has headers in first row
- Check delimiter (should be comma)
- Look for special characters or line breaks in data

---

## Platform Support

### Windows

**Supported Features:**
- ✅ Console clearing
- ✅ Time checking
- ✅ Media playback
- ✅ Desktop notifications
- ✅ File operations
- ✅ System control (may need admin for reboot/shutdown)
- ✅ Data parsing
- ✅ Currency conversion
- ✅ URL parsing

**Requirements:**
- Python 3.x for Windows
- VLC for Windows (for video playback)

### Linux

**Supported Features:**
- ✅ Console clearing
- ✅ Time checking
- ✅ Media playback
- ✅ Desktop notifications (with desktop environment)
- ✅ File operations
- ✅ System control (requires sudo)
- ✅ Data parsing
- ✅ Currency conversion
- ✅ URL parsing

**Requirements:**
- Python 3.x
- VLC media player
- Desktop environment (for notifications)
- sudo access (for system control)

**Common Distributions Tested:**
- Ubuntu
- Debian
- Fedora
- Arch Linux

### macOS

**Supported Features:**
- ✅ Console clearing
- ✅ Time checking
- ✅ Media playback
- ✅ Desktop notifications
- ✅ File operations
- ✅ System control (requires sudo)
- ✅ Data parsing
- ✅ Currency conversion
- ✅ URL parsing

**Requirements:**
- Python 3.x
- VLC for Mac
- sudo access (for system control)

---

## Additional Information

### Framework Version

Current version: **1.0**

Access programmatically:
```python
print(System.DIP_FRAMEWORK_VERSION)  # 1.0
```

### File Encoding

All file operations use UTF-8 encoding by default, supporting international characters.

### Exception Handling

All functions include built-in exception handling. Errors are caught and processed through the `retEx()` function.

### Thread Safety

The framework is not thread-safe by default. If using in multi-threaded applications, implement proper locking mechanisms.

### Performance Considerations

- File parsing operations are synchronous (blocking)
- Video playback blocks execution until complete
- Currency conversion requires network request (may be slow)
- System control operations are immediate

---

## Getting Help

### Documentation

- **README:** Quick overview and getting started
- **This Document:** Complete API reference and examples

### Community Support

- **GitHub Issues:** Report bugs and request features
- **GitHub Discussions:** Ask questions and share ideas

### Contributing

We welcome contributions! See README.md for contribution guidelines.

---

**DIP Framework v1.0 Documentation**

*Last Updated: December 2025*

**Made with ❤️ by the Druzhba Specifications team**
