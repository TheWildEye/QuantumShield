
import time, requests
from client.kemtls_client import KEMTLSClient

BASE="http://localhost:8000"

def run():
    kem=KEMTLSClient()
    t0=time.time()
    sid=kem.initiate_handshake(BASE)
    t1=time.time()

    h={"X-Session-ID":sid}
    a0=time.time()
    r=requests.post(BASE+"/authorize",json={"data":kem.encrypt(b"x")},headers=h)
    a1=time.time()

    t0b=time.time()
    r2=requests.post(BASE+"/token",json={"data":kem.encrypt(b"x")},headers=h)
    t1b=time.time()

    print("Handshake latency:",t1-t0)
    print("Auth latency:",a1-a0)
    print("Token latency:",t1b-t0b)
    jwt = kem.decrypt(r2.json()["data"])
    print("JWT size:", len(jwt))


if __name__=="__main__":
    run()
