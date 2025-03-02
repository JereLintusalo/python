# Budget Tracker App - Budjettiseurantasovellus
import json  # JSON-tiedostojen käsittelyyn


def add_expense(expenses, description, amount):
    # Lisää uuden kulun kululistaan.
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount}")


def get_total_expenses(expenses):
    # Laskee kaikkien kulujen yhteissumman.
    total = sum(expense["amount"] for expense in expenses)  # Käytetään sum() helpottamaan laskentaa
    return total


def get_balance(budget, expenses):
    # Laskee, kuinka paljon budjetista on jäljellä.
    return budget - get_total_expenses(expenses)


def show_budget_details(budget, expenses):
    # Näyttää budjetin tiedot, kaikki kulut ja jäljellä olevan summan.
    print(f"\nTotal Budget: {budget}")
    print("Expenses: ")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"Total Spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")


def load_budget_data(filepath):
    # Lataa budjetin ja kulut JSON-tiedostosta.
    # Jos tiedostoa ei löydy tai se on virheellinen, palautetaan oletusarvot.
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []  # Palautetaan oletusarvot, jos tiedostoa ei ole tai se on tyhjä/viallinen


def save_budget_details(filepath, initial_budget, expenses):
    # Tallentaa budjetin ja kulut JSON-tiedostoon.
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    # Sovelluksen pääfunktio, jossa käyttäjä voi lisätä kuluja,
    # tarkastella budjettia ja lopettaa ohjelman.
    print("Welcome to the Budget App")
    filepath = 'budget_data.json'
    
    # Ladataan tallennettu budjetti ja kulutiedot
    initial_budget, expenses = load_budget_data(filepath)
    
    # Jos budjettia ei ole aiemmin asetettu, kysytään käyttäjältä
    if initial_budget == 0:
        initial_budget = float(input("Please enter your initial budget: "))
    
    budget = initial_budget  # Määritetään budjetti aloitusarvosta

    while True:
        # Näytetään valikko käyttäjälle
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            # Pyydetään käyttäjää lisäämään kulu
            description = input("Enter expense description: ")
            try:
                amount = float(input("Enter expense amount: "))
                add_expense(expenses, description, amount)
            except ValueError:
                print("Invalid amount! Please enter a number.")
        elif choice == "2":
            # Näytetään budjetin ja kulujen tiedot
            show_budget_details(budget, expenses)
        elif choice == "3":
            # Tallennetaan tiedot ja lopetetaan ohjelma
            save_budget_details(filepath, initial_budget, expenses)
            print("Exiting Budget App. Goodbye!")
            break
        else:
            print("Invalid choice, please choose again!")  # Virheellisen syötteen käsittely


# Suoritetaan pääohjelma vain, jos tiedosto ajetaan suoraan
if __name__ == "__main__":
    main()
