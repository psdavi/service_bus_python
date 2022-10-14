from remetente import Remetente
from datetime import datetime

if __name__ == '__main__':
    remetente = Remetente()

    status = remetente.enviar_mensagem({'data': datetime.now()})
    print(status)
