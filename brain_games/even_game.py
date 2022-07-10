import prompt
import random


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num_of_correct_answers = 0
    num_of_wrong_answers = 0
    while num_of_correct_answers < 3 and num_of_wrong_answers == 0:
        guess_num = random.randint(1,100)
        print('Question:', guess_num)
        answer = prompt.string('Your answer: ')
        if guess_num % 2 == 0:
            if answer == 'yes':
                num_of_correct_answers += 1
                print('Correct!')
            else:
                num_of_wrong_answers += 1
                print('Answer "no" is wrong, correct answer is "yes"')
                print('Let\'s try again')
        else:
            if answer == 'no':
                num_of_correct_answers +=1
                print('Correct!')
            else:
                num_of_wrong_answers +=1
                print('Answer "yes" is wrong, correct answer is "no"' )
                print('Let\'s try again')

    if num_of_correct_answers == 3:
        print('Congratulations!')

