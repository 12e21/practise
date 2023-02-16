#!/usr/bin/python3
import encrypto_lib
while True:
    print('请选择模式:\n加密: 1\t解密: 2\t退出: 3')
    choice=int(input())
    if choice==1:
        print('请输入要加密的文本:')
        plaintext=input()
        print('请输入加密钥匙: (格式:十以内整数)')
        bias=int(input())
        ciphertext=encrypto_lib.encrypto(plaintext,bias)
        print(f'加密后文本:\n{ciphertext}\n')
        del plaintext,ciphertext
    elif choice==2:
        print('请输入要解密的文本:')
        ciphertext=input()
        print('请输入解密钥匙:')
        bias=int(input())
        plaintext=encrypto_lib.unencrypto(ciphertext,bias)
        print(f'解密后文本:\n{plaintext}\n')
    elif choice==3:
        break
    else:
        print('请输入正确指令')


