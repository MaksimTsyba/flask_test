import pika

params = pika.URLParameters('amqp://admin:mypass@rabbitmq:5672')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)

print('Starting consuming')
channel.start_consuming()
channel.close()