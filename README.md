# VeilStrike

![GitHub](https://img.shields.io/github/license/xdrew87/VeilStrike?style=flat-square)
![Python](https://img.shields.io/badge/python-3.7+-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)

> **A powerful CDN exposure & origin intelligence scanner for discovering unprotected web server origins.**

VeilStrike is a specialized tool designed to identify and resolve origin IP addresses of websites **NOT protected by Cloudflare** or other CDN providers. Built for security researchers, penetration testers, and OSINT investigators, it provides fast and reliable origin discovery on unprotected targets.

---

## Table of Contents

- [Features](#-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Examples](#examples)
- [Disclaimer](#-disclaimer)
- [Credits](#-credits)
- [License](#license)

---

## 🎯 Features

- ✅ **Origin IP Discovery** - Uncover real IP addresses of unprotected web servers
- ✅ **CDN Detection** - Identify if a site is behind Cloudflare or other protection
- ✅ **IP Resolution** - Resolve both IPv4 and IPv6 addresses
- ✅ **Server Fingerprinting** - Extract web server headers and identify technologies
- ✅ **Batch Scanning** - Process multiple targets efficiently
- ✅ **JSON Export** - Integrate with other tools and workflows
- ✅ **Lightweight & Fast** - Optimized for speed and minimal dependencies
- ✅ **OSINT Ready** - Perfect for security research and investigations

---

## Requirements

- Python 3.7 or higher
- `requests` library
- `colorama` library (for colored output)
- Valid SecurityTrails API key (optional, for enhanced results)

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/xdrew87/VeilStrike.git
cd VeilStrike
pip install -r requirements.txt
```

---

## Configuration

To use SecurityTrails API for enhanced origin detection, configure your API key in `config.ini`:

```ini
[API_KEYS]
SECURITYTRAILS_API_KEY = YOUR_KEY_HERE
```

> **Note:** Get your free API key from [SecurityTrails Dashboard](https://securitytrails.com)

---

## Usage

### Basic Usage

Scan a single domain:

```bash
python veilstrike.py example.com
```

### JSON Output

Export results in JSON format for automation:

```bash
python veilstrike.py example.com --json
```

### Batch Scanning

Scan multiple domains from a file:

```bash
python veilstrike.py sites.txt --json
```

---

## Examples

**Single Domain Scan:**
```
$ python veilstrike.py google.com
[+] Target: google.com
[+] Cloudflare: No
[+] Origin IP: 142.251.32.46
[+] Server: gws
```

**JSON Export:**
```bash
python veilstrike.py google.com --json > results.json
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a pull request

---

## ⚖️ Disclaimer

This tool is provided **for authorized security testing and OSINT research only**. Users are solely responsible for ensuring they have proper authorization to scan target websites. Unauthorized access to computer systems is illegal. Always follow applicable laws and obtain written permission before conducting security assessments.

---

## 📝 Credits

This project was inspired by and built upon the excellent work from [**CloakQuest3r**](https://github.com/spyboy-productions/CloakQuest3r) by [spyboy-productions](https://github.com/spyboy-productions). 

VeilStrike extends and optimizes the original concept with:
- Enhanced non-Cloudflare origin discovery
- Improved resolution accuracy
- Additional technological fingerprinting
- Better performance and reliability

---

## License

MIT License - See [LICENSE](LICENSE) file for details

---

**⭐ If you find this tool useful, please consider giving it a star!**