# DIP Framework

**A simple Python toolkit that makes system operations, media playback, and data parsing easy!**

Perfect for beginners who want to control their computer, play media, and work with data files without the complexity.

---

## What is DIP Framework?

DIP Framework is a collection of Python tools that makes complicated tasks simple. Instead of writing lots of code to do basic things like clearing your screen, playing a video, or reading a data file, you can do it with just one or two lines!

**Why DIP Framework?**

Instead of remembering platform-specific commands like:
- Windows: `os.system('cls')` vs Linux: `os.system('clear')`
- Windows: `os.system('start url')` vs Linux: `os.system('xdg-open url')`
- Windows: `os.system('shutdown /s')` vs Linux: `subprocess.run(['sudo', 'shutdown', '-h', 'now'])`

Just use DIP Framework:
- `Console.clear()` - works everywhere!
- `System.openbrowserlink(url)` - works everywhere!
- `System.computer.shutdown()` - works everywhere!

**One simple function. Any platform. No headaches.**

**Current Version:** 1.0

---

## Features

✅ **Clear your console screen** - Make your terminal clean and organized  
✅ **Check the time** - Run code at specific times of day  
✅ **Play sounds and videos** - Add media to your programs  
✅ **Send notifications** - Show desktop notifications to users  
✅ **Control your computer** - Sleep, restart, or shutdown (be careful!)  
✅ **File operations** - Read, write, and check if files/folders exist  
✅ **Open websites** - Launch URLs in your default browser  
✅ **Keep logs** - Track what your program is doing  
✅ **Read data files** - Work with JSON, CSV, YAML, and XML files  
✅ **Currency conversion** - Convert between different currencies  
✅ **URL parsing** - Extract domain information from URLs  
✅ **Get system info** - Find out about your computer's hardware and software  
✅ **Host websites easily** - REHH module for simple HTTP hosting  
✅ **Works everywhere** - Windows, Mac, and Linux support

---

## Quick Start

### Installation

**Step 1:** Download the latest release

**For stable features (recommended):**
- Go to [Releases](https://github.com/Druzhba-Specifications/DIP_Framework/releases)
- Download the latest release (e.g., `v1.0.0-pre.1`)
- Extract the files

**For beta features (REHH module):**
```bash
git clone https://github.com/Druzhba-Specifications/DIP_Framework.git
cd DIP_Framework
```

**Step 2:** Install required packages
```bash
pip install psutil requests pyyaml playsound3 python-vlc plyer freecurrencyapi
```

**Step 3:** You're ready to go! 🎉

### Simple Example

```python
import System
import Console
import REHH

# Clear the screen
Console.clear()

# Log a message
System.log("Program started")

# Show a notification
System.computer.notify("Hello", "DIP Framework is ready!", "MyApp")

# Check the time
import datetime
if System.sysIf.ifTimeIsAfter(datetime.time(14, 30)):
    print("Good afternoon!")

# Play a sound
System.computer.playsound("beep.mp3")

# Read a JSON file
data = System.parse.file.json("config.json")
print(data)

# Host a website (REHH module)
REHH.start_rehh("config.xml")  # Starts HTTP server based on XML config
```

---

## Documentation

For complete documentation with all features, examples, and API reference, see **[DOCUMENTATION.md](DOCUMENTATION.md)**

Quick links:
- [Console Operations](DOCUMENTATION.md#console-module)
- [Time Checking](DOCUMENTATION.md#time-checking)
- [Media Playback](DOCUMENTATION.md#media-playback)
- [File Operations](DOCUMENTATION.md#file-operations-1)
- [Data Parsing](DOCUMENTATION.md#data-parsing)
- [Currency Conversion](DOCUMENTATION.md#currency-conversion-1)
- [REHH Web Hosting](DOCUMENTATION.md#rehh-module)

---

## Requirements

- Python 3.x (any version of Python 3)
- psutil - System monitoring
- requests - Web requests
- pyyaml - YAML file support
- playsound3 - Audio playback
- python-vlc - Video playback
- plyer - Desktop notifications
- freecurrencyapi - Currency conversion

---

## Project Structure

```
DIP_Framework/
├── README.md                          # You are here!
├── DOCUMENTATION.md                   # Complete documentation
├── LICENSE.txt                        # CC0 1.0 Universal License
├── System.py                          # Core system operations
├── Console.py                         # Console utilities
├── REHH.py                            # Really Easy HTTP Hosting module
├── script.py                          # Example usage
├── REHH/
│   ├── example.xml                    # Example REHH config
│   └── rehh.txt                       # REHH information
└── DIP_Framework/
    └── log.txt                        # Application logs
```

---

## Important Notes

⚠️ **System Control** - Commands like shutdown and reboot actually control your computer! Use carefully.

🔑 **Permissions** - Some features need admin/sudo privileges on Mac/Linux.

🎵 **VLC Required** - Video playback needs VLC media player installed.

🌐 **Internet Required** - Currency conversion and external data parsing need internet.

📡 **REHH Module** - Beta feature for easy HTTP hosting. Use with caution in production.

---

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to help improve the DIP Framework.

When contributing, please:
1. Maintain code separation into logical groups
2. Update the documentation with any new features
3. Include error handling in new functions
4. Test on multiple platforms when possible

---

## Support

Need help? Have questions?

- 🐛 **Bug reports:** [Open an issue](https://github.com/Druzhba-Specifications/DIP_Framework/issues)
- 💡 **Feature requests:** [Open an issue](https://github.com/Druzhba-Specifications/DIP_Framework/issues)
- 📖 **Documentation:** See [DOCUMENTATION.md](DOCUMENTATION.md)

---

## License

This project is licensed under the **Creative Commons CC0 1.0 Universal License**, which means it is in the public domain. See [LICENSE.txt](LICENSE.txt) for details.

---

## Credits

Built with these awesome tools:
- **psutil** - System monitoring
- **requests** - Internet requests
- **PyYAML** - YAML parsing
- **playsound3** - Audio playback
- **python-vlc** - Video playback
- **plyer** - Cross-platform notifications
- **freecurrencyapi** - Currency conversion with live rates

---

**Made with ❤️ by the Druzhba Specifications team**

*Happy coding! 🚀*
