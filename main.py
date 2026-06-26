from char_spawn import player_start, mob_spawn
from character import Character
from combat import fight
from level_up import check_xp

def main():
    win = 1
    keep_playing = True
    print('Welcome to "Basic RPG" game!')
    player_name = input("Name your hero: ")
    player = player_start(player_name)
    while win != 0 and keep_playing == True:
        mob = mob_spawn(player.level)
        xp, win = fight(player, mob)
        if win == 1:
            player.xp += xp
            player.cur_hp = player.max_hp
            check_xp(player)
            user_input = input("Keep playing? (yes/no): ").lower().strip()
            keep_playing = user_input in ("yes", "y", "true", "t")

if __name__ == "__main__":
    main()