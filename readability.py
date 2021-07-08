#! python3
# Author: JGSnyder
# Date: 04 June 2020
# Use Coleman-Liau formula to compute grade level for submitted text

def main():
    text = input("Text: ")

    letters, words, sentences = count_text(text)

    # L is the average number of letters per 100 words
    # S is the average number of sentences per 100 words
    L = 100 * letters / words
    S = 100 * sentences / words

    gradelevel = round(.0588 * L - .296 * S - 15.8)

    if gradelevel < 1:
        print("Before Grade 1")
    elif gradelevel >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {gradelevel}")


def count_text(text):
    letters = 0
    words = 1 # accounts for lack of space at end of sentence
    sentences = 0
    for i in range(len(text)):
        if text[i].isalpha():
            letters += 1
        elif text[i] == " ":
            words += 1
        elif text[i] in "?.!":
            sentences += 1
    return letters, words, sentences

main()