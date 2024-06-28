import paho.mqtt

import time

import flask

app = Flask(__name__)

client_id = 'mqttx_4b4248fb'
username = ''
password = ''

def on_connect():
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    return client

def on_message():
    broker = 'broker.emqx.io'
    port = 1883
    topic = "topicName/iot"


@app.route('/')
def check_distance():
    on_connect()
    on_message

#https://wokwi.com/projects/401914531208297473