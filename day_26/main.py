import pandas
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# while True:
#     try:
#         user_name = input("Enter your name: ").upper()
#         if not user_name.isalpha():
#             raise KeyError
#     except KeyError:
#         print("Sorry. Only letters are allowed.")
#     else:
#         break


# for letter in user_name:
#     # print(data_frame[data_frame.letter == letter])
#     letter_word = data_frame[data_frame.letter == letter.upper()].code.item()
#     word_list.append(letter_word)

phonetic_dict = {row.letter: row.code for index, row in data_frame.iterrows()}


def generate_phonetic():
    user_name = input("Enter your name: ").upper()
    try:
        word_list = [phonetic_dict[letter] for letter in user_name]
    except KeyError:
        print("Sorry. Only letters are allowed.")
        generate_phonetic()
    else:
        print(word_list)

generate_phonetic()