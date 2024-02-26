#MODEL 2

#TODO determine if there should be a standardized period of time, or an 
#enumeration of most useful times

class Model_2:
    def __init__(self):
        self.investment = self.get_invest_input()
        self.phish_total = self.get_phish_total()
        self.hit_total = self.get_hit_total()
        self.hit_ratio = self.calc_hit_ratio()
        self.investment_performance_score = self.calc_investment_performance_score()

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

    #Getter function to get the total number of phishing attempts in a given period of
    #time.
    def get_phish_total(self):
        while True:
            try:
                user_input = input("Enter the total number of phishing attempts: ")
                number = float(user_input)  # Standardize to float for all calcs
                return number  # Return the float
            except ValueError:
                print("Invalid input. Please enter a valid number (int or float).")
    
    #Getter function to get the total number of phishing attempts in a given period of
    #time.
    def get_hit_total(self):
        while True:
            try:
                user_input = input("Enter the total number of successful phishing attacks: ")
                number = float(user_input)  # Standardize to float for all calcs
                return number  # Return the float
            except ValueError:
                print("Invalid input. Please enter a valid number (int or float).")

    #Calculation for the ratio of success/total attempts, used in calculating the 
    #investment performance score
    def calc_hit_ratio(self):
        return self.hit_total / self.phish_total
    
    #Calculation for the investment performance score, in this model the lower
    #the lower the value in the IPS, the more impact the investment had
    def calc_investment_performance_score(self):
        return self.hit_ratio * self.investment 
    
    #Call to run the model
    def run_model_2(self):
        print("###Model 2 Analysis###")
        print(f"Initial Investment: {self.investment}")
        print(f"Total Phishing Attempts: {self.phish_total}")
        print(f"Total Successful Attacks: {self.hit_total}")
        print(f"Investment Performance Score: {self.investment_performance_score}")

test_model_2 = Model_2()
test_model_2.run_model_2()