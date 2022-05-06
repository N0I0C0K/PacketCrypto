from .decrypt import decryptPacket
from .encrypt import encryptPacket
from .utils import EncryptData
import typing
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
        self.private_key = None
        self.public_key = None
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

    def encrypt(self, source) -> EncryptData:
        data, self.key = encryptPacket(
            source, key=self.key, encode_key=self.encode_key, custom_public_key=self.public_key)
        self.encode_key = data.key
        return data

    def decrypt(self, source: typing.Union[EncryptData, dict]) -> bytes:
        self.encode_key = source.key
        data, self.key = decryptPacket(source, key=self.key,
                                       custom_private_key=self.private_key)
        return data

    def __hash__(self) -> int:
        return hash(self.encode_key)
