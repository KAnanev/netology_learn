class FindWiki:
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, encoding='utf8')

    def __iter__(self):
        return self

    def __next__(self):
        read_file = self.file.readline()
        if not read_file:
            raise StopIteration
        return read_file


if __name__ == '__main__':
    for find_str in FindWiki('countries.json'):
        print(find_str)


