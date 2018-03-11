import os
import socket
import threading
import multiprocess


def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))


def worker(sock):
    while True:
        conn, addr = sock.accept()  # system call to accept conn. 
        print("pid", os.getpid())  # Every conn will be distributed by os
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()

with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()

    workers_count = 3
    workers_list = [multiprocess.Process(target=worker, args=(sock,))
                    for _ in range(workers_count)]

    for w in workers_list:
        w.start()

    for w in workers_list:
        w.join()  # wait until our process complete
