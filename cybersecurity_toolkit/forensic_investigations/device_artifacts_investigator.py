# device_artifacts_investigator.py

import os

def investigate_device_artifacts(device_path):
    print(f"Investigating artifacts on {device_path}...")
    try:
        # Example: Search for application-specific artifacts
        # Replace with actual artifact investigation code
        for root, dirs, files in os.walk(device_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Example: Look for configuration files, logs, etc.
                if file.endswith(".conf") or file.endswith(".log"):
                    print("Found artifact:", file_path)
        if not os.listdir(device_path):
            print("No artifacts found on the device")
    except Exception as e:
        print(f"Error investigating artifacts: {e}")

if __name__ == "__main__":
    device_path = input("Enter path to the device to investigate artifacts: ")
    if os.path.exists(device_path):
        investigate_device_artifacts(device_path)
    else:
        print("Device path does not exist:", device_path)
