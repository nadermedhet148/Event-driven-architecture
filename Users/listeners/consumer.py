import pika


def consumer(callback, channel_name):


    credentials = pika.PlainCredentials('root', 'root')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq', credentials=credentials))
    channel = connection.channel()
        

    channel.exchange_declare(exchange=channel_name, exchange_type='topic')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange=channel_name, queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


