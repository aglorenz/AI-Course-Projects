# Train a linear regression model
model = lm(mpg ~ hp, data = mtcars)

# Create a new car data from with 150 horsepower
new_car = data.frame(hp = 150)

# Predict the mpg for the new car
predicted_mpg = predict(model, newdata = new_car)

# Print the predicted mpg
cat("The predicted MPG for a car with 150 horsepower is: ", predicted_mpg)
