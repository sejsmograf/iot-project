import paho.mqtt.client as mqtt
import json
import sejsmo
import time
import threading

BROKER_HOST = "localhost"
ZONE_NAME = "sauna"
TOPIC_NAME = "auth/response"

client = mqtt.Client()

display_refresh_interval = 1
display_paused = False


def display_weather_data():
    while True:
        if not display_paused:
            print(f"Current time: {time.strftime('%H:%M:%S')}")
        time.sleep(display_refresh_interval)




def process_message(client, userdata, message):
    global display_paused

    message_decoded = json.loads(message.payload)
    print(f"RECEIVED AUTH: {message_decoded['authorized']}")

    # Tutaj logika w zalężoności czy autoryzacja udana czy nie,
    # jakieś buzzery etc
    if message_decoded["authorized"] == True:
        display_paused = True
        print("Success")
        time.sleep(5)
        display_paused = False
    else:
        display_paused = False
        print("Failure")


def connect_to_broker():
    client.connect(BROKER_HOST)
    client.on_message = process_message

    client.loop_start()
    client.subscribe(TOPIC_NAME)


def disconnect_from_broker():
    client.loop_stop()
    client.disconnect()


def run_receiver():
    connect_to_broker()
    try:
        display_weather_thread = threading.Thread(target = display_weather_data())
        display_weather_thread.start()
        while True:
            pass
    except KeyboardInterrupt:
        print("Ctrl+C received. Disconnecting from the broker and exiting.")
        disconnect_from_broker()

    disconnect_from_broker()


if __name__ == "__main__":
    print(f"starting clietn receiver in zone {ZONE_NAME}")
    run_receiver()
