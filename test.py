from PacketCrypto import *

# # generateRsaKey()
# setPublicKey()

# encode, key = encryptPacket(
#     {'name': 123, 'dasd': 'dasdasd', 'list': [123, 21, 21, 2]})
# print(encode)
# print(key)
# setPrivateKey()
# decode = decryptPacket(encode)
# print(decode)

public = '''-----BEGIN RSA PUBLIC KEY-----
MEgCQQCJ0HrhHs//dy6t2SkSFLB9gIbBnn6qUOTSGxmuACImCGMrWZo9GrDCSOV3
iYz4xwVJb2V9sAHP7ltQApYMht4vAgMBAAE=
-----END RSA PUBLIC KEY-----
'''

private = '''-----BEGIN RSA PRIVATE KEY-----
MIIBOwIBAAJBAInQeuEez/93Lq3ZKRIUsH2AhsGefqpQ5NIbGa4AIiYIYytZmj0a
sMJI5XeJjPjHBUlvZX2wAc/uW1AClgyG3i8CAwEAAQJANxjDV6cy7uZeIiDUu6bL
3JD6zwOnjj3jDWDKRndE9XrSe4aWdjuh5Spz8+9U6ERnes/cgRwoxPbz1yfLGewG
mQIjAJHECFClZUjEuEWLPM3HYo2APNyMJ3rmTUcK2KEAxrQrAbsCHwDyCROK0ZUn
e7boLMmW2Ij0j/yWPBnRq9YfWBF2RB0CIgSCJquv4ekVRInKG7BVqWOtArTjlNkF
RICdAkRAjOTHq78CHkMtfb0T+sAguF2swK8bnreylzrjp47okN/WQ9J9iQIiIrcP
2p3NHKXLnlFGnML4AunpoZFkkXR2uPwzJBrddW+77g==
-----END RSA PRIVATE KEY-----
'''


def session_test():
    sender = Session(public_key=public)
    recv = Session(private_key=private)
    print(recv.decrypto(sender.encrypto({'name': 'sender send'})))
    print(sender.decrypto(recv.encrypto({'name': 'recv send'})))


session_test()
