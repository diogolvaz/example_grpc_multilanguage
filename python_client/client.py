import grpc
import HelloWorld_pb2 as pb2
import HelloWorld_pb2_grpc as pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = pb2_grpc.HelloWorldServiceStub(channel)
        response = stub.greeting(pb2.HelloRequest(name='friend'))
    print("Greeter client received: " + response.greeting)


if __name__ == '__main__':
    run()
