import matplotlib.pyplot as plt
import numpy as np


def simulate_birthday_problem(trials=10000, group_size_limit=60):
    probabilities = []
    group_sizes = []

    for group_size in range(1, group_size_limit + 1):
        successful_trials_count = 0
        for _ in range(trials):
            # choose a random day for each person in the group
            # assuming each birhday is equally likely
            people = np.random.randint(1, 366, group_size)
            distinct_birthdays = np.unique(people)

            # If the number of distinct birthdays is less than the total group size,
            # it means at least one shared birthday exists in this group.
            if len(distinct_birthdays) < group_size:
                successful_trials_count += 1

        probability = successful_trials_count / trials
        probabilities.append(probability)
        group_sizes.append(group_size)

    return group_sizes, probabilities


def calculate_theoretical_probabilites(group_size_limit=60):
    theoretical_probabilities = []
    group_sizes_theoretical = []

    for n in range(1, group_size_limit + 1):
        if n > 365:  # If more people than days, probability of a shared birthday is 1
            prob_no_shared_birthday = 0.0
        else:
            # Calculate P(all birthdays are different)
            # P = (365/365) * (364/365) * (363/365) * ... * ((365-n+1)/365)
            prob_no_shared_birthday = 1.0
            for i in range(n):
                prob_no_shared_birthday *= (365.0 - i) / 365.0

        # Probability of at least one shared birthday is 1 - P(all birthdays are different)
        prob_at_least_one_shared = 1.0 - prob_no_shared_birthday
        theoretical_probabilities.append(prob_at_least_one_shared)
        group_sizes_theoretical.append(n)

    return group_sizes_theoretical, theoretical_probabilities


def main():
    group_size = 50
    simulation_trials = 10000

    # statistical trials
    group_sizes_sim, probabilities_sim = simulate_birthday_problem(
        trials=simulation_trials, group_size_limit=group_size
    )

    # theoretical calculation
    group_sizes_th, probabilities_th = calculate_theoretical_probabilites(group_size)

    plt.figure(figsize=(10, 7))

    # plot simulated values
    plt.plot(
        group_sizes_sim,
        probabilities_sim,
        label="Simulated Probability",
        marker="o",
        linestyle="--",
    )

    # plot theoretical values
    plt.plot(
        group_sizes_th,
        probabilities_th,
        label="Theoretical Probability",
        marker="x",
        linestyle="-",
    )

    plt.xlabel("Number of people")
    plt.ylabel("Probability at least 2 share birthday")
    plt.title("Birthday Problem: Simulated vs. Theoretical Probability")

    plt.grid(True)  # Add a grid for easier reading
    # 1.1 because arange(stop) is not inclusive
    plt.yticks(np.arange(0, 1.1, 0.1))  # Set y-axis ticks at 0.1 intervals
    # group_size + 5 because arange(stop) is not inclusive
    plt.xticks(np.arange(0, group_size + 5, 5))  # Set x-axis ticks at 5 intervals
    plt.legend()  # Add a legend to distinguish the lines

    sim_crossed_50 = False
    for i, prob_sim in enumerate(probabilities_sim):
        if prob_sim >= 0.5 and not sim_crossed_50:
            n_sim_cross = group_sizes_sim[i]
            p_sim_cross = probabilities_sim[i]

            # Add vertical and horizontal lines
            plt.axvline(
                x=n_sim_cross,
                color="dodgerblue",
                linestyle=":",
                linewidth=1.5,
                alpha=0.8,
            )
            plt.axhline(
                y=p_sim_cross,
                color="dodgerblue",
                linestyle=":",
                linewidth=1.5,
                alpha=0.8,
            )

            # Annotation text
            text_label = f"Simulated ≥ 50%\nat n={n_sim_cross} (P≈{p_sim_cross:.2f})"

            # Position the text always below the 0.5 mark
            x_offset = 1
            y_position = 0.5 - 0.03

            plt.text(
                n_sim_cross + x_offset,
                y_position,
                text_label,
                color="navy",
                fontsize=9,
                bbox=dict(
                    facecolor="white",
                    alpha=0.7,
                    edgecolor="lightgrey",
                    boxstyle="round,pad=0.3",
                ),
                verticalalignment="top",  # Align text box's top to y_position
                horizontalalignment="left",
            )

            sim_crossed_50 = True  # Ensure we only mark the first crossing
            break  # Exit loop once the first crossing is found and marked

    plt.show()


if __name__ == "__main__":
    main()
