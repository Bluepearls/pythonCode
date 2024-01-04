from zipfile import ZipFile
import os

def passwd(path, pwd):
    # 获取文件的后缀名
    suffix_name = os.path.splitext(path)[-1][1:]
    # print(suffix_name)
    # 如果是zip文件
    if suffix_name == 'zip':
        # 开始读zip文件
        with ZipFile(path, 'r') as zip:
            # print("当前尝试的密码是:%s"%(pwd))
            # 解压到指定文件目录下
            try:
                # print(pwd.encode('utf-8'))
                zip.extractall("C:\Learning\Python\Code", pwd=pwd.encode('utf-8'))
                print("解压成功，密码是：%s"%(pwd))
                return True
            except Exception as e: # 添加一个异常处理
                pass

def create_pwd(words):
    # 通过导入这包来设置枚举序列
    import itertools as its
    # 设置基础需要枚举的字符集

    # 这个base的意思就是把words集合的字符取repeat次组合
    # 打印出来
    base = its.product(words, repeat=6)

    # 一般需要把这个打印函数注释 因为这个函数运行很消耗时间的
    for i in base:
        # print(''.join(i))
        yield ''.join(i) # 把这个函数制作成一个迭代器

if __name__ == '__main__':

    words = '123456789'
    dir = 'C:\Learning\Python\Code\\test.zip'
    for p in create_pwd(words):
        flag = passwd(dir, p)
        if flag == True:
            break

