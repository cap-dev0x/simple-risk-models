#MODEL 1
#TEST OF CHANGE

#Function Library

#Simple function to get the input of the users, this input is the dollar
#amount that the company has invested, will be standardized to a float for 
#all calculations - will NOT round to hundreds place 
def get_number_input():
    while True:
        try:
            user_input = input("Enter the numerical dollar value of  investment: ")
            number = float(user_input)  # Standardize to float for all calcs
            return number  # Return the float
        except ValueError:
            print("Invalid input. Please enter a valid number (int or float).")

#Investment of funds
invst = get_number_input()

#Average_time_before_investment
avg_before = 12.4

#Average_time_after_investment
avg_after = 15

investment_performance_score = (avg_before - avg_after ) * invst

print("MODEL 1")
print(investment_performance_score)

#MODEL 2

#Total number of emails phished in a set period
phish_total = 409587

#Total number of employee responses to phishing attempts (hits)
hit_total = 2

#Hit Ratio of Attacks
hit_ratio = hit_total/phish_total

investment_performance_score = hit_ratio * invst

print("MODEL 2")
print(investment_performance_score)

#MODEL 3

#Set of the times when official CVEs were first published
discovery_wilds = [3,4,6]

#Set of the times when CVEs were discovered on system
discovery_system = [5,5,8]

#CVE scores for the CVEs found 
cve_scores  = [8.0,4.3,7,1]

#Calculate datapoints for average
impact_set = []
for i in range(0,len(discovery_wilds)):
    indv_impact = (discovery_system[i] - discovery_wilds[i]) * cve_scores[i]
    impact_set.append(indv_impact)

impact_score = sum(impact_set) / len(impact_set)

investment_performance_score = impact_score * invst

print("MODEL 3")
print(investment_performance_score)