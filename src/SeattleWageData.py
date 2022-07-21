
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
                                       'Information Technology': {}}

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
        return self.department_as_key_dict

    def get_data(self):
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
            for item in wages:
                total_wage += item
                print(f"$ {item}")
            median_wage = total_wage / number_of_wages
            print(f"The number of wages counted: {number_of_wages}")
            print(f"{department}'s Median Wage: $ {round(median_wage, 2)}")

    def menu(self):
        while True:
            print("Dictionary has been initialized... ")
            person = input("Enter a person to find (FIRST_NAME LAST_NAME): ")
            if person in self.all_employee_dict.keys():
                print(self.all_employee_dict.get(person))
                return
            else:
                print(f"{person} not found")
                return