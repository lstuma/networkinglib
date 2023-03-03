import tcp_client

class tcp:
    def __init__(self, address, port):
        # tcp_client can't work with localhost
        if address == 'localhost': address = '127.0.0.1'

        self.socket = tcp_client.connect(address, port)

    def receive(self):
        # receive next message and return it
        return tcp_client.receive(self.socket)

    def send(self, message):
        # send message
        return tcp_client.send(message, self.socket)

    def close(self):
        # close socket
        return tcp_client.close(self.socket)



    @classmethod
    def connect(address, port):
        return tcp(address, port)