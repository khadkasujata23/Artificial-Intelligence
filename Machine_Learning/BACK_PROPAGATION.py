# Back Propagation Algorithm
# XOR Problem
# No external library required


import math
import random


# Sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)


# Input data
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Expected output
Y = [
    [0],
    [1],
    [1],
    [0]
]


# Initialize weights
random.seed(1)

W1 = [
    [random.uniform(-1, 1), random.uniform(-1, 1)],
    [random.uniform(-1, 1), random.uniform(-1, 1)]
]

W2 = [
    [random.uniform(-1, 1)],
    [random.uniform(-1, 1)]
]


# Bias
B1 = [0, 0]
B2 = [0]

learning_rate = 0.5


# Training
for epoch in range(10000):

    for i in range(len(X)):

        # -------------------------
        # Forward Propagation
        # -------------------------

        hidden = []

        for j in range(2):
            value = (
                X[i][0] * W1[0][j]
                + X[i][1] * W1[1][j]
                + B1[j]
            )

            hidden.append(sigmoid(value))


        output_value = (
            hidden[0] * W2[0][0]
            + hidden[1] * W2[1][0]
            + B2[0]
        )

        output = sigmoid(output_value)


        # -------------------------
        # Back Propagation
        # -------------------------

        error = Y[i][0] - output

        output_delta = error * sigmoid_derivative(output)


        hidden_delta = []

        for j in range(2):
            hidden_error = output_delta * W2[j][0]
            delta = hidden_error * sigmoid_derivative(hidden[j])
            hidden_delta.append(delta)


        # -------------------------
        # Update Weights
        # -------------------------

        for j in range(2):
            W2[j][0] += learning_rate * output_delta * hidden[j]

        B2[0] += learning_rate * output_delta


        for j in range(2):
            W1[0][j] += learning_rate * hidden_delta[j] * X[i][0]
            W1[1][j] += learning_rate * hidden_delta[j] * X[i][1]

            B1[j] += learning_rate * hidden_delta[j]


# -------------------------
# Display Results
# -------------------------

print("Expected Output:")
for value in Y:
    print(value)


print("\nPredicted Output:")

for i in range(len(X)):

    hidden = []

    for j in range(2):
        value = (
            X[i][0] * W1[0][j]
            + X[i][1] * W1[1][j]
            + B1[j]
        )

        hidden.append(sigmoid(value))


    output_value = (
        hidden[0] * W2[0][0]
        + hidden[1] * W2[1][0]
        + B2[0]
    )

    output = sigmoid(output_value)

    print([round(output)])