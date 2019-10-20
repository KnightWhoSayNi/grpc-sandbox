import grpc
import time

import chat_pb2
import chat_pb2_grpc

import utils

from concurrent import futures
from datetime import datetime


class ServerServiceExample(chat_pb2_grpc.ChatServicer):

    def __init__(self):
        self.username = "Echo"

    def SendData(self, request, context):
        print("{} S <- C: [{}] {}".format(datetime.fromtimestamp(time.time()), request.username, request.content))
        response = chat_pb2.Data()
        response.username = self.username
        response.content = utils.UpperString(request.content)
        print("{} S -> C: [{}] {}".format(datetime.fromtimestamp(time.time()), response.username, response.content))
        return response


if __name__ == "__main__":

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    port = 5000
    chat_pb2_grpc.add_ChatServicer_to_server(ServerServiceExample(), server)
    print('Starting server. Listening on port {}'.format(port))
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()

    try:
        while True:
            time.sleep(5)
            break
    except KeyboardInterrupt:
        server.stop(0)
