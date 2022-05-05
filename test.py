from PacketCrypto import *

# generateRsaKey()
setPublicKey()

encode, key = encryptPacket(
    {'name': 123, 'dasd': 'dasdasd', 'list': [123, 21, 21, 2]})
print(encode)
print(key)
setPrivateKey()
decode = decryptPacket(encode)
print(decode)
