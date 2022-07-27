from Menu import Menu
from MenuOption import MenuOption

class SeattleWageData:
    def __init__(self, csvFile=None):
        self.csvFile = csvFile
        self.all_employee_dict = {}
        self.department_as_key_dict = {}
        self.assign_to_dict()

    def __read_file(self):
        if self.csvFile is not None:
            with open(self.csvFile) as openFile:
                openFile.readline()  # Discard column header
                file = openFile.readlines()
                openFile.close()
            return file
        else:
            print("File is invalid")

    def assign_to_dict(self):
        file = self.__read_file()
        for line in file:
            csv_list = line.rstrip().split(',')
            last_name = csv_list[1]
            first_name = csv_list[2]
            department = csv_list[0]
            job_title = csv_list[3]
            hourly_rate = csv_list[4]
            self.all_employee_dict[f"{first_name} {last_name}"] = {}
            self.all_employee_dict[f"{first_name} {last_name}"]['Department'] = department
            self.all_employee_dict[f"{first_name} {last_name}"]['Job Title'] = job_title
            self.all_employee_dict[f"{first_name} {last_name}"]['Hourly Rate'] = hourly_rate
        print()

    def separate_by_department(self):
        self.department_as_key_dict = {'Police Department': {},
                                       'Seattle City Light': {},
                                       'Parks & Recreation': {},
                                       'Seattle Dept of Transportation': {},
                                       'Construction & Inspections': {},
                                       'Fire Department': {},
                                       'Finance & Admin Services': {},
                                       'Human Services Department': {},
                                       'Seattle Public Utilities': {},
                                       'City Budget Office': {},
                                       'Seattle Center': {},
                                       'Information Technology': {},
                                       'Office of Labor Standards': {},
                                       'Office for Civil Rights': {}}

        for person in self.all_employee_dict:
            if self.all_employee_dict.get(person)['Department'] == 'Police Department':
                self.department_as_key_dict['Police Department'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Seattle City Light':
                self.department_as_key_dict['Seattle City Light'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Parks & Recreation':
                self.department_as_key_dict['Parks & Recreation'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Seattle Dept of Transportation':
                self.department_as_key_dict['Seattle Dept of Transportation'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Construction & Inspection':
                self.department_as_key_dict['Construction & Inspection'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Fire Department':
                self.department_as_key_dict['Fire Department'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Finance & Admin Services':
                self.department_as_key_dict['Finance & Admin Services'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Human Services Department':
                self.department_as_key_dict['Human Services Department'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Seattle Public Utilities':
                self.department_as_key_dict['Seattle Public Utilities'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'City Budget Office':
                self.department_as_key_dict['City Budget Office'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Seattle Center':
                self.department_as_key_dict['Seattle Center'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Information Technology':
                self.department_as_key_dict['Information Technology'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Office of Labor Standards':
                self.department_as_key_dict['Office of Labor Standards'][person] = self.all_employee_dict.get(person)
            elif self.all_employee_dict.get(person)['Department'] == 'Office for Civil Rights':
                self.department_as_key_dict['Office for Civil Rights'][person] = self.all_employee_dict.get(person)
        return self.department_as_key_dict

    def find_name_all_departments(self):
        person = input("What is the first and the last name of the person you are trying to find? ")
        if person in self.all_employee_dict:
            print(f"{person}'s information is {self.all_employee_dict.get(person)}")
        else:
            print(f"{person} was not found")

    def get_wages(self):
        print("The available departments: ")
        for key in self.department_as_key_dict.keys():
            print(key)
        print()
        department = input("Which department would you like to review? ")
        if department not in self.department_as_key_dict:
            print("That department is not in the database")
            return
        else:
            found_wages = []
            wages = []
            total_wage = 0
            for person in self.department_as_key_dict[department]:
                found_wages.append(self.department_as_key_dict[department][person]['Hourly Rate'])
            for wage in found_wages:
                if wage.replace('"', "")[0].isalpha():
                    found_wages.remove(wage)
                    continue
                elif wage.replace('"', "")[1].isalpha():
                    found_wages.remove(wage)
                    continue
                else:
                    num = float(wage.replace("'", ""))
                    wages.append(num)
            number_of_wages = len(wages)
            largest_wage = 0
            for item in wages:
                if item > largest_wage:
                    largest_wage = item
                total_wage += item
            list_wages_command = input("Would you like to print a list of the wages? (yes/no): ")
            if list_wages_command.lower() == 'yes':
                for item in wages:
                    print(f"$ {item}")
            print()
            if number_of_wages == 0:
                print(f"There are {number_of_wages} wages for the {department} department")
            else:
                median_wage = total_wage / number_of_wages
                print(f"{department}'s Median Wage: $ {round(median_wage, 2)}")
            print(f"The number of wages counted: {number_of_wages}")
            print(f"The greatest wage in {department}: $ {round(largest_wage, 2)}")
            print()

    def menu(self):
        menu = Menu("City of Seattle Wage Data Menu")
        menu += MenuOption("W", "Look up wages for a Department")
        menu += MenuOption('F', "View an employee's wage data")
        menu += MenuOption('X', "Exit the program")
        print()
        while True:
            command = menu.prompt()
            if command.upper() == 'W':
                self.get_wages()
                continue
            elif command.upper() == 'F':
                self.find_name_all_departments()
                continue
            elif command.upper() == 'X':
                print("Thank you for using this program")
                break
                