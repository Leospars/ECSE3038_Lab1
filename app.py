# Question 1
def parallel(resistors: list[int | float]) -> float:
    sum = 0
    for resistor in resistors:
        sum = sum + (1/resistor)
    resistance = 1/sum
    return resistance

resistance = parallel([330, 1000, 2200])
print(f"Resistance: {resistance:.2f} Ohms")
