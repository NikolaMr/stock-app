import json
import time

import pika
import os


def _callback(ch, method, properties, body):
    # Do something useful with your incoming message body here, e.g.
    # saving it to a database
    print("Received event {}".format(json.loads(body)))


if __name__ == "__main__":

    while True:
        try:
            # RabbitMQ credentials with username and password
            username = os.environ.get('RABBITMQ_USERNAME')
            password = os.environ.get('RABBITMQ_PASSWORD')
            credentials = pika.PlainCredentials(username, password)
            mq_url = os.environ.get('RABBITMQ_HOST')
            queue = os.environ.get('RABBITMQ_QUEUE')

            print('Initializing connection.')
            # Pika connection to the RabbitMQ host - typically 'rabbit' in a
            # docker environment, or 'localhost' in a local environment

            connection = pika.BlockingConnection(
                pika.ConnectionParameters(mq_url, credentials=credentials)
            )
            print('After initializing connection.')

            # start consumption of channel
            channel = connection.channel()
            print('After channel.')
            channel.basic_consume(queue=queue, on_message_callback=_callback, auto_ack=True)
            print('After basic_consume.')
            channel.start_consuming()
            print('Started consuming.')
        except Exception as e:
            print('Exception encountered')
            print(str(e))
            print('Going to sleep, will retry in 60 seconds.')
            time.sleep(60)
