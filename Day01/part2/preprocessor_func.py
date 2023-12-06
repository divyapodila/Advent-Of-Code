##two1nine6znb1
## break this into [2 , 1 , 9 , 6 , 1]
import re


def preprocessing(line_numbers):
    dictionary = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    matches = []
    for word, repl in dictionary.items():
        match = re.search(word, line_numbers)
        matches += [
            (word, match.start(), word[0]) for match in re.finditer(word, line_numbers)
        ]
        sorted_matches = sorted(matches, key=lambda x: x[1], reverse=True)
    for match in sorted_matches:
        line_numbers = line_numbers[: match[1]] + match[2] + line_numbers[match[1] :]
    for word, repl in dictionary.items():
        line_numbers = line_numbers.replace(word, repl)
    print(line_numbers)

    return line_numbers
