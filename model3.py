#MODEL 3

##TODO Convert this model into an object
##TODO Create functionality for user input 

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
