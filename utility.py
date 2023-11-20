import random

def generate_utility_metric(utility_type):
    # Generate a random number based on the specified utility type
    if utility_type == "gas":
        metric = random.uniform(5, 20)  # You can customize the range for gas usage
    elif utility_type == "electricity":
        metric = random.uniform(50, 200)  # You can customize the range for electricity usage
    elif utility_type == "water":
        metric = random.uniform(10, 50)  # You can customize the range for water usage
    else:
        raise ValueError("Invalid utility type. Please choose 'gas', 'electricity', or 'water'.")

    return metric

def main():
    # Get user input for utility type
    utility_type = input("Enter utility type (gas, electricity, or water): ").lower()

    # Generate utility metric
    utility_metric = generate_utility_metric(utility_type)

    # Display the result
    print(f"Utility Metric for {utility_type.capitalize()}: {utility_metric}")

if __name__ == "__main__":
    main()