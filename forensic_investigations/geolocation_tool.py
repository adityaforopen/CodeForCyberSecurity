# geolocation_tool.py

import requests

def geolocate_ip(ip_address):
    api_url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(api_url)
        data = response.json()
        if data["status"] == "success":
            print(f"IP Address: {ip_address}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
        else:
            print("Failed to geolocate IP address")
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip_address = input("Enter IP address to geolocate: ")
    geolocate_ip(ip_address)
