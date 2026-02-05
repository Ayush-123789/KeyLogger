# Diagnostics Service (sanitized)

This repository has been sanitized to remove any privacy-invasive features (browser password/cookie extraction, remote webhook exfiltration, automatic persistence, auto-update, stealth screenshots/audio capture without consent).

## Behavior
- The app now requires explicit user consent before any diagnostics (audio, screenshots, keystroke logging) are recorded or stored locally.
- All network exfiltration is disabled; data is stored locally under `diagnostics/` only if the user consents.
- Persistence (adding to startup) is disabled unless the user explicitly consents and the app is running as an EXE.

## How to run (development)
1. Create a virtual environment and install requirements:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the app (console prompt will ask for consent):

```powershell
python keylogger.py
```

3. When prompted, answer `y` to enable diagnostics (or use the GUI prompt if available).

## How to build a single EXE (PyInstaller)
```powershell
pip install pyinstaller
pyinstaller --clean --noconfirm keylogger.spec
```
This produces an EXE named `dist\stark connect.exe`. Test the EXE on a safe, isolated machine before distribution.

## Notes
- This repo has been sanitized for ethical use and educational purposes. Do not use this code to invade users' privacy or bypass security.
- If you want to add legitimate telemetry, always get explicit, documented consent from users and provide clear controls to view and delete collected data.