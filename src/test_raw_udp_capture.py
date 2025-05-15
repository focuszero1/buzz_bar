# File: buzz_bar/src/test_raw_udp_capture.py

import socket
import struct

def extract_float(data):
    try:
        if b'float' in data:
            index = data.find(b'float') + len(b'float')
            # Loop over possible float positions
            for offset in range(index, len(data) - 3):
                float_bytes = data[offset:offset+4]
                value = struct.unpack('f', float_bytes)[0]
                # If value is in a reasonable audio range
                if 0.0 <= value <= 2.0:
                    return value
        return None
    except Exception as e:
        print(f"Error extracting float: {e}")
        return None

def main(ip="127.0.0.1", port=7400):
    print(f"Listening for raw UDP packets on {ip}:{port}...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            float_value = extract_float(data)
            if float_value is not None:
                print(f"Received float value from {addr}: {float_value:.5f}")
            else:
                print(f"Received unrecognized data from {addr}: {data}")
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()
