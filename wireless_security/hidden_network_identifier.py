# hidden_network_identifier.py

import subprocess

def identify_hidden_networks():
    print("Identifying hidden wireless networks...")
    try:
        # Use subprocess to execute a command to scan for hidden networks
        result = subprocess.run(["netsh", "wlan", "show", "network", "mode=Bssid"], capture_output=True, text=True)
        output_lines = result.stdout.splitlines()
        hidden_networks = [line.split(":")[1].strip() for line in output_lines if "SSID" in line]
        if hidden_networks:
            print("Hidden networks found:")
            for network in hidden_networks:
                print(network)
        else:
            print("No hidden networks found")
    except Exception as e:
        print(f"Error identifying hidden networks: {e}")

if __name__ == "__main__":
    identify_hidden_networks()
