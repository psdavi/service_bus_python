from azure.servicebus import ServiceBusClient


class ConfigServiceBus:

    def __init__(self):
        self.CONNECTION_STR = "Endpoint=sb://davi-space.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=jJhICZlINDgerlmJmgBFRIdoL6oyk0dbIaedMFPoB9M="
        self.client = ServiceBusClient.from_connection_string(self.CONNECTION_STR)
        self.queue_name = "daviqueue"



    def get_client(self):
        return self.client
