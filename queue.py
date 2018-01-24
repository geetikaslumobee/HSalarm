from azure.storage.queue import QueueService
from azure.storage import CloudStorageAccount
import random

class Temperature():

    def run_temperature(account):
        queue_service = account.create_queue_service()
        
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
                queue_service.put_message(queue2, temp)
                

    def generateTemp():
        return random.randint(1,100)

