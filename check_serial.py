"""
Run this script in a separate terminal while the experiment is running.
It will print everything sent to and received from the serial port in real time.

Usage:
    python check_serial.py
"""

import time
import serial
import serial.tools.list_ports
import config as cfg


def list_available_ports():
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("No serial ports detected.")
    else:
        print("Available serial ports:")
        for port in ports:
            print(f"  {port.device:20s} — {port.description}")
    print()


def monitor(port_name):
    try:
        ser = serial.Serial(port_name, baudrate=128000, timeout=0)
        print(f"✓ Connected to '{port_name}' at {ser.baudrate} baud.")
        print("Monitoring — press Ctrl+C to stop.\n")

        buffer = b""
        try:
            while True:
                chunk = ser.read(256)
                if chunk:
                    buffer += chunk
                    while b"\n" in buffer:
                        line, buffer = buffer.split(b"\n", 1)
                        ts = time.strftime("%H:%M:%S")
                        print(f"[{ts}]  {line.decode('utf-8', errors='replace').strip()}")
                else:
                    time.sleep(0.005)

        except KeyboardInterrupt:
            print("\nStopped.")
        finally:
            ser.close()

    except serial.SerialException as e:
        print(f"✗ Could not open port '{port_name}': {e}")


if __name__ == "__main__":
    list_available_ports()

    if cfg.TRIGGER_PORT:
        print(f"Configured port: {cfg.TRIGGER_PORT}")
        monitor(cfg.TRIGGER_PORT)
    else:
        print("TRIGGER_PORT is set to None in config.py — update it first.")
