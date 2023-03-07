# 移除指定文件下的JPG格式文件

# 功能设计
**核心功能：** 用户输入指定年份和月份，然后删除指定年份+月份下，微信Video目录下，多余的JPG格式文件。
**
**交互设计：** 需要用户输入年份和月份，程序输出详细执行结果，包括：

- 删除的具体目录是否与输入匹配
- 删除操作是否成功
- 具体删除的文件名称，包括文件名和文件类型



**功能设计：** 

1. 本来是想做成交互式的，但是后来想想，写脚本就是为了简化操作的，不能做复杂了，所以改为脚本+参数的方式：python 脚本名称 参数1（年份） 参数2（月份）
1. 微信Video目录设置为常量，通过字符串拼接，结合用户输入的年份+月份，输出完整的目录结构
1. 通过os库获取目录下全部文件，文件会以列表形式返回，存储在一个变量里
1. 通过循环读取列表里的值，并判断文件类型是否为JPG格式
1. 如果是JPG格式则继续调用os命令删除这个JPG文件
1. 过程中输出对应执行结果即可



# 编写代码
```python
# 获取用户输入的参数
sys.argv[0]	# 脚本名称
sys.argv[1] # 用户输入的第一个参数
sys.argv[2] # 用户输入的第二个参数

# 获取目录下全部文件
os.listdir()

# 获取文件的文件类型，这里使用第三方库filetype，需要使用pip命令单独安装
import filetype
kind = filetype.guess(具体文件)
kind.extension	# 即为文件类型

# 删除指定文件
os.remove(具体文件)
```
参考功能设计以及上述可用参考代码，组合完整代码如下：


```python
#! /bin/python
# -*- coding:utf-8 -*-

import os, sys
import filetype

WECHAT_VIDEO = "/mnt/d/Docs/WeChat Files/zxz1203/FileStorage/Video/"


def main():
    TargetDir = WECHAT_VIDEO + str(sys.argv[1]) + "-" + str(sys.argv[2])
    if os.path.exists(TargetDir):
        print "要删除的目录为: %s" % TargetDir
    else:
        print "没有找到对应目录"
        exit(1)
    TargetFiles = os.listdir(TargetDir)
    for value in range(0, len(TargetFiles)):
        TargetFile = os.path.join(TargetDir, TargetFiles[value])
        TargetKind = filetype.guess(TargetFile)
        if TargetKind.extension == 'jpg':
            print "移除目标文件: %s" % TargetFile
            os.remove(TargetFile)

    print "暂无JPG文件需要移除"


if __name__ == "__main__":
    main()
```


