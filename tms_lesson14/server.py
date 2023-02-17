import os
import socket
import json


class Server:
    """
    Class represents server
    """
    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(('localhost', 8080))
        self.sock.listen(1)
    
    
    def run(self):
        """
        Main method that represents server performance
        """
        self.conn, self.address = self.sock.accept()
        try:
            while True:
                try:
                    data = self.conn.recv(1024).decode()
                    if not data:
                        break
                    data_dict = json.loads(data)
                    self.process_operation(data_dict)
                except Exception as e:
                    response = str(e)
                    self.conn.send(response.encode())
                    continue
                self.conn.send('Ok'.encode())
        finally:
            self.conn.close()



server = Server()
server.run()