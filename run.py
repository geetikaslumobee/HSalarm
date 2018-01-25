import os
from azure.storage.queue import QueueService
# from azure.storage import CloudStorageAccount
import random
import tkMessageBox

# from azure.storage import CloudStorageAccount
# import azure.common
# from queue import Temperature
# read the queue message and write to stdout

# inputMessage = open(os.environ['inputMessage']).read()
# message = "Python script processed queue message '{0}'".format(inputMessage)
inputMessage = open(os.environ['inputMessage']).read()
message = "Python script processed queue message '{0}'".format(inputMessage)
print(message)

print('Function started')

print('Azure Storage Queue Temperature')

print('Azure Storage Queue temperature')

# Create queue
# queue_service = QueueService(account_name='myaccount', account_key='mykey')
# queue_service.create_queue('taskqueue')
account_name = ''
account_key = ''
def run_temperature():
    queue_service = QueueService(account_name, account_key)

    queue1 = "NormalTemp"
    queue2 = "HighTemp"
   

    queue_service.create_queue(queue1)
    print("Queue created successfully...")

    queue_service.create_queue(queue2)
    print("Queue created successfully...")

    for i in range(1, 10):
        temp = generateTemp()
        queue_service.put_message(queue1, temp)

        if(temp > 80):
            # Code for alert function will be plcaed here
            tkMessageBox.showinfo(message=temp"is the temperature")
            queue_service.put_message(queue2, temp)

def generateTemp():
    return random.randint(1, 100)

run_temperature()
