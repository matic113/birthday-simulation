# Birthday Problem: Simulation & Paradox

## Abstract 🧐

The "Birthday Problem" (or Birthday Paradox) explores a surprisingly counterintuitive statistical phenomenon: in a group of people, what's the minimum number needed such that there's a greater than 50% chance that at least two individuals share the same birthday? This project provides a Python-based exploration, demonstrating that this number is much smaller than many initially expect—just 23 people! The script simulates this scenario, calculates the theoretical probabilities, and visualizes the results.

---
## Project Overview 💻

This Python script offers a hands-on way to understand the Birthday Problem by:

* **Simulating** the scenario using a Monte Carlo method to empirically estimate the probabilities.
* **Calculating** the exact theoretical probabilities for comparison.
* **Plotting** both simulated and theoretical results on a single graph.
* **Highlighting** the critical point where the probability of a shared birthday surpasses 50%.

---
## How the Code Works ⚙️

The script is primarily built around three functions:

1.  `simulate_birthday_problem(trials, group_size_limit)`: Runs random birthday assignments for various group sizes over many trials to find the empirical probability of shared birthdays.
2.  `calculate_theoretical_probabilites(group_size_limit)`: Computes the exact mathematical probability of at least one shared birthday for each group size using the complementary probability (1 - P(all birthdays are different)).
3.  `main()`: Orchestrates the simulation and theoretical calculations, then uses Matplotlib to generate a comparative plot, annotating the 50% threshold.

---
## Requirements 🛠️

* Python 3.x
* NumPy (`pip install numpy`)
* Matplotlib (`pip install matplotlib`)

---
## How to Run 🚀

1.  Save the code as a Python file (e.g., `birthday_paradox.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Execute the script:
    ```bash
    python main.py
    ```

---
## Expected Output 📊

Running the script will display a Matplotlib window showing a plot with:
* The number of people in a group on the x-axis.
* The probability of at least two people sharing a birthday on the y-axis.
* Lines representing both the simulated and theoretical probabilities.
* Annotations indicating when the 50% probability mark is crossed.

---
## Resources 📚

For a deeper dive into the Birthday Paradox and related concepts:

* **My Notion Page:** [Simulation: Birthday Paradox](https://bow-pantydraco-859.notion.site/Simulation-Birthday-Paradox-1e1185ce01ea8043a818e0ad1138f9f6) - Detailed notes and exploration of this project.
* **Videos:**
    * [Hash Collisions & The Birthday Paradox - Computerphile](https://youtu.be/jsraR-el8_o?si=PTCXqGxBu6QZjy01)
    * [The Birthday Paradox - Vsauce](https://youtu.be/ofTb57aZHZs?si=e1SzX_0xYjWyK1U_)
