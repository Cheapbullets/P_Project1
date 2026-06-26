from character import Character
import random

def player_start(name):
    player = Character(
        name,
        8,
        4,
        15,
        15,
        1,
        0
    )
    return player

def mob_spawn(level):
    mob = Character(
        "Monster",
        randomizer(5, level),
        randomizer(2, level),
        randomizer(10, level),
        randomizer(10, level),
        randomizer(1, level),
        randomizer(0, level)
    )
    return mob

def randomizer(num, level):
    minimum = max((int((num + 1) * 1.15) * level), 1)
    return random.randint(minimum, int((num + 1) * level * 1.5))