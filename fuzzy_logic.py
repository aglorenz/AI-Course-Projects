import numpy as np 
import skfuzzy as fuzz

# input variables
x = np.arange(0, 11, 1)  # Input range from 0 to 10
print(x)

# Define fuzzy sets for the input variable
low = fuzz.trimf(x, [0,0,5])  # Triangular fuzzy set for low values
medium  = fuzz.trimf(x, [2,5,8])  # Triangular fuzzy set for medium values 
high = fuzz.trimf(x, [5,10,10]) # Triangular fuzzy set for high values
custom = fuzz.trimf(x, [3,6,9]) # Triangular fuzzy set for custom values
print(low)
print(medium)
# print(high)
# print (custom)

# Define fuzzy rules
rule1 = np.fmax(low, medium) # Rule: If input is low or medium, then output is high
rule2 = np.fmin(medium, high) # Rule: If input is medium or high, then output is low
rule3 = np.fmax(low, custom)
print(rule1)

# Apply fuzzy rules to determine the fuzzy relation between input and output
relation = np.fmax(rule1, rule2)
newRelation = np.fmax(relation,rule3)

# Defuzzify the relation to obtain a crisp output
output = fuzz.defuzz(x, newRelation, 'centroid')

# Display the crisp output
print("Output:", output)

