class DataHandler:
    def __init__(self):
        self.data = []
        self.read_data()
    
    def read_data(self):
        data_file = open('data\\data.dat')
        for data in data_file:
            self.data.append(data.strip())
        data_file.close()
    
    def write_data(self):
        data_file = open('data\\data.dat', 'w')
        for data in self.data:
            data_file.write(data + '\n')
