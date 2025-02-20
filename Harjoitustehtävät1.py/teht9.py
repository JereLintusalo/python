#Harjoitus 9
laskin = input("Valitse laskutoimenpide (+ - * /): ")
num1 = float(input("Kerro eka numero: "))
num2 = float(input("Kerro toinen numero: "))

if laskin == "+":
    result = num1 + num2
    print(round(result, 3))
elif laskin == "-":
    result = num1 - num2
    print(round(result, 3))
elif laskin == "*":
    result = num1 * num2
    print(round(result, 3))
elif laskin == "/":
    result = num1 / num2 
    print(round(result, 3))