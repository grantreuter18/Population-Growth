"""
Grant Reuter
CSC 201
Programming Project 1

DESCRIPTION OF PROJECT:
This program calculates population growth. The user will input country name, year population, growth rate, and how years its wants to predict.
At the end of the program it will print the countries averages, max, min, and how many countries have a high and low growth rate.

"""
def main():
    #Beginning of the program 
    print("=== POPULATION GROWTH ESTIMATOR ===")
    print("This program estimates population growth of several countries")
    print()
    
    #counters for the program 
    sum = 0
    max = 0
    min = 0
    #country max counter and country name is stored in""
    countryMax = -10000
    countryNameMax = ""
    
    oneYearMax = 0
    oneYearMaxName = ""
    
    lastYearMax = 0
    lastYearMaxName = ""
    
    #asking for number of countries to be printed 
    NumberOfCountries = int(input("Number of countries: "))
    #if you dont enter a valid input then the program just exits  
    if NumberOfCountries <= 0:
        print("Error:",NumberOfCountries,"is not valid input") 
        exit(-1)
        
    numYears = int(input("Number of years: "))
    if numYears <= 0:
        print("Error:",numYears,"is not valid input")
        exit(-1)
    
    
    #Asks for userinput for country name, population, and growthrate
    for countries in range(NumberOfCountries):
        print()
        print("--- Country "+str(countries+1)+ "  ---")
        countryName=input("Country name: ")
        populationYear1=float(input("Year 1 population of "+ countryName + " (in millions): "))
        growthRate=float(input("Population growth rate (% per year): "))
        
        
        #if growthrate is greater than 1 then its stores as the max
        if growthRate > 1:
            max = max + 1 
        #if growthrate is less than or equal 0.1 then its stores as the min
        elif growthRate <= 0.1:
            min= min + 1
        
        #stores the country name with the biggest growthrate and the number 
        if growthRate > countryMax:
            countryNameMax = countryName
            countryMax = growthRate
        #stores the biggest population of year 1 and the countries name
        if populationYear1 > oneYearMax:
            countryYearMaxName = countryName
            oneYearMax = populationYear1
        #This finds the how much each country will go up each year    
        population = populationYear1
        for numYear in range(1, numYears):
            increase = population * (growthRate/100)
            population = increase + population 
            roundPopulation = round(population, 3)
            print("Year " +str(numYear + 1) + " population of " + countryName +" (in millions):",roundPopulation)
        #This stores the biggest population for the last year
            if roundPopulation > lastYearMax:
                lastYearMaxName = countryName
                lastYearMax = roundPopulation
        #this line stores the total population of all the countries
        sum=sum+population
            
    #this finds the avergae of all the countries and replaces it in sum
    average = sum/NumberOfCountries 
    raverage = round(average, 3)    
    print()
    #prints the summary of all the data 
    print("Summary Report")
    print("    Average year",numYears,"population of all countries:",raverage) 
    print("    Number of countries with high growth rate:",max)
    print("    Number of countries with low growth rate:",min)
    print("    Country with highest growth rate:",countryNameMax)
    print("    Country with maximum Year 1 population ("+ str(oneYearMax),"million):",countryYearMaxName)
    print("    Country with maximum Year",numYears,"Population ("+ str (lastYearMax),"million):",lastYearMaxName)
    
    
main()
