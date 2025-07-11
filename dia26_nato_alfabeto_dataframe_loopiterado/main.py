import pandas
nato = pandas.read_csv('nato_phonetic_alphabet.csv')

translate_this = input("ENTER YOUR TRANSLATION HERE").upper()
translate_this_sliced = [n for n in translate_this]

nato_text2 = {row['letter']: row['code'] for index, row in nato.iterrows()}

nato_translated = [nato_text2.get(letra) for letra in translate_this_sliced]

print(nato_translated)

'''
nato_translated =[nato_text2[n] for n in translate_this_sliced if n == nato_text2[n].iloc[0]]
print(nato_translated)
'''




