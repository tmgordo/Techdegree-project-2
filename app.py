import constants
import copy
import random
import statistics


all_players = copy.deepcopy(constants.PLAYERS)    
all_teams = copy.deepcopy(constants.TEAMS)

experienced_players = []
inexperienced_players = []

panthers = []
bandits = []
warriors = []

num_players_team = int(len(all_players) / len(all_teams))

def clean_data():
    for player in all_players:
        player['height'] = int(player['height'].split()[0])
        if player['experience'] == 'YES':
            player['experience'] = True
            experienced_players.append(player)
        if player['experience'] == 'NO':
            player['experience'] = False
            inexperienced_players.append(player)
        player['guardians'] = player['guardians'].split(' and ')
    

def balance_teams():
    random.shuffle(inexperienced_players)
    random.shuffle(experienced_players)
    for player in inexperienced_players:
        if len(panthers) != (num_players_team / 2):
            panthers.append(player)
        elif len(warriors) != (num_players_team / 2):
            warriors.append(player)
        else:
            bandits.append(player)
    for player in experienced_players:
        if len(panthers) != num_players_team:
            panthers.append(player)
        elif len(warriors) != num_players_team:
            warriors.append(player)
        else:
            bandits.append(player)
        

def stats(team, team_name):
    total_team_players = len(team)
    player_names = []
    player_heights = []
    player_guardians = []
    num_inexp_player = []
    num_exp_player = []
    for player in team:
        player_names.append(player['name'])
        player_heights.append(player['height'])
        player_guardians.append(', '.join(player['guardians']))
        if player['experience'] == True:
            num_exp_player.append(player)
        else:
            num_inexp_player.append(player)
    player_heights = statistics.mean(player_heights)
    player_names = ', '.join(player_names)
    print(f'\nTeam:  {team_name} Stats\n~~*~~*~~*~~*~~*~~*~~*~~\n')
    print(f'Total Players:  {total_team_players}')
    print(f'Total experienced:  {len(num_exp_player)}')
    print(f'Total unexperienced:  {len(num_inexp_player)}')
    print(f'Average height(inches):  {round(player_heights, 1)}\n')
    print(f'Players on Team {team_name}:\n   {player_names}\n')
    print(f'Guardians for Team {team_name}:\n   {", ".join(player_guardians)}\n')

def main():
    clean_data()
    balance_teams()
    print('Welcome to the...\n\nBASEBALL STATISTICS TOOL\n\n~~~~~~Main Menu~~~~~~\n\n')
    print('Please choose from the following:\n')
    print('  A. Display stats for team\n  B. Quit program\n')
    while True:
        try:
            choice1 = input('Enter choice  ')
            if choice1.upper() == 'A':
                print('\nChoose a team to see statistics for:\n\n')
                print('A. Panthers')
                print('B. Bandits')
                print('C. Warriors')
                choice2 = input('\nEnter choice  ')
                if choice2.upper() == 'A':
                    stats(panthers, 'Panthers')
                    print("\nIf you'd like to see stats for more teams enter 'A'. Otherwise, enter 'B' to quit.\n")
                    continue
                if choice2.upper() == 'B':
                    stats(bandits, 'Bandits')
                    print("\nIf you'd like to see stats for more teams enter 'A'. Otherwise, enter 'B' to quit.\n")
                    continue
                if choice2.upper() == 'C':
                    stats(warriors, 'Warriors')
                    print("\nIf you'd like to see stats for more teams enter 'A'. Otherwise, enter 'B' to quit.\n")
                    continue
                else:
                    raise ValueError
                    continue
            if choice1.upper() == 'B':
                print('Thank for using the Baseball Statistic Tool. Have a beautiful day')
                break
            else:
                raise ValueError
        except ValueError:
            print('Please enter one of the above options\n')
            continue
        break

if __name__ == '__main__':
    main()
