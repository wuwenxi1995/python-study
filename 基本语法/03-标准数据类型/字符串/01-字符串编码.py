"""
encode: 将字符串转为二进制字节流,转码
    b = b'hello' ==> 使用b将字符串类型转为字节流
    print(b, type(b)) ==> b'hello' <class 'bytes'>
    或直接使用字符串函数encode进行转码
decode: 将二进制字节流转为字符串, 解码

"""

b = b'hello'
print(b, type(b))
a = 'hello'
encoda = a.encode()
print('encode', encoda, type(encoda))

decodea = encoda.decode()
print('decode', decodea, type(decodea))
