import pandas as pd

# Read the CSV file into a DataFrame
phonetic_code = pd.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary mapping letters to their phonetic code words
phonetic_dict = {row.letter: row.code_word for (index, row) in phonetic_code.iterrows()}

# Print the dictionary
print(phonetic_dict)

# Get a word from the user
word = input("Enter a word: ").upper()

# Convert the word to a list of its letters' phonetic code words
phonetic_words = [phonetic_dict[letter] for letter in word if letter in phonetic_dict]

# Print the list of phonetic code words
print(phonetic_words)