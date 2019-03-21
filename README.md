# open-batch-processes
>  通过python打开常用的多个文件，比如每天开机后需要打开Google浏览器、idea等；
>  如果有的进程已经存在于系统进程列表，则不会被运行；
>  获取系统进程列表，读取配置文件，判断哪些进程在运行，未运行的进程则会被延迟打开

## 环境
> idea python3.7

## 目录结构
> 该项目的目录结构部分仿照spring-boot的项目，如启动文件的名称是"*Application.py",目录src/main/python。

## 启动
> 需要在"src/main/python/config/processes.ini"文件中，按照规范配置需要启动的程序。

### 现状

> 因为引入了*.py文件没有放在同一个目录，所以需要互相引入import；
> 
> 所以目前只能用idea打开，配置Project SDK，然后在idea下执行src/main/python目录下的OpenBatchFileApplication.py文件。

### 计划

> 把项目改进成，只需要执行如："python37 main.py" 就能够执行的方式。