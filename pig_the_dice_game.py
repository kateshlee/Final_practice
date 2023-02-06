import random

def game_start(player):
    players = []
    computer = 0
    while True:
        player = int(input('플레이어 수를 입력해주세요(플레이어는 최소 1명부터 최대 3명까지 가능합니다.): '))
        if player < 4 and player >= 1:
            break
        else:
            print('플레이어 수를 정확히 입력해주세요.')
    for i in range(player):
        players[i] = 'player' + str(i)
    computer = 'computer'

    turn(players, computer)

def trun(players, computer):
    player_score = []
    computer_score = 0
    Break = False
    while True:
        for i in range(len(players)):
            player_score[i] = roll_stop()
            if player_score[i] >= 100:
                print(f'player{i+1} win')
                Break = True
                break
        if Break == True:
            break
        computer_score = roll_stop()
        if computer_score >= 100:
            print('computer win')
            break

def roll_stop():
    while True:
        dice = random.randrange(1,7)
        if dice == 1:
            return 0
        else:
            total_score += dice
