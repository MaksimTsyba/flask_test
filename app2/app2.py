from flask import render_template, request, Flask
from threading import Thread
from flask_rabmq import RabbitMQ
# from producer import publish
import json
# import pika
import logging


# logging.basicConfig(format='%(asctime)s %(process)d,%(threadName)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     level=logging.INFO)
#
# logger = logging.getLogger(__name__)
app = Flask(__name__)
app.debug = True
app.config.setdefault('RABMQ_RABBITMQ_URL', 'amqp://admin:mypass@rabbitmq:5672')
app.config.setdefault('RABMQ_SEND_EXCHANGE_NAME', 'flask_rabmq')
app.config.setdefault('RABMQ_SEND_EXCHANGE_TYPE', 'topic')
app.config.setdefault('RABMQ_SEND_POOL_SIZE', 2)
app.config.setdefault('RABMQ_SEND_POOL_ACQUIRE_TIMEOUT', 5)
#
# ramq = RabbitMQ()
# ramq.init_app(app=app)
# parameters = pika.URLParameters('amqp://admin:mypass@rabbitmq:5672')



@app.route("/")
def hello_world():
    # publish()
    return "<p>Hello, World2!</p>"

# @app.route("/start")
# def start():
#     connection = pika.BlockingConnection(parameters)
#     channel = connection.channel()
#     channel.queue_declare(queue='test')
#     channel.basic_publish(exchange='test', routing_key='test',
#                           body=b'Test message.')
#
#     connection.close()
#     return "<p>Hello, World!</p>"
#
# @app.route("/receive")
# def receive():
#     data = []
#
#     connection = pika.BlockingConnection(parameters)
#     channel = connection.channel()
#     channel.queue_declare(queue='test')
#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     def my_callback(ch, method, properties, body):
#         data.append({'test': 'fkgedfgdjs'})
#         print(f" [x] Received, {body}")
#     channel.basic_consume("test", my_callback, auto_ack=True)
#     thread = Thread(target=channel.start_consuming)
#     thread.start()
#     return json.dumps(data)
#
#
# @app.route("/flask_test")
# def flask_test():
#     # send message
#     ramq.send({'message_id': 234234234567, 'a': 7}, routing_key='flask_rabmq.test', exchange_name='flask_rabmq')
#     # delay send message, expiration second(support float).
#     ramq.delay_send({'message_id': 333333, 'a': 7}, routing_key='flask_rabmq.test', exchange_name='flask_rabmq',
#                     delay=10)
#     return 'Hello World!'
#
#
# @ramq.queue(exchange_name='flask_rabmq', routing_key='flask_rabmq.test')
# def flask_rabmq_test2(body):
#     logger.info(body)
#     return True


if __name__ == '__main__':
    # ramq.run_consumer()
    app.run(host='0.0.0.0')
