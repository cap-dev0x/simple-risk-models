#MODEL 3

class Model_3:
    def __init__(self):
        self.investment = self.get_investment_input()
        self.discovery_wilds = []
        self.discovery_systems = []
        self.cve_scores = []
        self.impact_set = []
        self.impact_score = False #currently set to false for troubleshooting
        self.investment_performance_score = False #same set as impact_score

    #Helper function for get_arrays_inputs(), allows for a narrowing of 
    #get_arrays_input's functionality
    def get_arrays_size(self):
        while True:
            try:
                user_input = int(input("Enter the total number of iterations: "))
                return user_input
            except:
                print("Invalid input, please enter a whole number")

    #User sets the number of iterations, populates the user input into the 
    #the arrays of the object
    #TODO add input validation for each of the input functions in the foo
    def get_arrays_inputs(self):
        total_rounds = self.get_arrays_size()
        
        for item in range(0, total_rounds):
            self.discovery_wilds.append(int(input("Enter the time of CVE publication")))
            self.discovery_systems.append(int(input("Enter the time of discovery on system")))
            self.cve_scores.append(int(input("Enter the CVE score for the CVE")))
            
    #Simple function to get the input of the users, this input is the dollar
    #amount that the company has invested, will be standardized to a float for 
    #all calculations - will NOT round to hundreds place 
    def get_investment_input(self):
        while True:
            try:
                user_input = input("Enter the numerical dollar value of  investment: ")
                number = float(user_input)  # Standardize to float for all calcs
                return number  # Return the float
            except ValueError:
                print("Invalid input. Please enter a valid number (int or float).")

    #Function to calculate data points for the average, directly appends the 
    #results of the computations to self.impact set instead of returning an
    #array
    def calc_impact_set(self):
        for i in range(0,len(self.discovery_wilds)):
            indv_impact = (self.discovery_systems[i] - self.discovery_wilds[i]) * self.cve_scores[i]
            self.impact_set.append(indv_impact)

    #Calculates the impact score by finding the average exposure time of the 
    #CVEs
    def calc_impact_score(self):
        self.impact_score = sum(self.impact_set) / len(self.impact_set)

    #Higher in value the investment score, the more impact the investment 
    #has had. 
    def calc_investment_performance_score(self):
        self.investment_performance_score = self.impact_score * self.investment

    #Function to run the model
    def run_model_3(self):
        self.get_arrays_inputs()
        self.calc_impact_set()
        self.calc_impact_score()
        self.calc_investment_performance_score()

        print("###Model 3 Analysis###")
        print(f"Initial Investment: {self.investment}")
        print(f"Total CVEs Found: {len(self.discovery_systems)}")
        print(f"Average Discovery Time: {self.impact_score}")
        print(f"Investment Performance Score: {self.investment_performance_score}")

test_3 = Model_3()
test_3.run_model_3()





