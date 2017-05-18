games_count = int(input())

stat_dict = {}
result_dict = {'games': 1, 'win': 0, 'draw': 0, 'lose': 0}

for _ in range(games_count):
    game_result = input().split(';')
    game_result = zip(game_result[::2], game_result[1::2])
    game_result = [(i[0], int(i[1])) for i in game_result]

    for n, _ in game_result:
        if n not in stat_dict:
            stat_dict[n] = result_dict.copy()
        else:
            stat_dict[n]['games'] += 1

    if game_result[0][1] == game_result[1][1]:
        for n, _ in game_result:
            stat_dict[n]['draw'] += 1
    elif game_result[0][1] > game_result[1][1]:
        stat_dict[game_result[0][0]]['win'] += 1
        stat_dict[game_result[1][0]]['lose'] += 1
    else:
        stat_dict[game_result[0][0]]['lose'] += 1
        stat_dict[game_result[1][0]]['win'] += 1

for team in stat_dict:
    print(team + ':' + str(stat_dict[team]['games']),
          str(stat_dict[team]['win']),
          str(stat_dict[team]['draw']),
          str(stat_dict[team]['lose']),
          str(stat_dict[team]['win'] * 3 + stat_dict[team]['draw']))