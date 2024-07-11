def are_anagrams(word1, word2):
    cleaned_word1 = ''.join(word1.lower().split())
    cleaned_word2 = ''.join(word2.lower().split())

    return sorted(cleaned_word1) == sorted(cleaned_word2)

word1 = input("İlk kelimeyi girin: ")
word2 = input("İkinci kelimeyi girin: ")
if are_anagrams(word1, word2):
    print("Kelimeler anagramdır.")
else:
    print("Kelimeler anagram değildir.")
