
import pika
import json
import os


params = pika.URLParameters(os.environ.get("AMQP_URL"))

# connect to a broker machine on CloudAMQP console
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="",
        routing_key="main",
        properties=properties,
        body=json.dumps(body)
    )
