# DIP Framework

A Python utility framework designed to simplify system operations, console interactions, and cross-platform functionality. The DIP Framework provides easy-to-use abstractions for common tasks like system control, file logging, and platform-specific operations.

## Features

### System Operations
- **Time-based conditionals**: Check system time for scheduling and conditional logic
- **System control**: Sleep, reboot, and shutdown functionality with cross-platform support (Windows, Linux, macOS)
- **System information**: Retrieve detailed OS, CPU, and Python version information
- **URL opening**: Open links in the default browser across different operating systems

### Console Management
- **Simple output**: Consistent console writing functionality
- **Screen clearing**: Clear console output cross-platform

### File Logging
- **Persistent logging**: Automatic log file creation and management
- **Organized storage**: Logs stored in the `DIP_Framework/log.txt` file

### Data Format Support
The framework supports multiple data formats:
- JSON
- CSV
- YAML
- XML

## Installation

Clone the repository:
```bash
git clone https://github.com/Druzhba-Specifications/DIP_Framework.git
cd DIP_Framework
```

## Requirements

- Python 3.x
- `psutil` - For system resource monitoring
- `requests` - For HTTP operations
- `pyyaml` - For YAML parsing
- `lxml` - For XML processing (optional)

Install dependencies:
```bash
pip install psutil requests pyyaml
```

## Quick Start

### Import the Framework
```python
import System
import Console
```

### Basic Usage Examples

**Logging a message:**
```python
System.log("Application started")
```

**Writing to console:**
```python
Console.write("Hello, DIP Framework!")
```

**Clear the console:**
```python
Console.clear()
```

**Check system time:**
```python
if System.sysIf.ifTimeIsAfter("14:30:00"):
    print("Good afternoon!")
```

**Get your system information:**
```python
System.info()
```

**Open a URL:**
```python
System.openlink("https://github.com")
```

**System control (with caution!):**
```python
System.computer.sleep()      # Put computer to sleep
System.computer.reboot()     # Reboot the system
System.computer.shutdown()   # Shutdown the system
```

## Project Structure

```
DIP_Framework/
├── README.md                          # This file
├── LICENSE.txt                        # CC0 1.0 Universal License
├── Druzhba Specifications DIP Framework/
│   ├── System.py                      # Core system operations
│   ├── Console.py                     # Console utilities
│   └── script.py                      # Example usage
├── DIP_Framework/
│   └── log.txt                        # Application logs
└── __pycache__/                       # Python cache files
```

## API Reference

### System Module (`System.py`)

#### Time Conditionals (`sysIf` class)
- `ifTimeIs(time)` - Check if current time matches
- `ifTimeIsBefore(time)` - Check if current time is before specified time
- `ifTimeIsAfter(time)` - Check if current time is after specified time

#### Computer Control (`computer` class)
- `sleep()` - Suspend the system
- `reboot()` - Restart the system
- `shutdown()` - Power off the system

#### Utility Functions
- `openlink(url)` - Open URL in default browser
- `info()` - Display system information (OS, CPU, Python version, etc.)
- `log(message)` - Write message to log file

### Console Module (`Console.py`)

- `write(message)` - Print message to console
- `clear()` - Clear console screen

## Supported Platforms

- **Windows** (Python 3.x)
- **Linux** (Python 3.x)
- **macOS** (Python 3.x)

Each operation includes platform-specific implementations to ensure compatibility.

## License

This project is licensed under the **Creative Commons CC0 1.0 Universal License**, which means it is in the public domain. See [LICENSE.txt](LICENSE.txt) for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to help improve the DIP Framework.

## Framework Version

Current version: **1.0**

## Notes

- The framework includes exception handling for most operations, with detailed error messages logged
- Some features are marked for future implementation (e.g., enhanced exception handling)
- Logging is automatically created in the `DIP_Framework/` directory
- Administrator/sudo privileges may be required for system control operations (reboot, shutdown) on some platforms

## Support & Issues

For bug reports and feature requests, please open an issue on the [GitHub repository](https://github.com/Druzhba-Specifications/DIP_Framework/issues).

---

**Made with ❤️ by the Druzhba Specifications team**
