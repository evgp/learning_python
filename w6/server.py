import asyncio


class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.err_msg = "error\nwrong command\n\n"
        self.ok_msg = "ok\n\n"
        self.metric = {}

    def connection_made(self, transport):
        self.transport = transport

    def process_data(self, data):
        commands = ("get", "put")
        try:
            if len(data.split()) > 2:
                client_cmd, key, value, timestamp = data.split()
            elif len(data.split()) > 4:
                raise Exception
            else:
                client_cmd, key = data.split()
        except:
            return self.err_msg        
        if client_cmd not in commands:
            return self.err_msg
        else:
            if client_cmd == "put":
                if key not in self.metric:
                    self.metric[key] = []
                self.metric[key].append((timestamp, value))
                print(self.metric)
            if client_cmd == "get":
                if key == "*":
                    return self.metric
                else:
                    return self.metric[key]
            return self.ok_msg

    def data_received(self, data):
        print(data.decode())
        resp = self.process_data(data.decode())
        # print(resp)
        if isinstance(resp, dict):
            self.transport.write("ok\n".encode())
            for keyr in resp:
                for _ in resp[keyr]:
                    timestamp, value = _
                    self.transport.write(
                       f"{keyr} {value} {timestamp}\n".encode() 
                    )
            self.transport.write(b'\n')
        else:
            self.transport.write(resp.encode())


loop = asyncio.get_event_loop()
coro = loop.create_server(
    ClientServerProtocol,
    '127.0.0.1', 8181
)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
