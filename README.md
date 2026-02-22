# VeilStrike

![GitHub](https://img.shields.io/github/license/xdrew87/VeilStrike?style=flat-square)
![Python](https://img.shields.io/badge/python-3.7+-blue?style=flat-square)

**VeilStrike** is a CDN exposure & origin intelligence scanner designed to discover origin IPs of websites **NOT protected by Cloudflare**. Perfect for OSINT investigations and security research on unprotected targets.

## 🎯 Features

- ✅ Discover origin IPs of sites NOT behind Cloudflare
- ✅ Identify unprotected web servers
- ✅ Resolve IPv4 & IPv6 addresses
- ✅ Identify web server headers and fingerprints
- ✅ JSON output support for automation
- ✅ Fast and lightweight design
- ✅ Designed for OSINT workflows

## Installation

```bash
git clone https://github.com/xdrew87/VeilStrike.git
cd VeilStrike
pip install -r requirements.txt
```

## Configuration

Configure your API key in `config.ini`:

```ini
[API_KEYS]
SECURITYTRAILS_API_KEY = YOUR_KEY_HERE
```

## Usage

### Basic Usage
```bash
python veilstrike.py example.com
```

### JSON Output
```bash
python veilstrike.py example.com --json
```

### Batch Scanning
```bash
python veilstrike.py sites.txt --json
```

## Contributing

Feel free to submit issues and enhancement requests!

## ⚖️ Disclaimer

This tool is for authorized security testing and OSINT research only. Unauthorized access to computer systems is illegal.

## 📝 Credits

This project was inspired by and based on the excellent work from [CloakQuest3r](https://github.com/spyboy-productions/CloakQuest3r) by [spyboy-productions](https://github.com/spyboy-productions). VeilStrike extends this concept with additional features and optimizations for non-Cloudflare origin discovery.

## License

MIT License - See LICENSE file for details