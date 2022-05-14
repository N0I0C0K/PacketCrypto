import rsa
import base64
import json
import typing
import Crypto.Cipher.AES as CryCes
from .utils import *
init = False
private_key: rsa.PrivateKey = None

__all__ = ['setPrivateKey', 'decryptPacket', 'decryptPacket_bytes']


def setPrivateKey(key: str = None):
    global private_key, init
    if key:
        private_key = rsa.PrivateKey.load_pkcs1(key.encode())
    else:
        with open(model_path+'\\private_key', 'rb') as file:
            private_key = rsa.PrivateKey.load_pkcs1(file.read())
    init = True


def decryptPacket(source: typing.Union[dict, EncryptData], *,
                  key: typing.ByteString = None,
                  custom_private_key: rsa.PrivateKey = None) -> typing.Tuple[bytes, bytes]:
    '''
    decrypto from `dict | EncryptData`
    :param source: the source data , type of`dict | EncryptData`
    :param key : custom key , use means no random key
    :param custom_private_key : use custom private key.
    :return: a tuple of decrypto data `bytes` and the key aes use
    '''
    data: EncryptData = None
    if isinstance(source, EncryptData):
        data = source
    elif isinstance(source, dict):
        data = EncryptData.parse_obj(source)
    else:
        raise ValueError('unsupported format')
    if key is None:
        custom_private_key = private_key if custom_private_key is None else custom_private_key
        if custom_private_key is None:
            raise ValueError('please init private key')
        key = rsa.decrypt(base64.b64decode(data.key),
                          custom_private_key)
    aes_encrypt = CryCes.new(key, CryCes.MODE_EAX,
                             nonce=base64.b64decode(data.nonce))
    res = aes_encrypt.decrypt_and_verify(base64.b64decode(
        data.data), base64.b64decode(data.sign))
    return res, key


def decryptPacket_bytes(source : typing.ByteString, *,
                        key: typing.ByteString = None,
                        custom_private_key: rsa.PrivateKey = None) -> typing.Tuple[bytes, bytes]:
    '''
    decrypto from `bytes`
    :param source: the source data, must bytes.
    :param key : custom key , use means no random key
    :param custom_private_key : use custom private key.
    :return: a tuple of decrypto data `bytes` and the key aes use
    '''
    source = bytearray(source)
    nonce_len = int.from_bytes(source[0:4], 'big')
    key_len = int.from_bytes(source[4:8], 'big')
    sign_len = int.from_bytes(source[8:12], 'big')
    idx = 12
    nonce = source[idx:idx+nonce_len]
    idx = idx+nonce_len
    if key is None:
        custom_private_key = private_key if custom_private_key is None else custom_private_key
        if custom_private_key is None:
            raise ValueError('please init private key')
        key = rsa.decrypt(bytes(source[idx:idx+key_len]),
                          custom_private_key)
    idx = idx+key_len
    sign = source[idx:idx+sign_len]
    idx = idx+sign_len
    data = source[idx:]
    aes_encrypt = CryCes.new(key, CryCes.MODE_EAX,
                             nonce=nonce)
    return aes_encrypt.decrypt_and_verify(data, sign), key
