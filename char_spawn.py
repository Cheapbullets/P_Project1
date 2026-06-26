from character import Character
import random

def player_start(name):
    player = Character(
        name,
        5,
        1,
        10,
        10,
        1,
        0
    )
    return player

def mob_spawn(level):
    mob = Character(
        "Monster",
        randomizer(5, level),
        randomizer(1, level),
        randomizer(10, level),
        randomizer(10, level),
        randomizer(1, level),
        randomizer(0, level)
    )
    return mob

def randomizer(num, level):
    minimum = max((num // 2), 1)
    return random.randint(minimum, num + int(level * 1.5))