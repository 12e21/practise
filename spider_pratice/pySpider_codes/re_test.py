import re
#match,search方法
str=': tom has 25 apples'
match_res=re.match("^:.*?(\d+).*les$",str)
search_res=re.search(":.*?(\d+).*les",str)
#print(match_res.group(1))

#findall方法
multi_str=''': tom has 25 apples
: david has 30 apples
: sandy has 18 apples'''
find_all_res=re.findall(":.*?(\d+).*?les",multi_str,re.S)
# print(find_all_res)

#sub替换方法
content=re.sub("\d+","13",multi_str)
#print(content)

#compile封装匹配模式方法
pattern=re.compile("^:.*?(\d+).*?s$",re.S)
compile_res=re.match(pattern,str)
print(compile_res.group(1))