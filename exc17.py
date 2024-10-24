word: str = input("Enter a word: ")
half: int = len(word) // 2
bool_list: list[bool] = []
location: int = -1

for letter in word[:half]:
    if letter == word[location]:
        location += -1
        bool_list.append(True)
    else:
        bool_list.append(False)
if all(bool_list):
    print(f"the word: {word} is a palindrome")
else:
    print(f"the word: {word} isn't a palindrome")
