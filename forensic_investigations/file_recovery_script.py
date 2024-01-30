# file_recovery_script.py

import os

def recover_deleted_files(drive):
    print(f"Scanning drive {drive} for deleted files...")
    try:
        # Use any method or library for file recovery (e.g., forensic tools)
        # Example: Recursively scan the drive for deleted files
        recovered_files = []
        for root, dirs, files in os.walk(drive):
            for file in files:
                file_path = os.path.join(root, file)
                if not os.path.exists(file_path):
                    recovered_files.append(file_path)
        if recovered_files:
            print("Recovered files:")
            for file in recovered_files:
                print(file)
        else:
            print("No deleted files found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    drive = input("Enter drive to scan for deleted files (e.g., C:/): ")
    recover_deleted_files(drive)
