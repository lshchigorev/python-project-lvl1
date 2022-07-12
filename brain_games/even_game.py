import prompt
import random

NUM_OF_CORR_ANSW  = 3
MIN_RAND = 1
MAX_RAND = 100
def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num_of_correct_answers = 0
    num_of_wrong_answers = 0
    while num_of_correct_answers < NUM_OF_CORR_ANSW and num_of_wrong_answers == 0:
        guess_num = random.randint(MIN_RAND,MAX_RAND)
        print('Question:', guess_num)
        answer = prompt.string('Your answer: ')
        if guess_num % 2 == 0:
            if answer == 'yes':
                num_of_correct_answers = incr_num_of_corr_answ(num_of_correct_answers)
            else:
                num_of_wrong_answers = incr_num_of_wrong_answ(num_of_wrong_answers, 'yes', answer)
        else:
            if answer == 'no':
                num_of_correct_answers = incr_num_of_corr_answ(num_of_correct_answers)
            else:
                num_of_wrong_answers = incr_num_of_wrong_answ(num_of_wrong_answers, 'no', answer)

    if num_of_correct_answers == NUM_OF_CORR_ANSW:
        print('Congratulations!')

def incr_num_of_corr_answ(num_of_corr_answ):
    print('Correct!')
    num_of_corr_answ += 1
    return num_of_corr_answ

def incr_num_of_wrong_answ(num_of_wr_answ, corr_answ, user_answ):
    print('Answer',user_answ,' is wrong, correct answer is', corr_answ)
    print('Let\'s try again')
    num_of_wr_answ += 1
    return num_of_wr_answ