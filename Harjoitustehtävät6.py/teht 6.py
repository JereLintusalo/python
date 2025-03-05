def main(mj):
    konsonantti = "qwrtpsdfghjklzxcvbnmQWRRTPSDFGHJKLZXCVBNM"
    return sum(1 for merkki in mj if merkki.isalpha() and merkki in konsonantti)

mj = input("Anna merkkijono: ")
print(f"Konsonanttien määrä: {main(mj)}")

