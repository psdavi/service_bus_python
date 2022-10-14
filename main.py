from destinatario import Destinatario


if __name__ == '__main__':
    destinatario = Destinatario("daviqueue")
    mensagem = destinatario.ler_mensagem()
    print(mensagem)
