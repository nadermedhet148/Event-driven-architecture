import pika
import sys


def publish(channel_name, message):
    credentials = pika.PlainCredentials('root', 'root')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq', credentials=credentials))
        
    channel = connection.channel()

    channel.exchange_declare(exchange=channel_name, exchange_type='topic')
    try:
        channel.basic_publish(exchange=channel_name, routing_key='', body=message)
        connection.close()
    except Exception as ex:
        print(ex)
