# bluetooth_device_tracker.py

import bluetooth

def track_bluetooth_devices():
    print("Tracking nearby Bluetooth devices...")
    try:
        nearby_devices = bluetooth.discover_devices(duration=10, lookup_names=True, device_id=-1)
        if nearby_devices:
            print("Nearby Bluetooth devices:")
            for addr, name in nearby_devices:
                print(f"Name: {name}, Address: {addr}")
        else:
            print("No Bluetooth devices found nearby")
    except Exception as e:
        print(f"Error tracking Bluetooth devices: {e}")

if __name__ == "__main__":
    track_bluetooth_devices()
