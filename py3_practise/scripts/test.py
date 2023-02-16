#!/usr/bin/python3
def show_sites(**sites):
    sites_names=list(sites.keys())
    for i in range(len(sites_names)):
        print(f'网站名是{sites_names[i]},url是{sites[sites_names[i]]}')
show_sites(baidu='www.baidu.com',google='www.google.com',runoob='www.runoob.com')