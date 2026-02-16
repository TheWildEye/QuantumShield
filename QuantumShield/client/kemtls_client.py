# client/kemtls_client.py

import requests
from oqs import KeyEncapsulation
from crypto.symmetric import SymmetricChannel

class KEMTLSClient:
    def __init__(self):
        self.kem = KeyEncapsulation("Kyber768")
        self.channel = None
        self.sid = None

    def initiate_handshake(self, base_url):
        # Step 1: fetch server public key
        r = requests.get(base_url + "/kemtls/server-pk")
        server_pk = bytes.fromhex(r.json()["server_pk"])

        # Step 2: encapsulate
        ciphertext, shared_secret = self.kem.encap_secret(server_pk)

        r2 = requests.post(
            base_url + "/kemtls/handshake",
            json={"ciphertext": ciphertext.hex()}
        )

        self.sid = r2.json()["session_id"]
        self.channel = SymmetricChannel(shared_secret)
        return self.sid

    def encrypt(self, data: bytes):
        return self.channel.encrypt(data)

    def decrypt(self, data: str):
        return self.channel.decrypt(data)
