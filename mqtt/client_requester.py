import paho.mqtt.client as mqtt
import json
import time

BROKER_HOST = "localhost"
ZONE_NAME = "sauna"
TOPIC_NAME = "auth/request"

client = mqtt.Client()

def publish_data(topic_name, json_data):
    client.publish(topic_name, json_data)


def publish_mock_data(topic_name):
    json_data = json.dumps({
        "cardId" : 10000000 
    })

    publish_data(topic_name, json_data)
    time.sleep(10)


def connect_to_broker():
    client.connect(BROKER_HOST)

def disconnect_from_broker():
    client.disconnect()

def run_sender():
    connect_to_broker()
    try:
        while True:
            
            publish_mock_data(TOPIC_NAME)
    except KeyboardInterrupt:
        print("Ctrl+C received. Disconnecting from the broker and exiting.")
        disconnect_from_broker()


    disconnect_from_broker()


if __name__ == "__main__":
    print(f"Starting client auth requester in zone {ZONE_NAME}")
    run_sender()
