import json
import csv


class File:
    def __init__(self, path, delimiter=",", extension=""):
        self.path = path
        self.delimiter = delimiter
        self.extension = extension if extension else self.path.suffix
        self.read()

    def read(self):
        with open(self.path, 'r', encoding="utf-8-sig") as f:
            match self.extension:
                case '.csv':
                    file = csv.reader(f, delimiter=self.delimiter)
                    self.content = []
                    for row in file:
                        self.content.append(row)
                case '.json':
                    self.content = json.load(f)
                case _:
                    print("File extension not supported")
