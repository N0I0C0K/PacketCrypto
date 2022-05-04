import rsa
import base64
import json
import typing
import Crypto.Cipher.AES as CryCes
from .utils import *
init = False
private_key: rsa.PrivateKey = None


def setPrivateKey(key: str):
    global private_key
    private_key = rsa.PrivateKey.load_pkcs1(key.encode())


def decryptPacket(source: typing.Union[dict, EncryptData]) -> bytes:
    data: dict = None
    if isinstance(source, EncryptData):
        data = source.dict()
    elif isinstance(source, dict):
        data = source
    else:
        raise ValueError('unsupported format')

    pass
