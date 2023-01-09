# # #
import sqlite3
from random import randint

USER_NAME = "NoName"
COUNT_WORDS = 10
words_number_list = []
lesson_words_list = []


def greeting_app():
    global USER_NAME
    user_name = input("Введите имя пользователя:   ").strip().upper()
    if len(user_name) > 1 or user_name != " ":
        USER_NAME = user_name
    else:
        pass

    return USER_NAME


def count_round_words():
    global COUNT_WORDS
    print(f"Привет {USER_NAME}!")
    count_word = input("Введите количество слов для тренировки:   ").strip()
    if int(count_word) > 0 or count_word != "":
        cw = int(count_word)
        COUNT_WORDS = cw

    return COUNT_WORDS


def make_words_number_list():
    global words_number_list
    for i in range(COUNT_WORDS + 1):
        word_number = randint(1, 5001)
        words_number_list.append(word_number)

    return words_number_list


def make_lesson_words_list():
    global words_number_list, lesson_words_list
    connection = sqlite3.connect('words_base/cosmic_platform.db')
    cursor = connection.cursor()
    for words_number in words_number_list:
        with connection:
            lesson_word = cursor.execute("""SELECT * FROM '5000words_in_english' WHERE words_number = ?""",
                                         (words_number,)).fetchall()
            english_word = lesson_word[0][1]
            russian_word = lesson_word[0][2]
            line_words = (english_word, russian_word)
            lesson_words_list.append(line_words)
    return lesson_words_list


def next_step():
    nxt = input("Далее ENTER ✅")


def one_round_lesson():
    global lesson_words_list
    for num, lesson_word in enumerate(lesson_words_list):
        print(f"{num + 1}. {lesson_word[0]} переводится как {lesson_word[1]}.")
        next_step()
    print(f"Вы узнали {len(lesson_words_list)} новых слов, далее небольшой тест 😉")


def testing_game():
    global lesson_words_list


def main():
    greeting_app()
    count_round_words()
    make_words_number_list()
    make_lesson_words_list()
    one_round_lesson()


if __name__ == '__main__':
    main()

