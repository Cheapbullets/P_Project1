from char_spawn import player_start, mob_spawn
from character import Character
from combat import fight

def main():
    print('Welcome to "Basic RPG" game!')
    player_name = input("Name your hero: ")
    player = player_start(player_name)
    mob = mob_spawn(player.level)
    xp, win = fight(player, mob)
    if win == 1:
        player.xp += xp

if __name__ == "__main__":
    main()