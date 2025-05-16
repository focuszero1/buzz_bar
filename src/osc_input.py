# File: osc_input.py
import threading
from pythonosc import dispatcher, osc_server

# Shared global state
osc_bars = [0.0] * 16

def _update_bars(address, *args):
    smoothing = 0.2  # 0 = no smoothing, 1 = instant jump
    values = list(args)
    if len(values) == len(osc_bars):
        for i in range(len(osc_bars)):
            osc_bars[i] = (
                smoothing * values[i] + (1 - smoothing) * osc_bars[i]
            )

def start_osc_server(ip="127.0.0.1", port=7400):
    disp = dispatcher.Dispatcher()
    disp.map("/buzzbar/amplitude", _update_bars)

    server = osc_server.ThreadingOSCUDPServer((ip, port), disp)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

def get_osc_spectrum():
    print("OSC Bars:", osc_bars)  # Debug line
    return osc_bars

