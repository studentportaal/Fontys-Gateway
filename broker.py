from google.cloud import pubsub_v1

subscription_name = 'generic-fontys'
topic_name = 'fontys-generic'

project_id = 'pts6-bijbaan'

subscriber = pubsub_v1.SubscriberClient()
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)
subscription_path = subscriber.subscription_path(
    project_id, subscription_name
)


def callback(message):
    print('Received message {}'.format(message))
    message.ack()


def connect():
    subscriber.subscribe(subscription_path, callback=callback)
    print('Listening for messages on {}'.format(subscription_path))


def send_message():
    data = 'test message from fontys to generic'
    data = data.encode('utf-8')
    future = publisher.publish(topic_path, data=data, user='known')
    print('Published {} of message ID {}'.format(data.decode('UTF-8'), future.result()))
