# Basic Probability Notation Demonstration

A lightweight Python script that demonstrates the foundational concepts and mathematical notation of probability theory using a standard six-sided die roll.

## Core Concepts Covered

*   **Sample Space (Ω):** The set of all possible outcomes of an experiment.
*   **Outcomes:** Individual, distinct results within the sample space.
*   **Event (E):** A specific subset of outcomes from the sample space.
*   **Probability Value P(E):** The mathematical likelihood of an event occurring, bounded strictly between `0` (impossible) and `1` (certain).

## Mathematical Formula

The script calculates theoretical probability using the classical definition:

\[P(E) = \frac{\vert{}E\vert{}}{\vert{}\Omega\vert{}}\]

Where:
*   |E| is the number of favorable outcomes.
*   |Ω| is the total number of possible outcomes in the sample space.

## How to Run the Script

### Prerequisites
*   Python 3.x installed on your system.

### Execution
1. Save the code into a file named `probability_demo.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the following command:

```bash
python probability_demo.py
```

## Code Architecture

The script implements a simple, programmatic layout:
*   **`sample_space`**: Defined as a Python `set` `{1, 2, 3, 4, 5, 6}`.
*   **`calculate_probability()`**: A function that performs set intersection to ensure only valid outcomes are measured, preventing logic errors.
*   **Event Definitions**: Sets representing unique event types, including single-outcome events, multi-outcome events, certain events, and empty (impossible) events.

## Expected Output

When executed, the script will output the following clean text representation to your console:

```text
--- Basic Probability Demonstrations ---
Sample Space (Ω): {1, 2, 3, 4, 5, 6}
Total Number of Outcomes |Ω|: 6

Event A (Rolling a 3): {3}
Notation: P(A) = 0.1667 (or 16.7%)

Event B (Rolling an even number): {2, 4, 6}
Notation: P(B) = 0.5000 (or 50.0%)

Event D (Certain Event - Rolling 1-6): {1, 2, 3, 4, 5, 6} -> P(D) = 1.0
Event E (Impossible Event - Rolling a 7): set() -> P(E) = 0.0
```

## License

This project is open-source and free to use for educational purposes.
