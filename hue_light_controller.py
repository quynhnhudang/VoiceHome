import requests

BRIDGE_IP = '192.168.1.2'  # Replace with actual Bridge IP
USER_TOKEN = '1028d66426293e821ecfd9ef1a0731df'  # Replace with actual User Token

def send_light_command(light_id, data):
    """Generalized function for sending commands to a specific light."""
    url = f'http://{BRIDGE_IP}/api/{USER_TOKEN}/lights/{light_id}/state'
    response = requests.put(url, json=data)
    print(f"Response from Hue for light {light_id}: {response.json()}")

def set_brightness(light_id, brightness):
    """Set the brightness of the light."""
    send_light_command(light_id, {"bri": brightness})

def set_color_temp(light_id, color_temp):
    """Set the color temperature of the light."""
    send_light_command(light_id, {"ct": color_temp})

def get_light_status(light_id):
    """Retrieve the current status and settings of a light."""
    url = f'http://{BRIDGE_IP}/api/{USER_TOKEN}/lights/{light_id}'
    response = requests.get(url)
    print(f"Status for light {light_id}: {response.json()}")
