class Menu:
    def __init__(self, header):
        self.header = header
        self.__options = []
        print(f"--{self.header}--")

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

    def __is_valid_command(self, command):
        for i in range(len(self)):
            if command.upper() == self[i].command().upper():
                return True
        return False

    def prompt(self):
        while True:
            options = []

            for i in range(len(self)):
                option = self[i]
                if option is not None:
                    print(f"{option.command()} - {option.header()}")
                    options += option.command()

            print(f"\nEnter a {self.header} command ({', '.join(options)})")
            command = input()
            if self.__is_valid_command(command):
                return command
            else:
                print("Please enter one of the letter commands")