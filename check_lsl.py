"""
Run this script in a separate terminal while the experiment is running.
It will print every marker as it arrives from the LSL stream.

Usage:
    python check_lsl.py
"""

from pylsl import StreamInlet, resolve_streams

print("Searching for LSL marker stream...")
streams = resolve_streams()

if not streams:
    print("No stream found. Make sure the experiment is running.")
else:
    inlet = StreamInlet(streams[0])
    info = inlet.info()
    print(f"Connected to stream: '{info.name()}' | type: {info.type()} | source: {info.source_id()}")
    print("Listening for markers — press Ctrl+C to stop.\n")

    try:
        while True:
            sample, timestamp = inlet.pull_sample()
            print(f"[{timestamp:.3f}]  {sample[0]}")
    except KeyboardInterrupt:
        print("\nStopped.")
