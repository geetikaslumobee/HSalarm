from azure.storage import CloudStorageAccount
import azure.common
from queue import Temperature

print('Azure Storage Queue Temperature')

account_name = config.STORAGE_ACCOUNT_NAME
account_key = config.STORAGE_ACCOUNT_KEY
account = CloudStorageAccount(account_name, account_key)

print('Azure Storage Queue temperature')
queueTemp = Temperature()
queueTemp.run_temperature(account)
