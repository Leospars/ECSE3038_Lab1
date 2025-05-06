# Question 1
def parallel(resistors: list[int | float]) -> float:
    sum = 0
    for resistor in resistors:
        sum = sum + (1/resistor)
    resistance = 1/sum
    return resistance

resistance = parallel([330, 1000, 2200])
print(f"Resistance: {resistance:.2f} Ohms")

# Question 2
def potential_divider(voltage, resistors: list[int | float]) -> list[float]:
    vdrops = []
    rtotal = sum(resistors)
    for res in resistors:
        vdrops.append(voltage * (res/ rtotal))
        print(f"V_R{vdrops.index(vdrops[-1])}: {vdrops[-1]}")
    return vdrops

potential_divider(9, [3000, 1000])

# Question 3
def temperature_check(temp: float, degrees: str) -> str:
    if degrees == "F":
        if temp < 95:
            return "the patient is hypothermic"
        elif temp > 104:
            return "the patient is hyperthermic"
        else:
            return "the patient's temperature is normal"
    elif degrees == "C":
        if temp < 35:
            return "the patient is hypothermic"
        elif temp > 40:
            return "the patient is hyperthermic"
        else:
            return "the patient's temperature is normal"
    else:
        return "Invalid input degrees must be either F or C"

temperature_check(14, "C")
temperature_check(37, "C")
temperature_check(37, "F")