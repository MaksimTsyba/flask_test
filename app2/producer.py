import pika

params = pika.URLParameters('amqp://admin:mypass@rabbitmq:5672')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body=b'hello1234')