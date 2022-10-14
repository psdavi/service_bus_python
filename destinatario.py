from config_service_bus import ConfigServiceBus


class Destinatario:

    def __init__(self, queue_name):
        self.config = ConfigServiceBus()
        self.queue_name = queue_name
        self.recebido = self.config.get_client().get_queue_receiver(self.queue_name)

    def ler_mensagem(self):
        mensagem = self.recebido.receive_messages(max_message_count=1)
        return mensagem
