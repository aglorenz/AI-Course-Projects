# function to minimize
def function(x):
    return x**2 + 5*x + 6

# derivative of the function
def derivative (x):
    return 2*x + 5

# initial guess
x = 0

learning_rate = .6

num_iterations = 20

for _ in range(num_iterations):
    gradient = derivative(x)
    x = x - learning_rate * gradient

print ("The minimum value found at x = ", x)

