# registry_artifacts_extractor.py

import _winreg

def extract_registry_artifacts():
    # Define registry keys to extract artifacts from
    keys = [
        _winreg.HKEY_CURRENT_USER,
        _winreg.HKEY_LOCAL_MACHINE,
        # Add more keys as needed
    ]
    # List of registry paths to extract artifacts from
    paths = [
        "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
        # Add more paths as needed
    ]
    
    print("Extracting registry artifacts...")
    for key in keys:
        for path in paths:
            try:
                reg_key = _winreg.OpenKey(key, path, 0, _winreg.KEY_READ)
                print(f"Artifacts from {path}:")
                for i in range(_winreg.QueryInfoKey(reg_key)[1]):
                    try:
                        name, value, _ = _winreg.EnumValue(reg_key, i)
                        print(f"{name}: {value}")
                    except Exception as e:
                        print(f"Error: {e}")
                _winreg.CloseKey(reg_key)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    extract_registry_artifacts()
