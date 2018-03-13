import datetime
import socket


class Client:
    def __init__(self, addr, port, timeout=None):
        self.timeout = timeout
        self.addr = addr
        self.port = port
        try:
            self.sock = socket.create_connection((self.addr, self.port))
        except OSError as err:
            raise ClientError("create_connection: can't establish connection")

    def __del__(self):
        self.sock.close

    @staticmethod
    def parse_get(got_string):
        result = {}
        srv_answer = got_string.decode("utf-8").splitlines()
        if (srv_answer[0] != "ok"):
            raise ClientError("Error getting data from server")
        for answ in srv_answer:
            answ = answ.split()
            if len(answ) > 2:
                result.setdefault(answ[0], [])
                result[answ[0]].append((int(answ[2]), float(answ[1])))              
        return result

    def put(self, key, value, timestamp=datetime.datetime.now().timestamp()):
        self.timestamp = timestamp  # or datetime.datetime.now().timestamp()
        try:
            data_send = f"put {key} {value} {self.timestamp}\n"
            self.sock.sendall(data_send.encode("utf-8"))
            if self.sock.recv(1024) == "error\nwrong command\n\n":
                raise ClientError("put")
        except ClientError as err:
            return err.method

    def get(self, key):
        try:
            data_send = f"get {key}\n"
            self.sock.sendall(data_send.encode("utf-8"))
            a = self.sock.recv(1024).decode("utf-8").splitlines()
            if a[0] != "ok":
                raise ClientError
            return self.parse_get(self.sock.recv(1024))
        except ClientError as err:
            return err.method


class ClientError(Exception):
    def __init__(self, *args):
        self.method = ""
