import json


class FindWiki:
    def __init__(self, path):
        self.file = open(path, "r")
        self.data = json.load(self.file)
        self.start = 0
        self.end = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration
        data_1 = self.data[self.start]
        self.start += 1
        return data_1


if __name__ == '__main__':
    for find_str in FindWiki('countries.json'):
        print(find_str)
