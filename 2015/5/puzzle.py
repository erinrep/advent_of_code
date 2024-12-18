print("Day 5: Doesn't He Have Intern-Elves For This?")

import re

strings = [
    "ugknbfddgicrmopn",
    "aaa",
    "jchzalrnumimnmhp",
    "haegwjzuvuyypxyu",
    "dvszwmarrgswjxmb",
]
numNice = 0
for s in strings:
    threeVowels = re.search(r"([aeiou].*){3}", s)
    doubleLetter = re.search(r"(\w)\1", s)
    forbidden = re.search(r"ab|cd|pq|xy", s)
    if threeVowels and doubleLetter and not forbidden:
        numNice += 1

print("Part 1:", numNice)

strings = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]
numNice = 0
for s in strings:
    pairTwice = re.search(r"(\w)(\w).*\1\2", s)
    sandwich = re.search(r"(\w).{1}\1", s)
    if pairTwice and sandwich:
        numNice += 1

print("Part 2:", numNice)
