while True:
    word1 = input("Welcome to my new first Projeckt! Please enter you  ('exit!')")
    if word1 == 'exit':
        print('Welcome!')
        #break
    word = input('Enter a word in Latin or Cyrillic!')


    vowels = 'aeioaeёиоуыэюяuoaiyAEUYAIАОЮУЫЭЯ'
    consonants = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщBCDFGHJKLMNPSTVWXYZБВГДЖЗЙКЛМНРСТФХЦЧШЩ'

    word_length = len(word)
    vowel_count = 0
    consonant_count = 0

    for letter in word:
        if letter in vowels:
            vowel_count += 1
        elif letter in consonants:
            consonant_count += 1

    total_count = vowel_count + consonant_count
    vowel_precent = round((vowel_count / total_count) * 100,2)
    consonant_precent = round((consonant_count / total_count) * 100,2)

    print(f'Number of letters in a word {word_length}')
    print(f'Number of consonants {consonant_count}')
    print(f'Number of vowels {vowel_count}')
    print(f'Percentage of vowels {vowel_precent}%')
    print(f'Percentage of consonants {consonant_precent}%')
    choice = input("Do you want to continue?? (y/n)").lower()
    if choice == 'n':
        break