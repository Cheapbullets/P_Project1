def check_xp(player):
    if player.xp >= (player.level * 10):
        player.level += 1
        player.max_hp += 15
        player.cur_hp = player.max_hp
        player.str += 8
        player.defense += 4
        print(f"{player.name} has leveled up and is now level {player.level}")
        check_xp(player)
    return player