import random

def poker(player):
    PLAYER = player
    player_cards = {'Player_%s'%(i+1): list() for i in range(0,PLAYER)}

    # Generate 52 poker cards
    style_list = ['Spade', 'Heart', 'Diamond', 'Club']
    poker_list = ['%s_%s'%(style_list[int(i%4)], int(i/4) + 1) for i in range(0, 52)]

    # Shuffling
    random_poker_list = []
    while len(poker_list) > 0:
        choice = random.randint(0, len(poker_list)-1)
        random_poker_list.append(poker_list[choice])  # 將 poker_list 隨機排列
        del poker_list[choice]

    # Distributing
    for n, c in enumerate(random_poker_list):
        player_cards['Player_%s' % (n % PLAYER + 1)].append(c)  # 將 random_poker_list 一一加入 Player1, 2, 3,... 的 value

    return player_cards       # dictionary

if __name__ == '__main__':
    player_cards = poker(5)
    print(player_cards)

    # Order and print
    for i in player_cards:                      # 5 elements
        player_cards[i].sort(key=lambda x: x.split('_')[0])   # 將 key 拆為 Heart, 11 然後對花色排序
        print(i)
        print(player_cards[i])
        print()

