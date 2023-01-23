from collections import Counter

words = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'ДЯдя', 'брАт', 'Дядя', 'Дядя']
duplicate_words = [key for key, value in Counter(words).items() if value > 1]
words_lowercase = [word.lower() for word in words]
duplicate_words_lowercase = [word.lower() for word in duplicate_words]
words_without_duplicates = [word for word in words_lowercase if word not in duplicate_words_lowercase]
unique_words = set(words_without_duplicates)
print(words)
print(duplicate_words)
print(words_lowercase)
print(duplicate_words_lowercase)
print(words_without_duplicates)
print(result)

