import sys
import os
from typing import Union

__all__ = ['EncryptData', 'model_path']

model_path = os.path.dirname(__file__)


class EncryptData:
    data: str
    sign: str
    key: str
    nonce: str

    @staticmethod
    def parse_obj(obj: dict) -> 'EncryptData':
        res = EncryptData()
        res.__dict__.update(obj)
        return res
