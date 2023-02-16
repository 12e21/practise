#!/usr/bin/python3
from fileIO import config_build
print('欢迎使用生成矩阵文件脚本')
while True:
    print('请输入你想使用的功能:\n生成配置文件: 1\n解析配置文件生成矩阵文件: 2')
    choice=int(input())
    if choice ==1:
        print('请输入配置文件ID:')
        file_id=input()
        print('请输入矩阵行数:')
        row_count=input()
        print('请输入矩阵列数:')
        column_count=input()
        print('请输入生成矩阵个数:')
        matrix_count=input()
        config_build.build_config(file_id,row_count,column_count,matrix_count)
    elif choice==2:
        print('请输入配置文件ID:')
        file_id=input()
        configs=config_build.read_config(file_id)
        config_build.write_matrix_file('/home/www/Codes/py3_practise/file_lib',configs[0],configs[1],configs[2])
    else:
        print('请输入正确指令')
