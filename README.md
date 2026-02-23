# 🎯 VeilStrike

<div align="center">

![License](https://img.shields.io/badge/license-AGPL--3.0-blue?style=flat-square)
![Python](https://img.shields.io/badge/python-3.7+-blue?style=flat-square)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)
![Version](https://img.shields.io/badge/version-1.0.0-orange?style=flat-square)

**A powerful CDN exposure & origin intelligence scanner for discovering unprotected web server origins.**

*Uncover real IP addresses of websites NOT protected by Cloudflare and other CDN providers*

</div>

---

## 💡 Overview

VeilStrike is a specialized reconnaissance tool designed to identify and resolve origin IP addresses of websites **NOT protected by Cloudflare** or other CDN providers. Built for security researchers, penetration testers, and OSINT investigators, it provides fast and reliable origin discovery on unprotected targets with advanced fingerprinting capabilities.

## 📑 Quick Navigation

<table>
<tr>
<td><a href="#-features">✨ Features</a></td>
<td><a href="#-quick-start">🚀 Quick Start</a></td>
<td><a href="#-usage-guide">📖 Usage</a></td>
<td><a href="#-examples">💻 Examples</a></td>
<td><a href="#-license">⚖️ License</a></td>
</tr>
</table>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 **Origin IP Discovery** | Uncover real IP addresses of unprotected web servers with precision |
| 🛡️ **CDN Detection** | Identify if a site is behind Cloudflare or other protection layers |
| 🌐 **Dual Protocol Support** | Resolve both IPv4 and IPv6 addresses seamlessly |
| 🔎 **Server Fingerprinting** | Extract web server headers and identify technologies in use |
| ⚡ **Batch Processing** | Efficiently process multiple targets from wordlists |
| 📊 **JSON Export** | Export results in structured JSON for tool integration |
| 🚀 **Lightweight & Fast** | Optimized for speed with minimal dependencies |
| 🕵️ **OSINT Ready** | Purpose-built for security research and investigations |

---

## 📋 Requirements

```
Python 3.7+
requests library
colorama library (for colored output)
SecurityTrails API key (optional)
```

| Requirement | Purpose |
|-------------|---------|
| **Python 3.7+** | Core runtime environment |
| **requests** | HTTP library for making API calls |
| **colorama** | Enhanced console output styling |
| **SecurityTrails API** | *(Optional)* Enhanced origin detection accuracy |

---

## 🚀 Quick Start

### Installation

Clone the repository and install dependencies:

```bash
# Clone the repository
git clone https://github.com/xdrew87/VeilStrike.git
cd VeilStrike

# Install required dependencies
pip install -r requirements.txt
```

### Configuration (Optional)

To use SecurityTrails API for enhanced origin detection, create/update `config.ini`:

```ini
[API_KEYS]
SECURITYTRAILS_API_KEY = YOUR_API_KEY_HERE
```

> 💡 Get your free API key from [SecurityTrails Dashboard](https://securitytrails.com)

---

## 📖 Usage Guide

### Single Target Scan

```bash
python veilstrike.py example.com
```

### JSON Output for Integration

```bash
python veilstrike.py example.com --json
```

### Batch Scanning from File

```bash
python veilstrike.py targets.txt --json
```

### Output Options

| Flag | Purpose |
|------|---------|
| `--json` | Export results in JSON format |
| `-o FILE` | Save output to specified file |
| `-v` | Verbose mode with detailed information |

---

## 💻 Examples

### Example 1: Single Domain Scan

```bash
$ python veilstrike.py google.com
```

**Output:**
```
[+] Target: google.com
[+] Cloudflare: No
[+] Origin IP: 142.251.32.46
[+] Server: gws
[+] Country: US
```

### Example 2: JSON Export

```bash
python veilstrike.py google.com --json > results.json
```

### Example 3: Batch Scanning

```bash
python veilstrike.py targets.txt --json -o batch_results.json
```

### Example 4: Verbose Mode

```bash
python veilstrike.py example.com -v
```

---

## 📸 Screenshots

VeilStrike provides clean, color-coded output for easy analysis:
<div align="center">

![VeilStrike Sample Output](https://github.com/user-attachments/assets/f55922bd-d7b6-4ce7-8c1e-0d9abbdac9ae)

</div>

**Example Console Output:**
```
╔════════════════════════════════════════════════════════════════════╗
║                        VEILSTRIKE v1.0.0                          ║
║            CDN Exposure & Origin Intelligence Scanner             ║
╚════════════════════════════════════════════════════════════════════╝

[+] Version          : 1.0.0
[+] Author           : Galmx
[+] GitHub           : https://github.com/xdrew87/VeilStrike
[+] Module           : CDN Detection | Origin Resolution

────────────────────────────────────────────────────────────────────
[*] Scanning Target: google.com
────────────────────────────────────────────────────────────────────

✓ Cloudflare Detected  : False
✓ Web Server           : gws
✓ IPv4 Addresses       : 142.251.127.101, 142.251.127.139
                         142.251.127.113, 142.251.127.100
                         142.251.127.138
✓ IPv6 Address         : 2a00:1450:4001:804::200e
✓ Country              : United States
✓ ASN                  : AS15169 (Google LLC)

────────────────────────────────────────────────────────────────────
[+] Scan completed successfully!
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Submit** a Pull Request

### Contribution Ideas
- 🐛 Bug fixes and improvements
- 📚 Documentation enhancements
- ⚡ Performance optimizations
- 🔧 New detection methods
- 📊 Additional export formats

---

## ⚖️ Legal & Disclaimer

> ⚠️ **IMPORTANT**: This tool is provided **for authorized security testing and OSINT research only**.

**Users are solely responsible for ensuring they have proper authorization before using this tool.**

### Key Points:
- 🔒 Only scan targets you own or have explicit written permission to test
- ⚖️ Unauthorized access to computer systems is **illegal**
- 📋 Always comply with applicable laws and regulations
- 💼 Obtain written authorization before conducting security assessments
- 🌐 Respect privacy and data protection laws

This tool is intended for legitimate security research, penetration testing, and OSINT purposes only.

---

## 📝 Credits & Inspiration

This project stands on the shoulders of giants! 🦸

### Built Upon
[**CloakQuest3r**](https://github.com/spyboy-productions/CloakQuest3r) by [@spyboy-productions](https://github.com/spyboy-productions)

### VeilStrike Enhancements
- 🚀 Enhanced non-Cloudflare origin discovery algorithms
- 🎯 Improved resolution accuracy and reliability
- 🔧 Advanced technological fingerprinting capabilities
- ⚡ Optimized performance for batch operations
- 📊 Enhanced reporting and export formats

**Thank you to all contributors and the security community!** 🙏

---

## 📜 License

**GNU AFFERO GENERAL PUBLIC LICENSE Version 3**

This project is licensed under the AGPL-3.0 License - a strong copyleft license that ensures derivative works remain open source.

See the [LICENSE](LICENSE) file for complete details.

---

<div align="center">

### 🌟 Support & Feedback

If you find VeilStrike useful, please consider:
- ⭐ Giving it a star on GitHub
- 🐛 Reporting issues and bugs
- 💡 Suggesting improvements
- 🤝 Contributing to the project

**Questions?** Open an issue or reach out to the community!

---

**Made with ❤️ by the Security Research Community**

*Last Updated: February 2026*

</div>
