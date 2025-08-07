words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

vowels = ["a", "e", "i", "o", "u", "y"]


def main():
    words_tuples = []
    for word in words:
        vowel_count = sum(1 for letter in word if letter in vowels)
        word_tuple = (word, vowel_count)
        words_tuples.append(word_tuple)
    words_tuples.sort(key=lambda x: x[1], reverse=True)
    print(words_tuples)

main()