
import pika
import os


params = pika.URLParameters(os.environ.get("AMQP_URL"))

# connect to a broker machine on CloudAMQP console
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish():
    channel.basic_publish(
        exchange="",
        routing_key="main",
        body="hello dude"
    )
