scores = {
        # rock
        'A': 1,
        'X': 1,

        # paper
        'B': 2,
        'Y': 2,

        # scissors
        'C': 3,
        'Z': 3,
    }

# pt1
def pt1():
    def evalGame(me, opp):
        winningPos = [('Z', 'B'), ('Y', 'A'), ('X', 'C')]
        print('me: ', me, 'opp: ', opp)
        if (me, opp) in winningPos:
            print('win')
            return 6

        elif scores[me] == scores[opp]:
            print('draw')
            return 3

        else:
            print('lose')
            return 0

    with open('input.txt') as f:
        lines = f.readlines()

    lines = [line.strip().split(' ') for line in lines]
    score = 0

    for (oppMove, myMove) in lines:
        oppScore = scores[oppMove]
        myScore = scores[myMove]

        score += myScore + evalGame(myMove, oppMove)

    return score

# pt2
def pt2():
    def evalGame(me, opp):
        winningPos = [('Z', 'B'), ('Y', 'A'), ('X', 'C')]
        print('me: ', me, 'opp: ', opp)
        if (me, opp) in winningPos:
            print('win')
            return 6

        elif scores[me] == scores[opp]:
            print('draw')
            return 3

        else:
            print('lose')
            return 0

    equalVals = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
    }

    winningVals = {
        'B': 'Z',
        'A': 'Y',
        'C': 'X'
    }

    losingVals = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'    
    }

    roundEnds = {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win',
    }

    with open('input.txt') as f:
        lines = f.readlines()

    lines = [line.strip().split(' ') for line in lines]

    score = 0
    for (oppMove, myMove) in lines:
        if roundEnds[myMove] == 'win':
            score += scores[winningVals[oppMove]] + evalGame(winningVals[oppMove], oppMove)
        elif roundEnds[myMove] == 'draw':
            score += scores[equalVals[oppMove]] + evalGame(equalVals[oppMove], oppMove)
        else:
            score += scores[losingVals[oppMove]] + evalGame(losingVals[oppMove], oppMove)

pt1()
pt2()
