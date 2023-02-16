#!/usr/bin/python3

site_to_url={'google->www.google.com'}
print('欢迎使用网站查询记录脚本:\n')
while(True):
    print('请选择要使用的功能:\n查询现有缓存: c\n添加网站: a\n退出: q')
    function_choice=input().lower()
    if  function_choice=='c':
        for site in site_to_url:
            print(site)
    elif function_choice=='a':
        print('请输入要添加的条数')
        input_count=input()
        print('请以 google->www.google.com 的形式添加你的记录')
        for i in range(int(input_count)):
            site_to_url.add(input())
    elif function_choice=='q':
        break
