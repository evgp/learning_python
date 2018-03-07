import socket, threading, multiprocess


def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))
            

with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        th = threading.Thread(target=process_request, args=(conn, addr))

        th.start()

# with socket.socket() as sock:
#     sock.bind(("", 10001))
#     sock.listen()
#     while True:
#         conn, addr = sock.accept() # accept incoming connection
#         conn.settimeout(5) # time, in which we are waiting for data. If no data 5 sec, we are closing con
#         with conn:
#             while True:
#                 try:
#                     data = conn.recv(1024) #1024 - buffersize in bytes
#                 except socket.timeout:
#                     print("close connection by timeout")
#                     break


#                 if not data:
#                     break
#                 print(data.decode("utf8"))