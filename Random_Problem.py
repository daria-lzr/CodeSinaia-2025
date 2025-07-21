import random

def generate_dataset(count, min_value, max_value, filename="dataset.txt"):
    # Dicționar pentru a salva valorile unice și lista iterațiilor în care apar
    value_iterations = {}

    for i in range(count):
        value = random.randint(min_value, max_value)
        if value not in value_iterations:
            value_iterations[value] = []
        value_iterations[value].append(i)

    # Scrierea în fișier
    with open(filename, "w") as file:
        for value, iterations in value_iterations.items():
            iterations_str = ", ".join(str(it) for it in iterations)
            file.write(f"{value}: {iterations_str}\n")
            

generate_dataset(count=10, min_value=3, max_value=13)
