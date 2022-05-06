import rsa
import base64
import secrets
import json
import typing
from .utils import *
import Crypto.Cipher.AES as CryCes

__all__ = ['setPublicKey', 'encryptPacket']

init = False
public_key: rsa.PublicKey = None


def setPublicKey(key: str = None):
    global public_key, init
    if key:
        public_key = rsa.PublicKey.load_pkcs1(key.encode())
    else:
        with open(model_path+'\\public_key', 'rb') as file:
            public_key = rsa.PublicKey.load_pkcs1(file.read())
    init = True


def encryptPacket(data: typing.Union[str, dict, bytes], *,
                  key: typing.ByteString = None,
                  encode_key: typing.ByteString = None,
                  custom_public_key: rsa.PublicKey = None) -> typing.Tuple[EncryptData, bytes]:
    '''
    encrypto a dict type od data
    :param data: source data, suppost `str | dict | bytes`
    :param key : custom key , use means no random key
    :param custom_public_key: use custom public key
    :return:a tuple of `EncryptData` object and the key aes use
    '''
    if isinstance(data, dict):
        s = json.dumps(data).encode()
    elif isinstance(data, str):
        s = data.encode()
    elif isinstance(data, bytes):
        s = data
    else:
        raise ValueError('unsupport format')
    key = rsa.randnum.read_random_bits(128) if key is None else key
    aes_encryptor = CryCes.new(key, CryCes.MODE_EAX)
    encode_s, sign = aes_encryptor.encrypt_and_digest(s)
    encode_s, sign = base64.b64encode(
        encode_s).decode(), base64.b64encode(sign).decode()
    if encode_key is None:
        custom_public_key = public_key if custom_public_key is None else custom_public_key
        if custom_public_key is None:
            raise ValueError('please init public key before use')
        encode_key = base64.b64encode(
            rsa.encrypt(key, custom_public_key)).decode()
    return EncryptData.parse_obj({'data': encode_s, 'sign': sign, 'nonce': base64.b64encode(aes_encryptor.nonce).decode(), 'key': encode_key}), key
