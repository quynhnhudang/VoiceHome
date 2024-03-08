import requests

BRIDGE_IP = '192.168.1.2'
USER_TOKEN = '1028d66426293e821ecfd9ef1a0731df'

def control_light(light_id, state=None, brightness=None, color=None, color_temp=None):
    url = f'http://{BRIDGE_IP}/api/{USER_TOKEN}/lights/{light_id}/state'
    command = {"on": state} if state is not None else {}
    if brightness: command["bri"] = brightness
    if color: command["hue"] = color
    if color_temp: command["ct"] = color_temp
    response = requests.put(url, json=command)
    print(f"Response from Hue for Light {light_id}: {response.json()}")

# Will add more functions as needed, such as set_temperature(), change_light_color(), etc.

