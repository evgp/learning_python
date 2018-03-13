import datetime
import socket


class Client:
    def __init__(self, addr, port, timeout=None):
        self.timeout = timeout
        self.addr = addr
        self.port = port
        try:
            self.sock = socket.create_connection((self.addr, self.port), self.timeout)
        except:
            raise ClientError()

    def __del__(self):
        self.sock.close

    def put(self, key, value, timestamp=datetime.datetime.now().timestamp()):
        self.timestamp = timestamp  # or datetime.datetime.now().timestamp()
        try:
            data_send = f"put {key} {value} {self.timestamp}\n"
            self.sock.sendall(data_send.encode("utf-8"))
            # if self.sock.recv(1024) == "error\nwrong command\n\n":
            #     raise ClientError()
        except:
            raise ClientError

    def get(self, key):
        try:
            data_send = f"get {key}\n"
            self.sock.sendall(data_send.encode("utf-8"))
            result = {}
            srv_answer = self.sock.recv(1024).decode("utf-8").splitlines()
            if (srv_answer[0] != "ok"):
                raise ClientError()
            for answ in srv_answer:
                answ = answ.split()
                if len(answ) > 2:
                    result.setdefault(answ[0], [])
                    result[answ[0]].append((int(answ[2]), float(answ[1])))              
            return result
        except:
            raise ClientError()


class ClientError(Exception):
    pass
