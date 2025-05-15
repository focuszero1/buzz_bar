# File: buzz_bar/src/test_bridge_capture.py

import sys
import argparse
from pythonosc import dispatcher
from pythonosc import osc_server

def audio_callback(address, *args):
    print(f"Received from {address}: {args}")

def main(ip="127.0.0.1", port=8000):
    print(f"Listening for OSC messages on {ip}:{port}...")
    
    disp = dispatcher.Dispatcher()
    disp.map("/buzzbar/amplitude", audio_callback)

    server = osc_server.BlockingOSCUDPServer((ip, port), disp)
    print("Server started. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test script for BuzzBarBridge OSC output.")
    parser.add_argument("--ip", type=str, default="127.0.0.1", help="The IP to listen on.")
    parser.add_argument("--port", type=int, default=8000, help="The port to listen on.")
    args = parser.parse_args()

    main(ip=args.ip, port=args.port)
 