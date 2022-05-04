import rsa
import os
from typing import Tuple
from .utils import *


__all__ = ['generateRsaKey']


def generateRsaKey():
    '''
    生成一对公钥和密钥
    '''
    pub, pri = rsa.newkeys(512)
    path = os.path.dirname(__file__)
    with open(path+'\\private_key', 'wb') as file:
        print(f'[*] private key => {file.name}')
        file.write(pri.save_pkcs1())
    with open(path+'\\public_key', 'wb') as file:
        print(f'[*] public key => {file.name}')
        file.write(pub.save_pkcs1())
    print(f'{set_color("public key", COLOR.BLUE)}:\n{pub.save_pkcs1().decode()}')
    print(f'{set_color("private key", COLOR.CYAN)}:\n{pri.save_pkcs1().decode()}')
