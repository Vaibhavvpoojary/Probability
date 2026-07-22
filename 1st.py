# Program to demonstrate basic probability notation and concepts

# 1. Sample Space (Ω) and Outcomes
# The sample space is the set of all possible outcomes of our experiment.
# Here, the experiment is rolling a single fair six-sided die.
sample_space = {1, 2, 3, 4, 5, 6}


def calculate_probability(event, sample_space):
    """Calculates P(E), the probability of an event occurring."""
    # Ensure the event only contains valid outcomes from the sample space
    valid_event_outcomes = event.intersection(sample_space)

    # Formula: P(E) = Count of favorable outcomes / Total possible outcomes
    probability_value = len(valid_event_outcomes) / len(sample_space)
    return probability_value

   
# 2. Defining Events
# An event is a subset of the sample space (a collection of specific outcomes).
event_A = {3}  # Event A: Rolling exactly a 3
event_B = {2, 4, 6}  # Event B: Rolling an even number
event_C = {1, 2}  # Event C: Rolling a number less than 3
event_D = {1, 2, 3, 4, 5, 6}  # Event D: Rolling any number (Certain Event)
event_E = set()  # Event E: Rolling a 7 (Impossible Event)

# 3. Calculating and Displaying Probability Values
print("--- Basic Probability Demonstrations ---")
print(f"Sample Space (Ω): {sample_space}")
print(f"Total Number of Outcomes |Ω|: {len(sample_space)}\n")

# Scenario 1: Single Outcome
prob_A = calculate_probability(event_A, sample_space)
print(f"Event A (Rolling a 3): {event_A}")
print(f"Notation: P(A) = {prob_A:.4f} (or {prob_A * 100:.1f}%)\n")

# Scenario 2: Multiple Outcomes
prob_B = calculate_probability(event_B, sample_space)
print(f"Event B (Rolling an even number): {event_B}")
print(f"Notation: P(B) = {prob_B:.4f} (or {prob_B * 100:.1f}%)\n")

# Scenario 3: Bound Check (Certain vs Impossible)
prob_D = calculate_probability(event_D, sample_space)
prob_E = calculate_probability(event_E, sample_space)
print(f"Event D (Certain Event - Rolling 1-6): {event_D} -> P(D) = {prob_D}")
print(
    f"Event E (Impossible Event - Rolling a 7): {event_E} -> P(E) = {prob_E}"
)
