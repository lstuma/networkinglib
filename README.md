# networkinglib
Python Networking Module

## How to use

### TCP Client
#### Connecting to server
```
from networkinglib import tcp
socket = tcp.connect('127.0.0.1', 7777)
if not socket: print("Could not connect!")
```

#### Sending packet
```
socket.send("Hello Server!")
```

#### Receiving Packets
```
print(socket.receive())
```

#### Closing connection
```
socket.close()
```
