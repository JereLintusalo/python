def palindromi(sana):
    return sana == sana[::-1]
    
mj = input("Anna merkkijono: ")
if palindromi(mj):
    print("Merkkijono on palindromi!")
else:
    print("Merkkijono ei ole palindromi")
