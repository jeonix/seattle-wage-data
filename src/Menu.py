class Menu:
    def __init__(self, header):
        self.header = header
        self.__options = []
        print(f"\n--{self.header}--")

    def __iadd__(self, option):
        self.__options.append(option)
        return self

    def __len__(self):
        return len(self.__options)

    def __getitem__(self, item):
        if 0 <= item < len(self):
            return self.__options[item]
        else:
            raise IndexError
