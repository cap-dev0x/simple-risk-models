#MODEL 1 

class Model_1:
    def __init__(self):
        self.investment = self.get_invest_input()
        self.avg_before = self.get_number_before()
        self.avg_after = self.get_number_after()
        self.investment_performance_score = (self.avg_before - 
                                            self.avg_after ) * self.investment

    #Simple function to get the input of the users, this input is the dollar
    #amount that the company has invested, will be standardized to a float for 
    #all calculations - will NOT round to hundreds place 
    def get_invest_input(self):
        while True:
            try:
                user_input = input("Enter the numerical dollar value of  investment: ")
                number = float(user_input)  # Standardize to float for all calcs
                return number  # Return the float
            except ValueError:
                print("Invalid input. Please enter a valid number (int or float).")

    #Simple function to get the input of the users, this input is the dollar
    #amount that the company has invested, will be standardized to a float for 
    #all calculations - will NOT round to hundreds place 
    def get_number_before(self):
        while True:
            try:
                user_input = input("Enter the average fix time before investment: ")
                number = float(user_input)  # Standardize to float for all calcs
                return number  # Return the float
            except ValueError:
                print("Invalid input. Please enter a valid number (int or float).")

    #Simple function to get the input of the users, this input is the dollar
    #amount that the company has invested, will be standardized to a float for 
    #all calculations - will NOT round to hundreds place 
    def get_number_after(self):
        while True:
            try:
                user_input = input("Enter the average fix time after investment: ")
                number = float(user_input)  # Standardize to float for all calcs
                return number  # Return the float
            except ValueError:
                print("Invalid input. Please enter a valid number (int or float).")

    def __str__(self):
        return f"Investment: {self.investment}, Avg Before: {self.avg_before}, Avg After: {self.avg_after}"

test = Model_1()
print(test.investment_performance_score)
