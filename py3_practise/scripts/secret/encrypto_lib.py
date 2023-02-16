#!/usr/bin/python3
#此函数用于偏移式加密/解密
def encrypto_bias(plaintext,bias):
    plaintext_list=list(plaintext)
    plainnumber_list=[ord(char) for char in plaintext_list]
    plainnumber_bias_list=[num+bias for num in plainnumber_list]
    ciphertext_list=[chr(num) for num in plainnumber_bias_list]
    ciphertext=''.join(ciphertext_list)
    return ciphertext
#此函数用于异或式加密解密(单字符密钥)
def encrypto_xor(plaintext,key):
    plaintext_list=list(plaintext)
    plainnumber_list=[ord(char) for char in plaintext_list]
    plainnumber_xor_list=[num^key for num in plainnumber_list]
    ciphertext_list = [chr(num) for num in plainnumber_xor_list]
    ciphertext = ''.join(ciphertext_list)
    return ciphertext
#此函数用于异或式加密解密(多字符密钥)
def encrypto_xor_bits(plaintext,key):
    key=[int(num) for num in list(key) ]
    plaintext_list = list(plaintext)
    plainnumber_list = [ord(char) for char in plaintext_list]
    turn=0
    plainnumber_xor_list=[]
    for i in range(len(plaintext)):
        if turn==len(key)-1:
            turn=0

        plainnumber_xor_list.append(plainnumber_list[i]^key[turn])
        turn=turn+1
    ciphertext_list = [chr(num) for num in plainnumber_xor_list]
    ciphertext = ''.join(ciphertext_list)
    return ciphertext


#本函数用于破解xor加密文本
def crack_xor(cipher_text,crack_key_count):
    cipher_list=list(cipher_text)
    ciphernumber_list=[ord(char) for char in cipher_list]
    for key in range(crack_key_count):
        ciphernumber_xor_list=[num^key for num in ciphernumber_list]
        plaintext_list=[chr(num) for num in ciphernumber_xor_list]
        plaintext=''.join(plaintext_list)
        print(f'密钥{key}: {plaintext}')
    print('\n破解已完成')





if __name__=='__main__':
    print('加密模块正在运行\n')
    encrypto_xor_bits('password: 123','345')
else:
    print('加密模块被导入\n')

