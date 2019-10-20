import grpc
import time
import os

import echo_pb2
import echo_pb2_grpc

from datetime import datetime


class ClientExample(object):

    def __init__(self, username, host='localhost', port=5000):
        self.username = username
        self.host = host
        self.port = port
        channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.stub = echo_pb2_grpc.EchoStub(channel)

    def send_message(self, message):
        request = echo_pb2.Data()
        request.username = self.username
        request.content = message
        print("{} S <- C: [{}] {}".format(datetime.fromtimestamp(time.time()), request.username, request.content))
        response = self.stub.SendEcho(request)
        print("{} S -> C: [{}] {}".format(datetime.fromtimestamp(time.time()), response.username, response.content))


if __name__ == "__main__":
    _username = os.getenv('USERNAME', 'Bob')
    _host = os.getenv('ECHOSRV_HOST', 'localhost')
    _port = os.getenv('ECHOSRV_PORT', 5000)
    client = ClientExample(username=_username, host=_host, port=_port)
    for i in range(5):
        client.send_message(message="Hello World {}".format(i))
        time.sleep(0.2)
