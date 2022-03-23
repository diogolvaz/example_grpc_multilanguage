# gRPC example client

This is a Hello World example of a gRPC client application.

The client depends on the contract module, where the protocol buffers shared between server and client are defined.
The client needs to know the interface to make remote calls.


## Instructions

To install de grpc packages
```
 # windows
 > python -m venv .venv
 > venv\Scripts\activate

 # linux
 $ python -m pip install virtualenv 
 $ virtualenv .venv
 $ source .venv/bin/activate

 python -m pip install grpcio
 python -m pip install grpcio-tools

 deactivate
```


To compile and run the client:

```
python -m grpc_tools.protoc -I..\contract\src\main\proto --python_out=. --grpc_python_out=. ..\contract\src\main\proto\HelloWorld.proto
python client.py
```

----

[SD Faculty](mailto:leic-sod@disciplinas.tecnico.ulisboa.pt)
