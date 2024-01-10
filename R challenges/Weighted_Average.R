# List of numbers
numbers = c(1, 2, 4, 33, 40)
# Weights for the number list
weights = c(.8, .9, .2, .1, .2)

# weighted average is sum of the product of weights and numbers divided by the sum of weights
weighted_sum = sum(numbers * weights)
weighted_average = weighted_sum / sum(weights)

# use built in method for weighted_average
alt_weighted_average = weighted.mean(numbers, weights)

cat("The weighted average the hard way is: ", weighted_average,
"\nThe weighted average the easy way is: ", alt_weighted_average)
