import asyncio
from time import sleep

metric={}
host = "127.0.0.1"
port = 8181

class ClientServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.err_msg = "error\nwrong command\n\n"
        self.ok_msg = "ok\n\n"
        # self.metric = {}

    def connection_made(self, transport):
        self.transport = transport

    def process_data(self, data):
        # self.transport.pause_reading()
        # sleep(1)
        # self.transport.resume_reading()
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
                if key not in metric:
                    metric[key] = []
                if (timestamp, value) not in metric[key]:
                    metric[key].append((timestamp, value))
                print(metric)
            if client_cmd == "get":
                if key == "*":
                    return metric
                elif key in metric:
                    return {
                        key: metric[key]
                    }
            return self.ok_msg

    def data_received(self, data):
        print(data.decode())
        resp = self.process_data(data.decode())
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


# def run_server(host, port):
loop = asyncio.get_event_loop()
coro = loop.create_server(
    ClientServerProtocol,
    host, port
)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    exit()

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
