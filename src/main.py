import sys
import time

from SeattleWageData import SeattleWageData

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Not enough arguments given")
        sys.exit(1)
    else:
        print("Reading the Databases... ")
        csvFile = sys.argv[1]
        data = SeattleWageData(csvFile)
        data.separate_by_department()
        data.menu()
