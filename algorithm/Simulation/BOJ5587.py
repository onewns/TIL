import sys
sys.stdin = open("../input.txt", 'r')


def card_simulation():
    player1 = []
    player2 = []
    for i in range(2 * n):
        if player1_cards[i]:
            player1.append(i+1)
        else:
            player2.append(i+1)
    turn = True
    top = 0
    while player1 and player2:
        if turn:
            for i in range(len(player1)):
                if player1[i] > top:
                    top = player1.pop(i)
                    break
            else:
                top = 0
            turn = not turn
        else:
            for i in range(len(player2)):
                if player2[i] > top:
                    top = player2.pop(i)
                    break
            else:
                top = 0
            turn = not turn
    return '{}\n{}'.format(len(player2), len(player1))


n = int(input())
player1_cards = [0 for _ in range(2*n)]
for _ in range(n):
    player1_cards[int(input())-1] = 1
print(card_simulation())