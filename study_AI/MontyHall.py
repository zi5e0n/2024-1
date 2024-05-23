import random

NGames = 10000
UnchangeGame = []
ChangeGame = []

for i in range(0, NGames):
    CarDoor = random.choice(["Door1", "Door2", "Door3"])

    UserDoor = random.choice(["Door1", "Door2", "Door3"])

    OpenDoor = list(set(["Door1", "Door2", "Door3"])-set([UserDoor, CarDoor]))[0]

    OtherDoor = list(set(["Door1", "Door2", "Door3"])-set([UserDoor, OpenDoor]))[0]

    UnchangeGame.append(UserDoor == CarDoor)

    ChangeGame.append(OtherDoor == CarDoor)

print(f"{NGames} 개의 게임 중에서 바꾸지 않았을 때의 승률: {sum(UnchangeGame)/NGames} \n\
      바꾸었을 때의 승률: {sum(ChangeGame)/NGames}")