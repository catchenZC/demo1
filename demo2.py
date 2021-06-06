#-*- coding = utf-8 -*-
#@Author:Catchen
#@Time:2021/3/19 下午2:14
#@File:demo2.py
#@Software:PyCharm

import sys
import time

def readContent(filename):
    try:
        file = open(filename,"r")
    except Exception as errMsg:
        print("%s,即将用文件名代替文件内容进行复制！"%errMsg)
        return 1,[filename]
    content = file.read()
    line_list = content.splitlines()
    count = len(line_list)
    file.close()
    return count,line_list

def copyContent(content,strBuff,flag):
    if (flag == True) or (len(strBuff) > 0):
        try:
            file = open(content,"a")
        except Exception as errMsg:
            print(errMsg)
        file.write(strBuff)
        file.write("\n")
        file.close()


def main(argv,length):
    if length==3:
        boolenFlag=bool("")
    elif argv[3]=="False" or argv[3]=="false":
        boolenFlag=bool("")
    else:
        boolenFlag=bool("1")
    count,line_list = readContent(argv[1])
    titile = "-"*10+time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())+"-"*10
    copyContent(argv[2],titile,True)
    for i in range(count):
        str = line_list[i]
        copyContent(argv[2],str,boolenFlag)
    print("复制完毕")
    ending = "-"*40
    copyContent(argv[2],ending,True)


if __name__ == '__main__':
    length=len(sys.argv)
    if length>2:
        main(sys.argv,length)
    else:
        print("运行参数出错")