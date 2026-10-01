# Hill Climbing Algorithm

def objective(x):
    return -(x ** 2) + 3


def generate_neighbors(x, step_size):
    return [x + step_size, x - step_size]


def hill_climbing(initial, iterations, step_size):
    current = initial

    for i in range(iterations):

        neighbors = generate_neighbors(current, step_size)

        # Find the best neighbor
        best_neighbor = max(neighbors, key=objective)

        # Check if neighbor is better
        if objective(best_neighbor) > objective(current):
            current = best_neighbor

            print(
                f"Step {i + 1}: "
                f"x = {current:.4f}, "
                f"f(x) = {objective(current):.4f}"
            )
        else:
            print("No better neighbors found. Algorithm converged.")
            break

    return current, objective(current)


# Input
initial = float(input("Enter your initial guess: "))
iterations = int(input("Enter maximum iterations: "))
step_size = float(input("Enter step size: "))

# Run Hill Climbing
solution, value = hill_climbing(
    initial, iterations, step_size
)

# Result
print("\nBest solution x =", round(solution, 4))
print("Best value f(x) =", round(value, 4))