class OpenOne:
    # 公共属性
    from src.main.python.utils.ProcessNameList import ProcessNameList
    process_name_list = ProcessNameList()
    # 私有属性
    _open_files = []
    # 构造函数
    def __init__(self):
        pass

    def main(self):
        self.open_one_file()

    def open_one_file(self):
        import os
        # for 循环
        # 判断程序是否正在允许
        # 一个程序名称就是配置文件中的一个头
        running = self.process_name_list.process_is_running('idea.exe')
        if(running == False):
            # 执行对应的程序
            os.system('idea.exe')


# if __name__ == '__main__':


    # from src.main.python.utils.ProcessNameList import ProcessNameList
    # name_list = ProcessNameList()
    # list_main = name_list.main()
    # print(list_main)
    # print(name_list.process_is_running('System'))