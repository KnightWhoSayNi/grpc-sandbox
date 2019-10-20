import grpc
import time

import echo_pb2
import echo_pb2_grpc

import utils

from concurrent import futures
from datetime import datetime


class Server(object):

    def __init__(self, port=5000):
        self.port = port

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        echo_pb2_grpc.add_EchoServicer_to_server(ServerServiceExample(), self.server)

    def start(self):
        self.server.add_insecure_port('[::]:{}'.format(self.port))
        self.server.start()
        print('Starting server. Listening on port {}'.format(self.port))

    def stop(self):
        self.server.stop(0)

    def run(self):
        try:
            while True:
                time.sleep(4)
                break
        except KeyboardInterrupt:
            self.stop()


class ServerServiceExample(echo_pb2_grpc.EchoServicer):

    def __init__(self):
        self.username = "Echo"

    def SendEcho(self, request, context):
        print("{} S <- C: [{}] {}".format(datetime.fromtimestamp(time.time()), request.username, request.content))
        response = echo_pb2.Data()
        response.username = self.username
        response.content = utils.UpperString(request.content)
        print("{} S -> C: [{}] {}".format(datetime.fromtimestamp(time.time()), response.username, response.content))
        return response


if __name__ == "__main__":
    server = Server()
    server.start()
    server.run()
