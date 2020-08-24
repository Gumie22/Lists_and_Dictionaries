#This is a python program
#program creates a dictionary where the keys are the name of the country
#the value is the country's capital
countryMap = {"UnitedKingdom" : "London",
              "Sweden" : "Stockholm",
              "Canada" : "Ottawa",
              }
for country in countryMap.keys():
    country = input("Enter a country's name: ")
    print(countryMap[country])
#prints out the countryMap as per expected output              
