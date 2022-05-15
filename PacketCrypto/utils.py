import sys
import os
from typing import Union

__all__ = ['EncryptData', 'model_path']

model_path = os.path.dirname(__file__)


class EncryptData:
    def __init__(self) -> None:
        self.data: str = None
        self.sign: str = None
        self.key: str = None
        self.nonce: str = None

    def dict(self) -> dict:
        res = {}
        for key in self.__init__.__code__.co_names:
            res.update({key: self.__getattribute__(key)})
        return res

    @staticmethod
    def parse_obj(obj: dict) -> 'EncryptData':
        res = EncryptData()
        res.__dict__.update(obj)
        return res
