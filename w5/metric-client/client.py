import datetime
import socket


class Client:
    def __init__(self, addr, port, timeout=None):
        self.timeout = timeout
        self.addr = addr
        self.port = port
        try:
            self.sock = socket.create_connection((self.addr, self.port))
        except:
            pass

    def __del__(self):
        self.sock.close

    @staticmethod
    def parse_get(got_string):
        pass

    def put(self, key, value, timestamp):
        self.timestamp = timestamp or datetime.datetime.now().timestamp()
        try:
            self.sock.sendall(f"put {key} {value} {self.timestamp}\n")
            if self.sock.recv(1024) == "error\nwrong command\n\n":
                raise ClientError("put")
        except ClientError as err:
            return err.method

    def get(self, key):
        try:
            pass
        except ClientError as err:
            return err.method


class ClientError(Exception):
    def __init__(self, method):
        self.method = method
