import sys
import os
from typing import Union

__all__ = ['EncryptData', 'model_path']

model_path = os.path.dirname(__file__)


class EncryptData:
    data: str = None
    sign: str = None
    key: str = None
    nonce: str = None

    def dict(self) -> dict:
        return self.__dict__.copy()

    @classmethod
    def parse_obj(cls, obj: dict) -> 'EncryptData':
        res = EncryptData()
        if '__annotations__' in cls.__dict__:
            for key in cls.__annotations__.keys():
                if key not in obj:
                    raise KeyError(f'variable {key} is miss')
        res.__dict__.update(obj)
        return res
