import grpc
import time
import os

import chat_pb2
import chat_pb2_grpc

from datetime import datetime


class ClientExample:

    def __init__(self, username, host='localhost', port=5001):
        self.username = username
        self.host = host
        self.port = port
        channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.stub = chat_pb2_grpc.ChatStub(channel)

    def send_message(self, message):
        request = chat_pb2.Data()
        request.username = self.username
        request.content = message
        print("{} S <- C: [{}] {}".format(datetime.fromtimestamp(time.time()), request.username, request.content))
        response = self.stub.SendData(request)
        print("{} S -> C: [{}] {}".format(datetime.fromtimestamp(time.time()), response.username, response.content))


if __name__ == "__main__":
    _username = os.getenv('USERNAME', 'Bob')
    _host = os.getenv('ECHOSRV_HOST', 'localhost')
    _port = os.getenv('ECHOSRV_PORT', 5001)
    client = ClientExample(username=_username, host=_host, port=_port)
    for i in range(5):
        client.send_message(message="Hello World {}".format(i))
        time.sleep(0.2)
