
import pika
import os


params = pika.URLParameters(os.environ.get("AMQP_URL"))
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)


channel.basic_consume(queue="admin", on_message_callback=callback)

print("Started Consuming")
channel.start_consuming()
channel.close()
