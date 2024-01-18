#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import tkinter
import sqlite3
import time
import json


BROKER_HOST = "localhost"
TOPIC_LISTENER_NAME = "auth/request"
TOPIC_PUBLISER_NAME = "auth/response"
client = mqtt.Client()


def process_message(client, userdata, message):
    # W tej wiadomości powinno być card id
    message_decoded = json.loads(message.payload)
    print(f"received request to authorize: {message_decoded}")

    # tutaj logika do sprawdznia po stronie serwera czy karta jest autoryzowana
    authorized = True

    # Spakowanie odpowiedzi do JSON
    json_data = json.dumps({
        "authorized": authorized
    })

    # Odesłanie odpowiedzi na auth/response
    client.publish(TOPIC_PUBLISER_NAME, json_data)


def connect_to_broker():
    client.connect(BROKER_HOST)
    client.on_message = process_message

    client.loop_start()
    client.subscribe(TOPIC_LISTENER_NAME)


def disconnect_from_broker():
    # Disconnet the client.
    client.loop_stop()
    client.disconnect()


def run_receiver():
    connect_to_broker()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Ctrl+C received. Disconnecting from the broker and exiting.")
        disconnect_from_broker()

    disconnect_from_broker()


if __name__ == "__main__":
    run_receiver()
