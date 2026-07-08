"""
Task 1 — Problem 8 (Medium): The Minion Game

HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem

Adapted as a function so it can be tested automatically.
"""

VOWELS = "AEIOU"


def minion_game(word: str) -> str:
    """Play the Minion Game on an uppercase word and return the result.

    Two players make substrings of `word`:
    - Kevin scores every substring that starts with a vowel (A, E, I, O, U).
    - Stuart scores every substring that starts with a consonant.

    A letter at index i in a word of length n starts (n - i) substrings.

    Return:
    - "Stuart <score>" if Stuart wins,
    - "Kevin <score>" if Kevin wins,
    - "Draw" if the scores are equal.

    Example: "BANANA" -> "Stuart 12".
    """
    stuart = 0
    kevin = 0
    i = 0
    for j in word:
        if j in VOWELS:
            kevin += (len(word)) - i
            i = i + 1
        else:
            stuart += (len(word)) - i
            i = i + 1

    if stuart > kevin:
        return f"Stuart {stuart}"
    elif stuart == kevin:
        return "Draw"
    else:
        return f"Kevin {kevin}"


if __name__ == "__main__":
    print(minion_game("BANANA"))
