counter_vowel = 0
counter_consonant = 0

user_word = input('enter word: ')
for letter in user_word:
    vowel = 'qwrtpsdfghjklzxcvbnmцкнгшщзхфвпрлджчсмтб'
    if letter in vowel:
        counter_vowel += 1
    else:
        counter_consonant += 1

sum = counter_vowel + counter_consonant
result_c = round((counter_consonant / sum) * 100, 2)
result_v = round((counter_vowel / sum) * 100, 2)

print('word:', user_word)
print('number of letters:', len(user_word))
print('consoants:', counter_consonant,
      '\nvowels:', counter_vowel)
print('consonants / vowels:\n', result_c, '% /', result_v, '%')