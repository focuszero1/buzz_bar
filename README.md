Buzz Bar - Minimal Audio Amplitude Visualizer

Overview:
Buzz Bar is a lightweight desktop visualizer designed to display real-time audio amplitude as animated bars. Built for use alongside DAWs like Ableton Live, it offers a clean, floating visual overlay with minimal system load.

Current Features:
- Captures live audio input using the system default device
- Computes frequency band magnitudes via FFT
- Displays a 16-band amplitude bar graph in real-time using Pygame
- Supports OSC input for bridge testing from external sources

Structure:
├── src/
│   ├── main.py                # Launches the visualizer
│   ├── audio_input.py         # Captures audio and computes frequency bands
│   ├── visualizer.py          # Renders visual bar graph
│   ├── test_raw_udp_capture.py  # Debug tool for inspecting raw UDP data
│   └── test_bridge_capture.py   # Listens for OSC messages on /buzzbar/amplitude

Requirements:
- Python 3.9+
- `sounddevice`
- `pygame`
- `numpy`
- `python-osc` (for test_bridge_capture.py)

Installation:
1. Clone the repo:
   git clone https://github.com/focuszero1/buzz_bar.git
2. Install dependencies:
   pip install -r requirements.txt
3. Run it:
   python src/main.py

Note:
OSC bridge testing tools are included for integration with Ableton + Max for Live.

Status:
Prototype v0.1 – Core audio-to-visual pipeline is working. Future phases may include peak hold, spectrum mode, and customization options.

Author:
Usher (FocusZero1) - https://www.linkedin.com/in/focuszero1

License:
MIT 
