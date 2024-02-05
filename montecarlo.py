import random
import math

def monte_carlo_pi_simulation(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate

# Number of random points to generate
num_samples = 100000

estimated_pi = monte_carlo_pi_simulation(num_samples)

print(f"Estimated value of Pi using {num_samples} samples: {estimated_pi}")