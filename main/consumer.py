import pika
import json
import os

from models import Product
from app import main, db

params = pika.URLParameters(os.environ.get("AMQP_URL"))
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="main")

# This is so we can perform database operation outside an application context.
main.app_context().push()


def callback(ch, method, properties, body):
    print("Received in main")
    data = json.loads(body)
    print(data)
    if properties.content_type == "product_created":
        product = Product(id=data["id"], title=data["title"], image=data["image"])
        db.session.add(product)
        db.session.commit()
        print("Product created")

    elif properties.content_type == "product_updated":
        # column = Product.__table__.columns
        product = Product.query.filter(Product.id == data["id"]).update(
            {k: data[k] for k in data if (k != "id" and hasattr(Product, k))}
        )
        db.session.commit()
        print("Product updated")

    elif properties.content_type == "product_deleted":
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print("Product deleted")


channel.basic_consume(queue="main", auto_ack=True, on_message_callback=callback)

print("Started Consuming")
channel.start_consuming()

channel.close()
