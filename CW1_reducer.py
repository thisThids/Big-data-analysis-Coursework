#! /usr/bin/env python3
import sys

current_date = None
counter = 0
cur_max_val = 0
cur_min_val = 0
key_min = None
key_max = None
dbts = []
total_dbt = 0

def mean(x, y):
    
    """ To calculate mean:
    input 
    - total daily temperatures 
    - numbers of record (len of list of daily temperatures)
    output
    - mean
    """
    
    average = x / y
    return average


def middle(L):
    
    """ To calculate median:
    input
    - list of daily temperatures
    - len of the list
    output
    - index number of middle value of item in the list
    - median
    """
    
    L = sorted(L)
    a = len(L)/2
    n = int(a)
    index = L[n]
    return index
       

def variance(val, mean):
    
    """ To calculate variance:
    input:
    - mean
    - median
    - list of daily temperatures
    output:
    - variance
    """
   
    average = mean
    a = []
    for i in val:
        a.append((int(i) - average) ** 2)
    return sum(a) / len(a)


for line in sys.stdin:
    word = line.split(' ')
    
# To store each value in different variables
    try:
        date = word[0]
        temperature = word[1]
        count = int(word[2])
        dbt = int(temperature)
    except ValueError:
        continue

# To find total count and number of daily records
# To parse variables to customed function to calculate statistical values

    if date == current_date:
        counter += count  
        total_dbt += int(word[1])
        dbts.append(temperature)
        total = len(dbts)

    else:
        if current_date:
            print("Date:",current_date)
            print("\n")
            #print(total)
            avg = mean(total_dbt, total)
            print("Mean daily temperature:",avg)
            print("\n")
            var = variance(dbts, avg)
            mid = middle(dbts)
            print("Median daily temperature:",mid)
            print("\n")
            print("Variance daily temperature:",var)
            print("\n")

        current_date = date
        counter = count

# To find daily maximum temperature

    if key_max and key_max != date:
        print('%s\t%s' % ("Daily maximum temperature:", cur_max_val))
        print("\n")
        #print(cur_max_val)
        (key_max, cur_max_val) = (date, float(temperature))
    else:
        (key_max, cur_max_val) = (date, max(cur_max_val, float(temperature)))
        
# To find daily minimum temperature 
    if key_min and key_min != date:
        print('%s\t%s' % ("Daily minimum temperature:", cur_min_val))
        print("\n")
        print("Next day :)")
        print("\n")
        (key_min, cur_min_val) = (date, float(temperature))

    else:
        (key_min, cur_min_val) = (date, min(cur_min_val, float(temperature)))
          
# To print last day of the month

if date:
    print("Date:",current_date)
    print("\n")
    print("Mean daily temperature:",avg)
    print("\n")
    print("Median daily temperature:",mid)
    print("\n")
    print("Variance of daily temperature:",var)
    print("\n")
    print("Daily maximum temperature:",cur_max_val)
    print("\n")
    print("Daily minimum temperature",cur_min_val)
    
    
    
    
    