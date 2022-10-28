from random import sample
import art
from game_data import data


continue_game = True
score = 0
while continue_game:
    print('\n' * 50)
    people = sample(range(0, 15), 2)
    person_a = data[people[0]]
    person_b = data[people[1]]

    print(art.logo)
    if score > 0:
        print(f'Scoreboard: {score}')

    print(f'Compare A: {person_a["name"]}, a {person_a["description"]}, from {person_a["country"]}')
    person_a_follower_count = person_a["follower_count"]

    print(art.vs)

    print(f'Against B: {person_b["name"]}, a {person_b["description"]}, from {person_b["country"]}')
    person_b_follower_count = person_b["follower_count"]

    guess = input('\nWho has more followers? Type \"A\" or \"B\": ').upper()

    if guess != 'A' and guess != 'B':
        print('Error, that isn`t an valid option')
    else:
        if guess == 'A' and person_a_follower_count > person_b_follower_count:
            score += 1
        elif guess == 'B' and person_a_follower_count < person_b_follower_count:
            score += 1
        else:
            print('\n' * 50)
            print('You lose!')
            print(f'Final score: {score}')
            continue_game = False
