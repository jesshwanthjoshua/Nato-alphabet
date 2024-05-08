import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
# nato_dict = nato.to_dict()
# print(nato_dict)

phonetic_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
print(phonetic_dict)

user_name = input("What is your name?: ").upper()

# phonetic_list = [row.code for letter in user_name for (index, row) in nato.iterrows() if row.letter == letter]
phonetic_list_with_order = [phonetic_dict[letter] for letter in user_name ]

print(f"Phonetic List by order: {phonetic_list_with_order}")
