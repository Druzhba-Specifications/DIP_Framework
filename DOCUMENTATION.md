# DIP Framework - Complete Documentation

**Version 1.0**

A comprehensive guide to all features, functions, and capabilities of the DIP Framework.

---

## Table of Contents

### Getting Started
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Quick Reference](#quick-reference)

### Core Modules
4. [Console Module](#console-module)
5. [System Module](#system-module)
6. [REHH Module (Beta)](#rehh-module)

### System Features
7. [Time Checking](#time-checking)
8. [Computer Control](#computer-control)
9. [System Information](#system-information)
10. [Logging System](#logging-system)

### File & Data
11. [File Operations](#file-operations)
12. [Data Parsing - Local Files](#data-parsing---local-files)
13. [Data Parsing - External URLs](#data-parsing---external-urls)

### Media & Notifications
14. [Media Playback](#media-playback)
15. [Desktop Notifications](#desktop-notifications)

### Internet & Web
16. [URL Operations](#url-operations)
17. [Currency Conversion](#currency-conversion)
18. [Internet Utilities](#internet-utilities)

### Reference
19. [Best Practices](#best-practices)
20. [Troubleshooting](#troubleshooting)
21. [Platform Support](#platform-support)
22. [API Quick Reference](#api-quick-reference)

---

# Getting Started

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
- Simple web hosting (REHH - beta)

---

## Installation

### Requirements

- Python 3.x or higher
- pip package manager

### Install Dependencies

```bash
pip install psutil requests pyyaml playsound3 python-vlc plyer freecurrencyapi
```

### Getting DIP Framework

**Option 1: Stable Release (Recommended)**

Download from the [Releases page](https://github.com/Druzhba-Specifications/DIP_Framework/releases):
1. Go to the releases page
2. Download the latest release (e.g., `v1.0.0-pre.1.zip`)
3. Extract the files to your project directory

**Includes:** All stable features (System, Console modules)  
**Does NOT include:** Beta features like REHH module

**Option 2: Clone Repository (For Beta Features)**

For access to REHH and other beta features:
```bash
git clone https://github.com/Druzhba-Specifications/DIP_Framework.git
cd DIP_Framework
```

**Includes:** Everything, including beta/experimental features

### Import the Framework

```python
import System
import Console
import REHH  # Only available if you cloned the repository
```

---

## Quick Reference

### Most Common Operations

```python
import System
import Console
import datetime

# Console
Console.clear()                              # Clear screen

# Logging
System.log("Message")                        # Log with timestamp

# Time Checking
System.sysIf.ifTimeIsAfter(time)            # Check if after time
System.sysIf.ifTimeIsBefore(time)           # Check if before time

# File Operations
System.computer.file.read.read_file(path)                    # Read file
System.computer.file.write.write_file(path, content)         # Write file
System.computer.file.ensure_dir(dir, True)                   # Create directory

# Data Parsing - Local
System.parse.file.json(filepath)             # Parse JSON file
System.parse.file.csv(filepath)              # Parse CSV file

# Data Parsing - URLs
System.grabexternal.parse.json(url)          # Parse JSON from URL
System.grabexternal.parse.csv(url)           # Parse CSV from URL

# Media
System.computer.playsound(file)              # Play audio
System.computer.playvideo(file)              # Play video

# Notifications
System.computer.notify(title, msg, app)      # Desktop notification

# System Control
System.computer.sleep()                      # Sleep computer
System.computer.reboot()                     # Reboot computer
System.computer.shutdown()                   # Shutdown computer

# Internet
System.openbrowserlink(url)                  # Open URL in browser
System.internet.convert_currency(amt, from, to)  # Convert currency
System.internet.extract_domain(url)          # Parse URL

# System Info
System.info()                                # Display system info
```

---

# Core Modules

## Console Module

The Console module provides utilities for terminal/console management.

### Functions

#### `Console.clear()`

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

**Platform Behavior:**
- Windows: Uses `cls` command
- Linux/Mac: Uses `clear` command

---

## System Module

The System module contains most of the framework's functionality.

### Global Variables

**`System.DIP_FRAMEWORK_VERSION`**
- Framework version number (1.0)

**`System.time_var`**
- Current time as datetime.time object
- Updated when module is imported

**`System.date_var`**
- Current date as datetime.date object
- Updated when module is imported

**`System.date_now`**
- Formatted string: "MM/DD/YYYY HH:MM:SS AM/PM"
- Updated when module is imported

**Example:**
```python
print(System.DIP_FRAMEWORK_VERSION)  # 1.0
print(System.time_var)                # 14:30:45.123456
print(System.date_var)                # 2024-12-22
print(System.date_now)                # 12/22/2024 02:30:45 PM
```

---

## REHH Module

**REHH** (Really Easy HTTP Hosting) is a compact module for hosting HTML files with minimal configuration.

**Current Version:** 0.03 (Beta)  
**Status:** Extreme Beta - No guarantee of working on all devices  
**Availability:** Clone repository only - not in stable releases

### Overview

REHH simplifies web hosting by using XML configuration files. Instead of setting up complex web servers, you just create a simple XML config and start the server.

**⚠️ Important:** REHH is only available if you clone the repository:
```bash
git clone https://github.com/Druzhba-Specifications/DIP_Framework.git
```

It is **not** included in stable release downloads because it's still in extreme beta.

### Functions

#### `REHH.start_rehh(location)`

Starts an HTTP server based on an XML configuration file.

**Syntax:**
```python
import REHH

REHH.start_rehh("config.xml")
```

**Parameters:**
- `location` (string) - Path to the XML configuration file

**Returns:** None (server runs until interrupted)

**Example:**
```python
import REHH

# Start server with config file
REHH.start_rehh("REHH/example.xml")
# Server starts and runs until you press Ctrl+C
```

### Configuration File Format

REHH uses XML configuration files:

```xml
<rehh>
    <port>6767</port>
    <loc>diffloc</loc>
    <html>/home/Druzhba/index.html</html>
</rehh>
```

**Configuration Tags:**

| Tag | Description | Values |
|-----|-------------|--------|
| `<port>` | Port number for HTTP server | Any number (use 1024+ to avoid permissions) |
| `<loc>` | Location type for HTML | `diffloc` (file path) or `webdoc` (direct HTML) |
| `<html>` | HTML content or file path | File path when using `diffloc`, HTML when using `webdoc` |

### Configuration Examples

**Example 1: Host Local File**
```xml
<rehh>
    <port>8080</port>
    <loc>diffloc</loc>
    <html>C:/websites/mysite/index.html</html>
</rehh>
```

**Example 2: Direct HTML Content**
```xml
<rehh>
    <port>3000</port>
    <loc>webdoc</loc>
    <html><h1>Hello World!</h1><p>Welcome!</p></html>
</rehh>
```

### Complete Example

**Step 1: Create HTML File**
```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>My Site</title>
</head>
<body>
    <h1>Welcome!</h1>
    <p>Hosted with REHH</p>
</body>
</html>
```

**Step 2: Create Config**
```xml
<!-- config.xml -->
<rehh>
    <port>8080</port>
    <loc>diffloc</loc>
    <html>index.html</html>
</rehh>
```

**Step 3: Start Server**
```python
import REHH

REHH.start_rehh("config.xml")
```

**Step 4: Visit Browser**
Open `http://localhost:8080`

### Stopping the Server

Press `Ctrl+C` (or `Cmd+C` on Mac) to stop.

### Important Notes

⚠️ **Beta Status:**
- Extreme beta - test thoroughly
- No guarantee it works on all devices

⚠️ **Security:**
- For local development only
- Not for production hosting
- No authentication or encryption

⚠️ **Limitations:**
- Static HTML only
- One file per server
- No SSL/HTTPS
- Ports below 1024 need admin/sudo

---

# System Features

## Time Checking

Time checking functions allow you to run code based on the current time.

### Functions

#### `System.sysIf.ifTimeIs(time)`

Checks if current time matches a specific time.

**Syntax:**
```python
System.sysIf.ifTimeIs(time)
```

**Parameters:**
- `time` (datetime.time) - Time to check against

**Returns:** Boolean

**Example:**
```python
import datetime

if System.sysIf.ifTimeIs(datetime.time(15, 30)):
    print("It's exactly 3:30 PM!")
```

#### `System.sysIf.ifTimeIsBefore(time)`

Checks if current time is before a specific time.

**Syntax:**
```python
System.sysIf.ifTimeIsBefore(time)
```

**Parameters:**
- `time` (datetime.time) - Time to check against

**Returns:** Boolean

**Example:**
```python
if System.sysIf.ifTimeIsBefore(datetime.time(12, 0)):
    print("Good morning!")
```

#### `System.sysIf.ifTimeIsAfter(time)`

Checks if current time is after a specific time.

**Syntax:**
```python
System.sysIf.ifTimeIsAfter(time)
```

**Parameters:**
- `time` (datetime.time) - Time to check against

**Returns:** Boolean

**Example:**
```python
if System.sysIf.ifTimeIsAfter(datetime.time(18, 0)):
    print("Good evening!")
```

### Use Cases

- Scheduling tasks
- Time-based greetings
- Conditional execution
- Business hours checking

---

## Computer Control

**⚠️ WARNING:** These functions actually control your computer. Use with caution!

### Functions

#### `System.computer.sleep()`

Puts computer into sleep/suspend mode.

**Syntax:**
```python
System.computer.sleep()
```

**Parameters:** None

**Returns:** None

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

**Platform Behavior:**
- Windows: Uses `shutdown /h` (hibernate)
- Linux: Uses `systemctl suspend`
- Mac: Uses `pmset sleepnow`

**Requirements:**
- Windows: May need administrator privileges
- Linux/Mac: Requires sudo privileges

#### `System.computer.reboot()`

Restarts the computer.

**Syntax:**
```python
System.computer.reboot()
```

**Parameters:** None

**Returns:** None

**Example:**
```python
System.log("Rebooting system...")
System.computer.reboot()
```

**Platform Behavior:**
- Windows: Uses `shutdown /r`
- Linux/Mac: Uses `sudo shutdown -r now`

**⚠️ WARNING:** All unsaved work will be lost!

#### `System.computer.shutdown()`

Shuts down the computer completely.

**Syntax:**
```python
System.computer.shutdown()
```

**Parameters:** None

**Returns:** None

**Platform Behavior:**
- Windows: Uses `shutdown /s`
- Linux/Mac: Uses `sudo shutdown -h now`

**⚠️ WARNING:** All unsaved work will be lost!

---

## System Information

### Functions

#### `System.info()`

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
# Output: OS: win32, OS VERSION: Windows-10-10.0.19041 DIP FRAMEWORK VERSION: 1.0, ...
```

---

## Logging System

### Functions

#### `System.log(message)`

Writes a timestamped message to the log file.

**Syntax:**
```python
System.log(message)
```

**Parameters:**
- `message` (string) - Message to log

**Returns:** None

**Log Location:** `DIP_Framework/log.txt`

**Example:**
```python
System.log("Application started")
System.log("User logged in")
System.log("Processing 100 records")
System.log("Operation completed")

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
- Automatic timestamps
- Auto-creates log directory
- Auto-creates log file
- Appends to existing logs

---

# File & Data

## File Operations

File operations are organized under `System.computer.file`.

### Reading Files

#### `System.computer.file.read.read_file(path)`

Reads contents of a text file.

**Syntax:**
```python
System.computer.file.read.read_file(path)
```

**Parameters:**
- `path` (string) - Path to file

**Returns:** String (file contents) or None

**Example:**
```python
content = System.computer.file.read.read_file("document.txt")
if content:
    print(content)
```

### Writing Files

#### `System.computer.file.write.write_file(filepath, content)`

Writes content to a text file.

**Syntax:**
```python
System.computer.file.write.write_file(filepath, content)
```

**Parameters:**
- `filepath` (string) - Where to save
- `content` (string) - Content to write

**Returns:** None

**Example:**
```python
System.computer.file.write.write_file("output.txt", "Hello, World!")
```

#### `System.computer.file.write.write_json(path, json_data)`

Writes data to a JSON file.

**Syntax:**
```python
System.computer.file.write.write_json(path, json_data)
```

**Parameters:**
- `path` (string) - Where to save
- `json_data` (dict/list) - Data to write

**Example:**
```python
data = {"name": "John", "age": 30}
System.computer.file.write.write_json("config.json", data)
```

#### `System.computer.file.write.write_csv(path, csv_data)`

Writes data to a CSV file.

**Syntax:**
```python
System.computer.file.write.write_csv(path, csv_data)
```

**Parameters:**
- `path` (string) - Where to save
- `csv_data` (list of lists) - Data to write

**Data Format:**
```python
data = [
    ['Name', 'Age', 'City'],      # Headers
    ['Alice', '25', 'Boston'],
    ['Bob', '30', 'Chicago']
]
```

**Example:**
```python
System.computer.file.write.write_csv("people.csv", data)
```

#### `System.computer.file.write.write_yaml(path, yaml_data)`

Writes data to a YAML file.

**Syntax:**
```python
System.computer.file.write.write_yaml(path, yaml_data)
```

**Parameters:**
- `path` (string) - Where to save
- `yaml_data` (dict/list) - Data to write

**Example:**
```python
config = {
    "database": {"host": "localhost", "port": 5432},
    "debug": True
}
System.computer.file.write.write_yaml("config.yaml", config)
```

### Directory Management

#### `System.computer.file.ensure_dir(directory, answer)`

Checks if directory exists, optionally creates it.

**Syntax:**
```python
System.computer.file.ensure_dir(directory, answer)
```

**Parameters:**
- `directory` (string) - Path to directory
- `answer` (boolean) - True to create, False to just check

**Returns:** Boolean

**Example:**
```python
# Just check
if System.computer.file.ensure_dir("data", False):
    print("Exists!")

# Create if needed
System.computer.file.ensure_dir("output", True)

# Nested directories
System.computer.file.ensure_dir("data/processed/2024", True)
```

---

## Data Parsing - Local Files

All local file parsing under `System.parse.file`.

### Functions

#### `System.parse.file.json(filepath)`

Parses a JSON file.

**Syntax:**
```python
System.parse.file.json(filepath)
```

**Parameters:**
- `filepath` (string) - Path to JSON file

**Returns:** Dict or list

**Example:**
```python
data = System.parse.file.json("config.json")
print(data["database"]["host"])
```

#### `System.parse.file.csv(filepath)`

Parses a CSV file.

**Syntax:**
```python
System.parse.file.csv(filepath)
```

**Parameters:**
- `filepath` (string) - Path to CSV file

**Returns:** List of dictionaries

**Example:**
```python
data = System.parse.file.csv("contacts.csv")
for row in data:
    print(f"{row['Name']}: {row['Email']}")
```

#### `System.parse.file.yaml(filepath)`

Parses a YAML file.

**Syntax:**
```python
System.parse.file.yaml(filepath)
```

**Parameters:**
- `filepath` (string) - Path to YAML file

**Returns:** Dict or list

**Example:**
```python
config = System.parse.file.yaml("config.yaml")
print(config["database"]["host"])
```

#### `System.parse.file.xml(filepath)`

Parses an XML file.

**Syntax:**
```python
System.parse.file.xml(filepath)
```

**Parameters:**
- `filepath` (string) - Path to XML file

**Returns:** ElementTree object

**Example:**
```python
tree = System.parse.file.xml("data.xml")
for child in tree:
    print(child.tag, child.text)
```

---

## Data Parsing - External URLs

All external URL parsing under `System.grabexternal.parse`.

### Functions

#### `System.grabexternal.parse.json(url)`

Fetches and parses JSON from a URL.

**Syntax:**
```python
System.grabexternal.parse.json(url)
```

**Parameters:**
- `url` (string) - URL to fetch from

**Returns:** Dict or list

**Example:**
```python
weather = System.grabexternal.parse.json("https://api.weather.com/current")
print(weather["temperature"])
```

#### `System.grabexternal.parse.csv(url)`

Fetches and parses CSV from a URL.

**Syntax:**
```python
System.grabexternal.parse.csv(url)
```

**Parameters:**
- `url` (string) - URL to fetch from

**Returns:** List of dictionaries

**Example:**
```python
data = System.grabexternal.parse.csv("https://example.com/data.csv")
```

#### `System.grabexternal.parse.yaml(url)`

Fetches and parses YAML from a URL.

**Syntax:**
```python
System.grabexternal.parse.yaml(url)
```

**Parameters:**
- `url` (string) - URL to fetch from

**Returns:** Dict or list

#### `System.grabexternal.parse.xml(url)`

Fetches and parses XML from a URL.

**Syntax:**
```python
System.grabexternal.parse.xml(url)
```

**Parameters:**
- `url` (string) - URL to fetch from

**Returns:** ElementTree object

**Note:** All external parsing requires internet connection.

---

# Media & Notifications

## Media Playback

### Functions

#### `System.computer.playsound(location)`

Plays an audio file.

**Syntax:**
```python
System.computer.playsound(location)
```

**Parameters:**
- `location` (string) - Path to audio file

**Returns:** None

**Supported Formats:** MP3, WAV, OGG

**Example:**
```python
System.computer.playsound("sounds/notification.mp3")
System.computer.playsound("C:/Users/You/Music/song.wav")
```

**Requirements:**
- playsound3 library
- Working audio output

#### `System.computer.playvideo(location)`

Plays a video file using VLC.

**Syntax:**
```python
System.computer.playvideo(location)
```

**Parameters:**
- `location` (string) - Path to video file

**Returns:** None

**Supported Formats:** MP4, AVI, MKV, MOV

**Example:**
```python
System.computer.playvideo("videos/tutorial.mp4")
```

**Important:**
- Requires VLC media player installed
- Script pauses until video finishes
- Download VLC: https://www.videolan.org/vlc/

---

## Desktop Notifications

### Functions

#### `System.computer.notify(title, message, appname)`

Displays a desktop notification.

**Syntax:**
```python
System.computer.notify(title, message, appname)
```

**Parameters:**
- `title` (string) - Notification title
- `message` (string) - Notification body
- `appname` (string) - Your app name

**Returns:** None

**Example:**
```python
System.computer.notify(
    "Download Complete",
    "Your file has been downloaded!",
    "MyApp"
)
```

**Platform Support:**
- Windows: Native notifications
- Linux: notify-send (needs desktop environment)
- Mac: Notification center

**Note:** Duration fixed at 10 seconds.

---

# Internet & Web

## URL Operations

### Functions

#### `System.openbrowserlink(url)`

Opens a URL in default browser.

**Syntax:**
```python
System.openbrowserlink(url)
```

**Parameters:**
- `url` (string) - URL to open

**Returns:** None

**Example:**
```python
System.openbrowserlink("https://www.github.com")
System.openbrowserlink("https://www.python.org")
```

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

**Platform Behavior:**
- Windows: Uses `start` command
- Linux: Uses `xdg-open` command
- Mac: Uses `open` command

---

## Currency Conversion

### Functions

#### `System.internet.convert_currency(amount, original_currency, converted_currency)`

Converts money between currencies using live rates.

**Syntax:**
```python
System.internet.convert_currency(amount, original_currency, converted_currency)
```

**Parameters:**
- `amount` (number) - Amount to convert
- `original_currency` (string) - Source currency (ISO 4217 code)
- `converted_currency` (string) - Target currency (ISO 4217 code)

**Returns:** Float (converted amount)

**Example:**
```python
# Convert 100 USD to EUR
result = System.internet.convert_currency(100, "USD", "EUR")
print(f"100 USD = {result} EUR")

# Convert 50 GBP to JPY
result = System.internet.convert_currency(50, "GBP", "JPY")
```

**Common Currency Codes:**
- USD - US Dollar
- EUR - Euro
- GBP - British Pound
- JPY - Japanese Yen
- CAD - Canadian Dollar
- AUD - Australian Dollar

**Requirements:**
- Internet connection
- freecurrencyapi library

---

## Internet Utilities

### Functions

#### `System.internet.extract_domain(url)`

Parses a URL and extracts components.

**Syntax:**
```python
System.internet.extract_domain(url)
```

**Parameters:**
- `url` (string) - URL to parse

**Returns:** ParseResult object

**Available Properties:**
- `scheme` - URL scheme (http, https, etc.)
- `netloc` - Network location/domain
- `path` - Path to resource
- `query` - Query string
- `fragment` - Fragment identifier

**Example:**
```python
parsed = System.internet.extract_domain("https://www.github.com/user/repo?tab=readme")

print(parsed.scheme)    # https
print(parsed.netloc)    # www.github.com
print(parsed.path)      # /user/repo
print(parsed.query)     # tab=readme

# Extract just domain
domain = System.internet.extract_domain(url).netloc
```

**Use Cases:**
- Extract domain names
- Validate URL structure
- Parse query parameters
- Security checks

---

# Reference

## Best Practices

### Error Handling

Always wrap potentially failing operations:

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

### System Control

Always warn users:

```python
print("WARNING: This will reboot your computer!")
response = input("Continue? (yes/no): ")
if response.lower() == "yes":
    System.computer.reboot()
```

---

## Troubleshooting

### Module Not Found

**Problem:** `ModuleNotFoundError`

**Solution:**
```bash
pip install psutil requests pyyaml playsound3 python-vlc plyer freecurrencyapi
```

### Video Won't Play

**Problem:** Videos don't play

**Solution:**
- Install VLC: https://www.videolan.org/vlc/
- Install python-vlc: `pip install python-vlc`

### Notifications Not Showing

**Problem:** Desktop notifications don't appear

**Solutions:**
- Need desktop environment (not headless server)
- Linux: Check notification daemon running
- Verify system notification settings

### Permission Denied

**Problem:** Can't sleep/reboot/shutdown

**Solutions:**
- Windows: Run as Administrator
- Linux/Mac: Use sudo: `sudo python script.py`

### Currency Conversion Fails

**Problem:** Currency errors

**Solutions:**
- Check internet connection
- Verify currency codes (ISO 4217)
- API rate limits - wait and retry

### File Not Found

**Problem:** Can't find files

**Solutions:**
- Use absolute paths
- Check file exists: `os.path.exists("file.json")`
- Verify spelling and extension

### REHH Issues

**Problem:** Server won't start

**Solutions:**
- Try different port
- Use ports above 1024
- Check port not already in use

---

## Platform Support

### Windows

**Supported Features:**
- ✅ All console operations
- ✅ All time checking
- ✅ All media playback
- ✅ Desktop notifications
- ✅ All file operations
- ✅ System control (admin for reboot/shutdown)
- ✅ All data parsing
- ✅ Currency conversion
- ✅ All URL operations
- ✅ REHH web hosting

**Requirements:**
- Python 3.x
- VLC (for video)

### Linux

**Supported Features:**
- ✅ All console operations
- ✅ All time checking
- ✅ All media playback
- ✅ Desktop notifications (with desktop environment)
- ✅ All file operations
- ✅ System control (requires sudo)
- ✅ All data parsing
- ✅ Currency conversion
- ✅ All URL operations
- ✅ REHH web hosting

**Requirements:**
- Python 3.x
- VLC media player
- Desktop environment (for notifications)
- sudo (for system control)

### macOS

**Supported Features:**
- ✅ All console operations
- ✅ All time checking
- ✅ All media playback
- ✅ Desktop notifications
- ✅ All file operations
- ✅ System control (requires sudo)
- ✅ All data parsing
- ✅ Currency conversion
- ✅ All URL operations
- ✅ REHH web hosting

**Requirements:**
- Python 3.x
- VLC
- sudo (for system control)

---

## API Quick Reference

### Console Module

```python
Console.clear()                                      # Clear screen
```

### System Module - Basic

```python
System.info()                                        # System information
System.log(message)                                  # Log message
System.openbrowserlink(url)                          # Open URL
```

### Time Checking

```python
System.sysIf.ifTimeIs(time)                         # Check exact time
System.sysIf.ifTimeIsBefore(time)                   # Check before time
System.sysIf.ifTimeIsAfter(time)                    # Check after time
```

### Computer Control

```python
System.computer.sleep()                              # Sleep computer
System.computer.reboot()                             # Reboot computer
System.computer.shutdown()                           # Shutdown computer
```

### File Operations - Read

```python
System.computer.file.read.read_file(path)           # Read text file
System.computer.file.ensure_dir(dir, answer)        # Check/create directory
```

### File Operations - Write

```python
System.computer.file.write.write_file(path, content)     # Write text
System.computer.file.write.write_json(path, data)        # Write JSON
System.computer.file.write.write_csv(path, data)         # Write CSV
System.computer.file.write.write_yaml(path, data)        # Write YAML
```

### Data Parsing - Local

```python
System.parse.file.json(filepath)                     # Parse JSON
System.parse.file.csv(filepath)                      # Parse CSV
System.parse.file.yaml(filepath)                     # Parse YAML
System.parse.file.xml(filepath)                      # Parse XML
```

### Data Parsing - External

```python
System.grabexternal.parse.json(url)                  # Parse JSON from URL
System.grabexternal.parse.csv(url)                   # Parse CSV from URL
System.grabexternal.parse.yaml(url)                  # Parse YAML from URL
System.grabexternal.parse.xml(url)                   # Parse XML from URL
```

### Media

```python
System.computer.playsound(location)                  # Play audio
System.computer.playvideo(location)                  # Play video
```

### Notifications

```python
System.computer.notify(title, message, appname)      # Desktop notification
```

### Internet

```python
System.internet.convert_currency(amt, from, to)      # Convert currency
System.internet.extract_domain(url)                  # Parse URL
```

### REHH Module

```python
REHH.start_rehh(config_path)                        # Start HTTP server
```

---

## Additional Information

### Framework Version

Current version: **1.0**

Access programmatically:
```python
print(System.DIP_FRAMEWORK_VERSION)  # 1.0
```

### File Encoding

All file operations use UTF-8 encoding by default.

### Exception Handling

All functions include built-in exception handling via `retEx()`.

### Thread Safety

Not thread-safe by default. Implement locking for multi-threaded use.

### Performance

- File parsing is synchronous (blocking)
- Video playback blocks until complete
- Currency conversion requires network request
- System control is immediate

---

## Getting Help

### Documentation

- **README:** Quick overview
- **This Document:** Complete API reference

### Community

- **GitHub Issues:** Bug reports and features
- **GitHub Discussions:** Questions and ideas

### Contributing

Contributions welcome! See README.md for guidelines.

---

**DIP Framework v1.0 Documentation**

*Last Updated: December 2024*

**Made with ❤️ by the Druzhba Specifications team**
