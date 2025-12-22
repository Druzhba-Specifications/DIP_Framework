# DIP Framework

**A simple Python toolkit that makes system operations, media playback, and data parsing easy!**

Perfect for beginners who want to control their computer, play media, and work with data files without the complexity.

---

## Table of Contents

1. [What is DIP Framework?](#what-is-dip-framework)
2. [What Can It Do?](#what-can-it-do)
3. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Requirements](#requirements)
4. [Quick Examples](#quick-examples)
   - [Console Operations](#console-operations)
   - [Working with Time](#working-with-time)
   - [Playing Media](#playing-media)
   - [System Control](#system-control)
   - [Opening Websites](#opening-websites)
   - [Logging Messages](#logging-messages)
   - [Reading Data Files](#reading-data-files)
5. [Complete Feature Guide](#complete-feature-guide)
   - [Console Module](#console-module)
   - [System Module](#system-module)
   - [Time Checking](#time-checking)
   - [Computer Control](#computer-control)
   - [Media Playback](#media-playback)
   - [Data Parsing](#data-parsing)
6. [Important Things to Know](#important-things-to-know)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)
9. [License](#license)

---

## What is DIP Framework?

DIP Framework is a collection of Python tools that makes complicated tasks simple. Instead of writing lots of code to do basic things like clearing your screen, playing a video, or reading a data file, you can do it with just one or two lines!

**Current Version:** 1.0

---

## What Can It Do?

✅ **Clear your console screen** - Make your terminal clean and organized  
✅ **Check the time** - Run code at specific times of day  
✅ **Play sounds and videos** - Add media to your programs  
✅ **Control your computer** - Sleep, restart, or shutdown (be careful!)  
✅ **Open websites** - Launch URLs in your default browser  
✅ **Keep logs** - Track what your program is doing  
✅ **Read data files** - Work with JSON, CSV, YAML, and XML files  
✅ **Get system info** - Find out about your computer's hardware and software  
✅ **Works everywhere** - Windows, Mac, and Linux support

---

## Getting Started

### Installation

**Step 1:** Download or clone the framework
```bash
git clone https://github.com/Druzhba-Specifications/DIP_Framework.git
cd DIP_Framework
```

**Step 2:** Install required packages
```bash
pip install psutil requests pyyaml playsound3 python-vlc ply
```

**Step 3:** You're ready to go! 🎉

### Requirements

- Python 3.x (any version of Python 3)
- The packages listed above (installed with pip)

---

## Quick Examples

Here are some simple examples to get you started!

### Console Operations

**Clear your terminal screen:**
```python
import Console

Console.clear()  # Poof! Clean screen
```

### Working with Time

**Do something only in the afternoon:**
```python
import System
import datetime

# Check if it's after 2:30 PM
if System.sysIf.ifTimeIsAfter(datetime.time(14, 30)):
    print("Good afternoon!")
```

**Check if it's before noon:**
```python
if System.sysIf.ifTimeIsBefore(datetime.time(12, 0)):
    print("Good morning!")
```

### Playing Media

**Play a sound effect:**
```python
import System

System.computer.playsound("beep.mp3")
```

**Play a video:**
```python
System.computer.playvideo("myvideo.mp4")
# The video will play until it's finished!
```

### System Control

**⚠️ Warning: These commands actually control your computer!**

**Put your computer to sleep:**
```python
System.computer.sleep()
```

**Restart your computer:**
```python
System.computer.reboot()
```

**Shut down your computer:**
```python
System.computer.shutdown()
```

### Opening Websites

**Open a website in your browser:**
```python
System.openlink("https://www.github.com")
```

### Logging Messages

**Keep track of what your program does:**
```python
System.log("Program started")
System.log("User logged in")
System.log("Data saved successfully")
```

Logs are saved in `DIP_Framework/log.txt` with timestamps!

### Reading Data Files

**Read a JSON file:**
```python
data = System.parse.json("config.json")
print(data)
```

**Read a CSV file (like a spreadsheet):**
```python
data = System.parse.csv("contacts.csv")
for row in data:
    print(row)
```

**Get data from a website:**
```python
# Get JSON from an API
weather = System.grabexternal.parse.json("https://api.weather.com/data.json")
print(weather)
```

---

## Complete Feature Guide

### Console Module

Import it like this:
```python
import Console
```

#### `Console.clear()`
**What it does:** Clears everything from your terminal screen  
**How to use:**
```python
Console.clear()
```
**Works on:** Windows, Mac, Linux

---

### System Module

Import it like this:
```python
import System
```

#### System Information

#### `System.info()`
**What it does:** Shows information about your computer  
**How to use:**
```python
System.info()
```
**Shows you:**
- Your operating system
- Your CPU information
- Your Python version
- DIP Framework version
- CPU temperature (if available)

#### `System.openlink(url)`
**What it does:** Opens a website in your default browser  
**How to use:**
```python
System.openlink("https://www.python.org")
```

#### `System.log(message)`
**What it does:** Saves a message to a log file with the current date and time  
**How to use:**
```python
System.log("Something important happened!")
```
**Where logs are saved:** `DIP_Framework/log.txt`

---

### Time Checking

These help you run code at specific times!

#### `System.sysIf.ifTimeIs(time)`
**What it does:** Checks if it's exactly a certain time  
**How to use:**
```python
import datetime
if System.sysIf.ifTimeIs(datetime.time(15, 30)):
    print("It's exactly 3:30 PM!")
```

#### `System.sysIf.ifTimeIsBefore(time)`
**What it does:** Checks if the current time is before a certain time  
**How to use:**
```python
if System.sysIf.ifTimeIsBefore(datetime.time(12, 0)):
    print("It's still morning!")
```

#### `System.sysIf.ifTimeIsAfter(time)`
**What it does:** Checks if the current time is after a certain time  
**How to use:**
```python
if System.sysIf.ifTimeIsAfter(datetime.time(18, 0)):
    print("Time to go home!")
```

---

### Computer Control

**⚠️ Important:** These actually control your computer! Use carefully!

#### `System.computer.sleep()`
**What it does:** Puts your computer into sleep mode (like closing a laptop)  
**How to use:**
```python
System.computer.sleep()
```
**Note:** On Mac/Linux, you might need administrator permissions

#### `System.computer.reboot()`
**What it does:** Restarts your computer  
**How to use:**
```python
System.computer.reboot()
```
**Note:** Make sure to save your work first!

#### `System.computer.shutdown()`
**What it does:** Turns off your computer completely  
**How to use:**
```python
System.computer.shutdown()
```
**Note:** All unsaved work will be lost!

---

### Media Playback

#### `System.computer.playsound(location)`
**What it does:** Plays an audio file  
**How to use:**
```python
System.computer.playsound("music.mp3")
System.computer.playsound("C:/Users/You/sounds/beep.wav")
```
**Supported formats:** MP3, WAV, and other common audio formats

#### `System.computer.playvideo(location)`
**What it does:** Plays a video file  
**How to use:**
```python
System.computer.playvideo("movie.mp4")
```
**Important:** 
- Requires VLC media player installed on your computer
- Your program will wait until the video finishes playing
- Works with MP4, AVI, MKV, and other video formats

---

### Data Parsing

Reading data files is now super easy!

#### Reading Local Files

**JSON Files** (like config files):
```python
data = System.parse.json("settings.json")
```

**CSV Files** (like spreadsheets):
```python
data = System.parse.csv("data.csv")
# Returns a list of dictionaries, one for each row
```

**YAML Files** (configuration files):
```python
data = System.parse.yaml("config.yaml")
```

**XML Files** (structured documents):
```python
data = System.parse.xml("document.xml")
```

#### Reading from Websites/APIs

Same formats, but from the internet!

**JSON from API:**
```python
data = System.grabexternal.parse.json("https://api.example.com/data.json")
```

**CSV from URL:**
```python
data = System.grabexternal.parse.csv("https://example.com/data.csv")
```

**YAML from URL:**
```python
data = System.grabexternal.parse.yaml("https://example.com/config.yaml")
```

**XML from URL:**
```python
data = System.grabexternal.parse.xml("https://example.com/feed.xml")
```

---

## Important Things to Know

### 🔒 Permissions

**On Windows:**
- Most features work without special permissions
- System shutdown/reboot might need administrator rights

**On Mac/Linux:**
- System control commands (sleep, reboot, shutdown) need `sudo` permissions
- You might be asked for your password

### 🎵 Media Playback

**For audio:**
- Just needs the `playsound3` package (installed automatically)
- Works with common audio formats (MP3, WAV, etc.)

**For video:**
- Requires VLC media player installed on your computer
- Download VLC from: https://www.videolan.org/vlc/
- Your script will pause while the video plays

### 📝 Logging

- Logs are saved automatically in the `DIP_Framework` folder
- Each log entry includes the date and time
- The log file is created automatically if it doesn't exist
- Great for debugging and tracking your program's behavior

### 🌐 Internet Connection

- Parsing from URLs (`grabexternal.parse.*`) needs an internet connection
- If the website is down, you'll get an error message
- Local file parsing works offline

### ⚠️ Error Handling

- All functions have built-in error handling
- If something goes wrong, you'll get a helpful error message
- Common errors include:
  - File not found (check your file path)
  - Invalid data format (check your file format)
  - Permission denied (try running with admin/sudo)
  - No internet connection (for external URLs)

---

## Troubleshooting

### "Module not found" error
**Solution:** Install the required packages:
```bash
pip install psutil requests pyyaml playsound3 python-vlc ply
```

### Video won't play
**Solution:** Install VLC media player from https://www.videolan.org/vlc/

### "Permission denied" on system control
**Solution:** 
- **Windows:** Run your script as Administrator (right-click → Run as Administrator)
- **Mac/Linux:** Use `sudo python your_script.py`

### File not found when parsing
**Solution:** 
- Check that your file path is correct
- Use full paths like `C:/Users/You/file.json` if needed
- Make sure the file actually exists

### Can't clear console
**Solution:** This is rare, but make sure your terminal supports clear commands (most do!)

---

## Contributing

Want to help make DIP Framework better? Great!

**How to contribute:**
1. Fork the repository
2. Make your changes
3. Keep code organized and well-commented
4. Update this README if you add features
5. Test on multiple platforms if possible
6. Submit a pull request

**Ideas for contributions:**
- Add more file formats
- Improve error messages
- Add new features
- Fix bugs
- Improve documentation

---

## License

**Creative Commons CC0 1.0 Universal License**

This means the code is in the public domain - you can use it for anything, no restrictions!

See [LICENSE.txt](LICENSE.txt) for full details.

---

## Project Structure

Here's what's in the framework:

```
DIP_Framework/
├── README.md           ← You are here!
├── LICENSE.txt         ← Legal stuff
├── System.py           ← Main system operations
├── Console.py          ← Console utilities
└── DIP_Framework/
    └── log.txt         ← Your logs appear here
```

---

## Support

Need help? Have questions?

- 🐛 **Bug reports:** [Open an issue](https://github.com/Druzhba-Specifications/DIP_Framework/issues)
- 💡 **Feature requests:** [Open an issue](https://github.com/Druzhba-Specifications/DIP_Framework/issues)
- 📧 **Questions:** Check the examples above or open an issue

---

## Credits

Built with these awesome tools:
- **psutil** - System monitoring
- **requests** - Internet requests
- **PyYAML** - YAML parsing
- **playsound3** - Audio playback
- **python-vlc** - Video playback
- **PLY** - Parsing toolkit

---

**Made with ❤️ by the Druzhba Specifications team**

*Happy coding! 🚀*