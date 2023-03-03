# networkinglib
Python Networking Module

## How to use

### TCP Client
#### Connecting to server
```Python
from networkinglib import tcp
socket = tcp.connect('127.0.0.1', 7777)
if not socket: print("Could not connect!")
```

#### Sending packet
```Python
socket.send("Hello Server!")
```

#### Receiving Packets
```Python
print(socket.receive())
```

#### Closing connection
```Python
socket.close()
```
