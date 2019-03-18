class ProcessNameList:

    def __init__(self):
        pass

    def main(self):
        name = self.get_process_name_list()
        return name

    # 当前进程的进程名list
    def get_process_name_list(self):
        names = []

        import psutil

        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
            except psutil.NoSuchProcess:
                pass
            else:
                names.append(pinfo['name'])

        return names

    # name对应的进程名是否存在于list中
    def process_is_running(self, name):
        names = self.get_process_name_list()
        return names.__contains__(name)


if __name__ == '__main__':
    process = ProcessNameList()
    print(process.get_process_name_list())
    print(process.process_is_running('smss.exe'))
