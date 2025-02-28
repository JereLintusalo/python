numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

# Suodatetaan validit numerot listaan
valid_numbers = [num for num in numbers if 0 <= num <= 100]

#Lasketaan summa ja keskiarvo
summa = sum(valid_numbers)
keskiarvo = summa / len(valid_numbers) if valid_numbers else 0 #Varmistaa ettei jaa nollalla

print(f"Validit numerot: {valid_numbers}")
print(f"Summa on {summa}")
print(f"Keskiarvo on: {keskiarvo:.2f}")