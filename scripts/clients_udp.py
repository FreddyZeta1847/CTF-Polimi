from socket import *
import json
import threading
import config

HOST = config.SERVER_HOST
PORT = config.UDP_PORT

N = xx
CODE = "xxxxxxxxx"

# payload JSON finale
payload = config.AUTH_PAYLOAD.copy()
payload["msg_code"] = CODE

message = (json.dumps(payload)).encode("utf-8")


def send_udp(client_id):
    s = socket(AF_INET, SOCK_DGRAM)

    try:
        print(f"[#] Client {client_id} invia UDP")

        s.sendto(message, (HOST, PORT))

        # UDP: non c'è connessione → recvfrom opzionale
        s.settimeout(5)

        try:
            data, _ = s.recvfrom(4096)
            print(f"[<] Client {client_id}: {data.decode(errors='replace')}")
        except timeout:
            print(f"[<] Client {client_id}: nessuna risposta (normale UDP)")

    except Exception as e:
        print(f"[!] Client {client_id} errore:", e)

    finally:
        s.close()
        print(f"[#] Client {client_id} chiuso")


threads = []

# come richiesto: più client UDP (di solito 2)
for i in range(N):
    t = threading.Thread(target=send_udp, args=(i + 1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()