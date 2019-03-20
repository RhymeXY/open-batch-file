from src.main.python.service.OpenBatch import OpenBatch

if __name__ == '__main__':
    batch = OpenBatch()
    batch.open_batch_file('config/processes.properties')
