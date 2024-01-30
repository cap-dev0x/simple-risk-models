#MODEL 1

#Investment of funds
invst = 1000.0

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