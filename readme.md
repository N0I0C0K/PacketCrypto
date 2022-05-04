# Packet Encryptor
Python数据传输加密中间件, 适用于体积不大的数据传输.基于RSA, AES实现的数据加密模块.

## Usage
用户端代码
```python
#client
from PacketCrypto import *
from requests import get
setPublicKey(...)
data = {'name':'test','pwd':'123'}
get('http://test.com/test', json = encryptPacket(data).dict())
```

服务端代码
```python
#server  , based on fastapi

setPrivateKey(...)
@get('/test')
def test(form:EncryptData):
    return decryptPacket(form)
```