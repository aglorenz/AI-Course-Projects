# Load required libraries
library(e1071)

# Load the iris dataset
data(iris)

# Preprocessing: Splitting the dataset into features and target variable
features = iris[, -5]  # Exclude the species column
target = iris$Species

# Train a Naive Bayes classifier
nb_model = naiveBayes(features, target)

# Create new data for prediction (example)
new_data = data.frame(
  Sepal.Length = 5.1,
  Sepal.Width = 3.5,
  Petal.Length = 1.4,
  Petal.Width = 0.2
)

# Make a prediction using the trained model
prediction = predict(nb_model, new_data)

# Print the predicted category
print(prediction)