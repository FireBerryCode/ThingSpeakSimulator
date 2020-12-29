import requests
import numpy as np
import time

channel_api_key = "IRXY6XB0IPLB1L7B"

payload = {
    "api_key": channel_api_key,
    "field1": 29.18293912,
    "field2": 3.45,
    "field3": 0.34,
    "field4": 0
}


def generate_data():
    temp = np.random.normal(29, 3, 1)[0]
    hum = np.random.normal(10, 2, 1)[0]
    meth = np.random.normal(0.5, 0.01, 1)[0]
    fire = np.random.binomial(1, 0.1)

    payload["field1"] = temp
    payload["field2"] = hum
    payload["field3"] = meth
    payload["field4"] = fire

    return payload


while 1:

    payload = generate_data()
    r = requests.post("https://api.thingspeak.com/update.json", json=payload)

    if r.status_code == 200:
        print("Mensaje enviado correctamente")
        print(payload)

    time.sleep(60)




