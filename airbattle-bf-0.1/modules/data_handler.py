class DataHandler:
    def __init__(self):
        self.data = []
        self.read_data()
    
    def read_data(self):
        data_file = open('data\\data.dat')
        idx = 0
        for data in data_file:
            self.data[idx] = data.strip()
            idx += 1
        data_file.close()
    
    def write_data(self):
        data_file = open('data\\data.dat', 'w')
        idx = 0
        for data in data_file:
            data_file.write(self.data[idx])
            idx += 1
