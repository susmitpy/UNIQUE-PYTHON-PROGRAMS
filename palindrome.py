def is_palin():
    word = input("Enter the word: ")
    old_word = word.lower()
    new_list = []
    for i in range(1, len(old_word) + 1):
        new_list.append(old_word[-(i)])
    new_word = ''.join(new_list)
    if old_word == new_word:
        print("The Word Is A Palindrome")
    else:
        print("The Word Is Not A Palindrome")
while True:
    is_palin()
