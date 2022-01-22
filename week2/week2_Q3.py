class ReadCSV():
    def __init__(self, file_path:str):
        self.file_path = file_path

    def read_file(self) -> list:
        content = list()
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            print(lines)
            for line in lines:
                line = line.strip().split(',')
                content.append(line)
        return content

file_path = 'week2\data-01-test-score.csv'
read_csv = ReadCSV(file_path)
print(read_csv.read_file())