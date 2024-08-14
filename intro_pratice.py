import pandas as pd
import numpy as np

#Variables
number_var = 42
string_var = "Bonjour, World!"
list_var = [1, 2, 3, 4, 5]
dict_var = {
        "key1": "value1",
        "key2": [1,2,3],
        "key3": {
            "nested_key1": "nested_value1",
            "nested_key2": 100
        }
}

# Function to analyze blood pressure
def analyze_blood_pressure(systolic, diastolic):
    if systolic <= 120 and diastolic <= 80:
        return "Normal Blood Pressure"
    elif systolic < 130 and diastolic < 80:
        return "Elevated Blood Pressure"
    elif systolic < 140 and diastolic <90:
        return "High Blood Pressure (Stage 1)"
    elif systolic >= 140 or diastolic >= 90:
        return "High Blood Pressure (Stage 2)"
    else: 
        return "Hypertensive Crisis"    

# Print statements
print("Number Variable:", number_var)
print("String Variable:", string_var)
print("List Variable", list_var)
print("Dictionary Variable", dict_var)

#Run the function with example data
bp_result = analyze_blood_pressure(120, 80)
print("Blood Pressure Analysis:", bp_result)
