from .decrypt import *
from .encrypt import *
import rsa


class Session:
    def __init__(self, *, public_key: str = None, private_key: str = None) -> None:
        """
        a reusable, continuous conversation encryption.\n
        `public_key` and `private_key` should chose one.\n
        if a sender:
        ```
        a = Session(public_key=...)
        ```
        or if a receiver:
        ```
        a = Session(private_key=...)
        ```
        :param public_key:public key, If it is the first initiating message
        :param private_key:private key
        """
        if public_key:
            self.public_key: rsa.PublicKey = rsa.PublicKey.load_pkcs1(
                public_key.encode())
        elif private_key:
            self.private_key: rsa.PrivateKey = rsa.PrivateKey.load_pkcs1(
                private_key.encode())
        else:
            raise ValueError('please chose public_key or private key!')
        self.key: bytes = None
        self.encode_key: str = None

    def encrypto(self, message):
        data, self.key = encryptPacket(
            message, key=self.key, custom_public_key=self.public_key)
        self.encode_key = data.key
        
