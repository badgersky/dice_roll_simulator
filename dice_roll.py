from random import randint


def format_dice(dice):
    """Function takes string and format it to get info about dice"""
    if '+' in dice or '-' in dice:
        operators = ['+', '-']
        for op in operators:
            if op in dice:
                dice_parts = dice.split(op)
                modifier = int(dice_parts[1])
                number_type = dice_parts[0].split('D')
                dice_number = int(number_type[0])
                dice_type = int(number_type[1])
                return dice_number, dice_type, op, modifier
    else:
        number_type = dice.split('D')
        dice_number = int(number_type[0])
        dice_type = int(number_type[1])
        return dice_number, dice_type


def roll_dice(d):
    """Function simulates dice roll"""
    dice = format_dice(d)
    if len(dice) == 2:
        result = [randint(1, dice[1]) for _ in range(dice[0])]
        return ', '.join([str(n) for n in result])
    else:
        if '+' in dice:
            result = [randint(1, dice[1]) + dice[3] for _ in range(dice[0])]
            return ', '.join([str(n) for n in result])
        elif '-' in dice:
            result = [randint(1, dice[1]) - dice[3] for _ in range(dice[0])]
            return ', '.join([str(n) for n in result])


if __name__ == '__main__':
    prompt = 'In order to stop rolling dices type Q'
    while True:
        s = input(prompt + '\nEnter your throw: ')
        if s.lower() == 'q':
            break
        else:
            try:
                print(f'Result of your roll is: ' + roll_dice(s) + '\n')
            except TypeError:
                print('Wrong input!')
            except IndexError:
                print('Wrong input!')
            except ValueError:
                print('Wrong input!')
                