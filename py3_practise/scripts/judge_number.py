#!/usr/bin/python3
while True:
    print('请输入一个实数:')
    input_num=float(input())
    if input_num > 0:
        print('它是一个正数')
        if (input_num-int(input_num)==0):
            print('它是一个整数')
            multi_count=input_num
            multi_num=input_num
            while multi_count >=2:
                multi_num*=(multi_count-1)
                multi_count-=1
            print(f'它的阶乘是{multi_num}')
        else:
            print('它不是整数')
    elif input_num==0:
        print('它是零')
    else:
        print('它是一个负数')
    print('\n')
