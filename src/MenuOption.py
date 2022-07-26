class MenuOption:
    def __init__(self, command, header):
        self.__command = command
        self.__header = header

    def command(self):
        return self.__command

    def header(self):
        return self.__header

    def __str__(self):
        return f"{self.__command} {self.__header}"
