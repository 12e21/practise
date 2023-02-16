#!/usr/bin/python3
#创建参数文件函数
def build_config(file_id,row_count,column_count,matrix_count):
    file_name=f'{file_id}_config'
    file_p=open(f'/home/www/Codes/py3_practise/file_lib/'+file_name,'w+')
    text=[f'line_count:<{row_count}>\n',f'char_count:<{column_count}>\n',f'matrix_count:<{matrix_count}>']
    file_p.writelines(text)
    file_p.close()
#生成矩阵文件函数
def write_matrix_file(module_path,row_count,columncout,file_count):
    for i in range(file_count):
        file_p=open(f'{module_path}/matrix_{i}','w')
        line_text='#'*columncout
        all_text=[line_text+'\n' for i in range(row_count)]
        file_p.writelines(all_text)
        file_p.close()
#解析参数文件函数
def read_config(file_id):
    file_name=f'{file_id}_config'
    file_p=open(f'/home/www/Codes/py3_practise/file_lib/'+file_name,'r')
    lines=file_p.readlines()
    configs=[]
    for i in range(3):
        left=lines[i].find('<')
        right=lines[i].find('>')
        configs.append(int(lines[i][left+1:right]))
    return configs


