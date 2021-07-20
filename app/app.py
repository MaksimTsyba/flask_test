from flask import render_template, request
from models import db, User, Request
from init import create_app
from threading import Thread
from flask_rabmq import RabbitMQ
import json
import pika
import logging

# logging.basicConfig(format='%(asctime)s %(process)d,%(threadName)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     level=logging.INFO)
#
# logger = logging.getLogger(__name__)
app = create_app()
app.debug = True
app.config.setdefault('RABMQ_RABBITMQ_URL', 'amqp://admin:mypass@rabbitmq:5672')
app.config.setdefault('RABMQ_SEND_EXCHANGE_NAME', 'flask_rabmq')
app.config.setdefault('RABMQ_SEND_EXCHANGE_TYPE', 'topic')
app.config.setdefault('RABMQ_SEND_POOL_SIZE', 2)
app.config.setdefault('RABMQ_SEND_POOL_ACQUIRE_TIMEOUT', 5)

ramq = RabbitMQ()
ramq.init_app(app=app)
parameters = pika.URLParameters('amqp://admin:mypass@rabbitmq:5672')

@app.route("/")
def hello_world():
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='test')
    channel.basic_publish(exchange='test', routing_key='test',
                          body=b'Test message.')

    connection.close()
    return "<p>Hello, World!</p>"

@app.route("/receive")
def receive():
    data = []

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='test')
    print(' [*] Waiting for messages. To exit press CTRL+C')
    def my_callback(ch, method, properties, body):
        data.append({'test': 'fkgedfgdjs'})
        print(f" [x] Received, {body}")
    channel.basic_consume("test", my_callback, auto_ack=True)
    thread = Thread(target=channel.start_consuming)
    thread.start()
    return json.dumps(data)


@app.route("/flask_test")
def flask_test():
    # send message
    ramq.send({'message_id': 234234234567, 'a': 7}, routing_key='flask_rabmq.test', exchange_name='flask_rabmq')
    # delay send message, expiration second(support float).
    ramq.delay_send({'message_id': 333333, 'a': 7}, routing_key='flask_rabmq.test', exchange_name='flask_rabmq',
                    delay=10)
    return 'Hello World!'


# @ramq.queue(exchange_name='flask_rabmq', routing_key='flask_rabmq.test')
# def flask_rabmq_test2(body):
#     logger.info(body)
#     return True

@app.route("/test")
@app.route("/test/<name>/")
def hello_world23(name=None):
    return render_template('index.html', name=name.capitalize())


@app.route("/get_cars", methods=['GET'])
def get_cars():
    # cars = Car.query.filter(Car.price > 11000).all()
    all_cars = list()
    # for item in cars:
    #     all_cars.append({"name": item.name, "price": item.price})
    return json.dumps(all_cars)

@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return json.dumps("Added"), 200


@app.route("/add_request", methods=['POST'])
def add_request():
    data = request.get_json()
    new_request = Request(**data)
    db.session.add(new_request)
    db.session.commit()
    return json.dumps("Added"), 200

@app.route("/get_request", methods=['GET'])
def get_request():
    data = Request.query.all()
    items = list()
    for item in data:
        items.append({'name': item.name, 'user_name': item.user.name})
    return json.dumps(items), 200


# @app.route("/add_user", methods=['GET', 'POST'])
# def add_user():
#     name = None
#     if request.method == 'POST':
#         name = request.form.get('name')
#     if request.method == 'GET':
#         name = request.args.get('name')
#     if name:
#         name.capitalize()
#     return f"Hello, {name}"

if __name__ == '__main__':
    # ramq.run_consumer()
    app.run(host='0.0.0.0')
