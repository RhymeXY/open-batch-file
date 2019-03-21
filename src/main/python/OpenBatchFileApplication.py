from src.main.python.service.OpenBatch import OpenBatch
import logging

# 设置日志级别为DEBUG
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    batch = OpenBatch()
    batch.open_batch_file('config/processes.properties')
