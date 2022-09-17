def game():
    return 30


score = game()
with open("Ch9_Que2_game.txt") as f:
    hiscore = int(f.read())

if hiscore < score:
    with open("Ch9_Que2_game.txt", "w") as f:
        f.write(str(score))


# def game():
#     #     return 26
#     return 28


# score = game()
# with open("Ch9_Que2_game.txt") as f:
#     #     hiscore = int(f.read())
#     hiScoreStr = f.read()
# if hiScoreStr == '':
#     # if hiscore < score:
#     with open("Ch9_Que2_game.txt", "w") as f:
#         #     with open("Ch9_Que2_game.txt", "w") as f:
#         f.write(str(score))
# #         f.write(str(score))
# elif int(hiScoreStr) < score:
#     with open("Ch9_Que2_game.txt", "w") as f:
#         f.write(str(score))
