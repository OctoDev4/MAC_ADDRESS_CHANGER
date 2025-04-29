# MAC Address Changer

This is a simple Python script that allows you to change the MAC address of a given network interface using system commands. It's useful for privacy, testing, or bypassing MAC-based filters.

## 📦 Features

- Change the MAC address of a specified interface.
- Verify whether the MAC address was changed successfully.
- Simple command-line interface with helpful error messages.

## ⚠️ Requirements

- Linux-based system (uses `ifconfig`)
- Python 3
- Root privileges

## 🚀 Usage

```bash
sudo python3 mac_changer.py -i <interface> -m <new_mac_address>
