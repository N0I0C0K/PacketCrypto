# Packet Crypto
Python数据传输加密中间件, 适用于体积不大的数据传输.基于RSA, AES实现的数据加密模块.
适用于:
- API服务器数据加密传输


## Usage
- API服务器数据加密传输:

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
- 长对话加密(Session)
    首先我们规定:第一个发送消息的是Sender, 接收的是Recvicer

    Sender:
    ```python
    from PacketCrypto import *
    sender_crypto = Session(public_key=public)
    send(sender_crypto.encrypt({'name': 'sender_crypto send'}))

    # 接收到消息
    print(sender_crypto.decrypt(data))

    ```
    Recvice:
    ```python
    from PacketCrypto import *
    recv_crypto = Session(private_key=private)
    recv_crypto.decrypt(data)

    # 加密发送
    send(recv_crypto.encrypt({'name':'recv send'}))
    ```

    可以去看看`test.py`里的`session_test()`
