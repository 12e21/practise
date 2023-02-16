#!/usr/bin/python3
# 此脚本用于加密和解密文本(解密的偏移取加密偏移负数即可)
# 获取要加密的文本和偏移长度
print('请输入要加密的文本:')
plaintext=input()
print('请输入偏移的长度:')
bias=int(input())


# 处理明文
# 将明文字符串转成列表
plaintext_list=list(plaintext)
# 将明文列表转成ASC码的数字列表
plainnumber_list=[ord(char) for char in plaintext_list]
# 为数字列表添加偏移
plainnumber_bias_list=[num+bias for num in plainnumber_list]
# 将偏移后数字列表转成隐文字符列表
ciphertext_list=[chr(num) for num in plainnumber_bias_list]
# 将隐文列表拼接成字符串
ciphertext=''.join(ciphertext_list)

# 输出隐文
print('加密后文本是：\n',ciphertext)

