# Naive Bayes Algorithm without sklearn

from math import sqrt, pi, exp


# Calculate mean
def mean(values):
    return sum(values) / len(values)


# Calculate standard deviation
def standard_deviation(values):
    avg = mean(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return sqrt(variance)


# Calculate Gaussian probability
def probability(x, mean_value, std):
    if std == 0:
        return 1 if x == mean_value else 0

    exponent = exp(-((x - mean_value) ** 2) / (2 * std ** 2))

    return (1 / (sqrt(2 * pi) * std)) * exponent


# Training data
X = [
    [1, 20],
    [2, 21],
    [3, 22],
    [6, 30],
    [7, 31],
    [8, 32]
]

Y = [
    "No",
    "No",
    "No",
    "Yes",
    "Yes",
    "Yes"
]


# Separate data according to class
data = {}

for i in range(len(Y)):
    class_name = Y[i]

    if class_name not in data:
        data[class_name] = []

    data[class_name].append(X[i])


# Calculate mean and standard deviation
statistics = {}

for class_name in data:
    statistics[class_name] = []

    for column in range(len(X[0])):
        values = [row[column] for row in data[class_name]]

        statistics[class_name].append(
            (mean(values), standard_deviation(values))
        )


# Predict function
def predict(test_data):

    probabilities = {}

    for class_name in statistics:

        # Prior probability
        prior = len(data[class_name]) / len(X)

        probability_value = prior

        for i in range(len(test_data)):
            avg, std = statistics[class_name][i]

            probability_value *= probability(
                test_data[i], avg, std
            )

        probabilities[class_name] = probability_value

    return max(probabilities, key=probabilities.get)


# Test data
test_data = [
    [4, 23],
    [7, 30]
]


# Prediction
for test in test_data:
    result = predict(test)

    print("Test Data:", test)
    print("Predicted Class:", result)
    print()