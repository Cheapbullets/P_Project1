import random
import time

def fight(player, mob):
    win = 1
    xp = 0
    print(f"{player.name} is attacked by a {mob.name}!")

    player_dmg = player.str - mob.defense
    if player_dmg < 1:
        player_dmg = 1
    
    mob_dmg = mob.str - player.defense
    if mob_dmg < 1:
        mob_dmg = 1
    
    battle_tick = 20
    
    while player.cur_hp > 0 and mob.cur_hp > 0 and battle_tick > 0:
        hit_dmg, crit = damage_done(player_dmg)
        mob.cur_hp -= hit_dmg
        if crit == False:
            print(f"{player.name} dealt {hit_dmg}. {mob.name} has {mob.cur_hp} hp left.")
        else:
            print(f"{player.name} dealt critical damage! hitting for {hit_dmg}. {mob.name} has {mob.cur_hp} hp left.")

        time.sleep(1)

        if mob.cur_hp > 0:
            hit_dmg, crit = damage_done(mob_dmg)
            player.cur_hp -= hit_dmg
            if crit == False:
                print(f"{mob.name} dealt {hit_dmg}. {player.name} has {player.cur_hp} hp left.")
            else:
                print(f"{mob.name} dealt critical damage! hitting for {hit_dmg}. {player.name} has {player.cur_hp} hp left.")
            
            time.sleep(1)
        
        battle_tick -= 1
    
    if battle_tick > 0:
        if player.cur_hp > 0:
            xp_multi = (mob.level - player.level)
            if xp_multi < 1:
                xp_multi = 1
            xp = xp_multi * 2

            print(f"{player.name} has defeated {mob.name}!")
            print(f"{player.name} has been awarded {xp}xp!")

        elif mob.cur_hp > 0:
            print(f"{mob.name} has defeated {player.name}!")
            win = 0
    else:
        win = 3
        print(f"{mob.name} got away. battle was a draw.")
    
    return xp, win


def damage_done(dmg):
    crit = False
    if dmg != int(dmg * 1.5):
        base_dmg = random.randint(dmg, int(dmg * 1.5))
    else:
        base_dmg = dmg
    
    crit_roll = random.randint(0, 10)
    if crit_roll == 0:
        base_dmg = base_dmg * 2
        crit = True

    return base_dmg, crit