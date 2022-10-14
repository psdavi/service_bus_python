from azure.servicebus import ServiceBusMessage
from config_service_bus import ConfigServiceBus


class Remetente:

    def __init__(self, queue_name):
        self.config = ConfigServiceBus()
        self.queue_name = queue_name
        self.remetente = self.config.get_client().get_queue_sender(self.queue_name)

    def enviar_mensagem(self, conteudo):
        try:
            mensagem = ServiceBusMessage(str(conteudo))
            self.remetente.send_messages(mensagem)
            return True
        except Exception as ex:
            print(ex)
            return False
