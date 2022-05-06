import sys
import os
from typing import Union
from pydantic import BaseModel

__all__ = ['EncryptData', 'model_path']

model_path = os.path.dirname(__file__)


class EncryptData(BaseModel):
    data: str
    sign: str
    key: str
    nonce: str
