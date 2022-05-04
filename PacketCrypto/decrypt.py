import rsa
import base64
import json
import typing
import Crypto.Cipher.AES as CryCes
from .utils import *
init = False
private_key: rsa.PrivateKey = None


def setPrivateKey(key: str = None):
    global private_key, init
    if key:
        private_key = rsa.PrivateKey.load_pkcs1(key.encode())
    else:
        with open(model_path+'\\private_key', 'rb') as file:
            private_key = rsa.PrivateKey.load_pkcs1(file.read())
    init = True


def decryptPacket(source: typing.Union[dict, EncryptData]) -> bytes:
    data: EncryptData = None
    if isinstance(source, EncryptData):
        data = source
    elif isinstance(source, dict):
        data = EncryptData.parse_obj(source)
    else:
        raise ValueError('unsupported format')
    key = rsa.decrypt(base64.b64decode(data.key), private_key)
    aes_encrypt = CryCes.new(key, CryCes.MODE_EAX,
                             nonce=base64.b64decode(data.nonce))
    res = aes_encrypt.decrypt_and_verify(base64.b64decode(
        data.data), base64.b64decode(data.sign))
    return res
