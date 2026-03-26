# OBS Sync Pro 🎛️

*Heads up: Most of this code was made with AI. I just wanted to make this tool to control OBS, so this isn't like a performance showcase*

A lightweight, privacy-first web remote for OBS Studio, optimized for touch devices. It uses a local Python server to sync your soundboard and settings across your home network without relying on third-party cloud databases.

## The Files (How it works)
* **`index.html`** - The "Face." This is the actual website with all the buttons and layout that you see on the tablet.
* **`server.py`** - The "Brain." A tiny local server you run on your main PC that lets the tablet save your settings and soundboard list.
* **`obs-websocket.js`** - The "Translator." A standard library that lets the website actually send commands directly to OBS.
* **`settings.json`** - The "Memory." This gets generated automatically and stores your OBS password and network IP. *(Keep this private!)*
* **`.gitignore`** - The "Shield." Makes sure `settings.json` never gets uploaded to GitHub so you don't leak your passwords.

## Setup & Usage

1. **Enable OBS WebSockets:**
   * Open OBS Studio -> `Tools` -> `WebSocket Server Settings`.
   * Check "Enable WebSocket server" and note the Port (default: 4455) and Server Password.

2. **Start the Local Server:**
   * Open a terminal in this directory.
   * Run the server:
     ```bash
     python3 server.py
     ```

3. **Connect your Tablet/Phone:**
   * Find your computer's local IP address (e.g., `192.168.1.x`).
   * Open a browser on your device and navigate to `http://YOUR_IP:8000`.
   * Enter your IP, Port, and WebSocket Password, then hit Connect!
