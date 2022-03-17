from MySQLController import *
from prettytable import PrettyTable

def display_options():
    print('1. Get Player Info By PlayerID')
    print('2. Display All Players')
    print('3. Get Game Info')
    print('4. Display All Games')
    print('5. Add New Player')
    print('6. Add New Game')
    print('7. Delete Player')
    print('8. Delete Game')
    print('0. Exit')


def main():
    while True:
        display_options()
        user_choice = int(input('Enter Choice: '))
        if user_choice == 1:
            player_id = int(input('Enter Player ID: '))
            player_name, player_age = get_player_info(player_id)
            print(f'Player Name = {player_name}\tPlayer Age: {player_age}')
        elif user_choice == 2:
            pTable = PrettyTable()
            query_all_players = 'SELECT * FROM fantastic_games.players'
            col_names, rows = get_rows(query_all_players)
            pTable.field_names = col_names
            pTable.add_rows(rows)
            print(pTable)
        elif user_choice == 3:
            game_id = int(input('Enter Game ID: '))
            game_name, game_price, game_year = get_game_info(game_id)
            print(f'Game Name = {game_name}\tGame Price = {game_price}\tGame Year = {game_year}')
        elif user_choice == 4:
            pTable = PrettyTable()
            query_all_games = 'SELECT * FROM fantastic_games.game'
            col_names, rows = get_rows(query_all_games)
            pTable.field_names = col_names
            pTable.add_rows(rows)
            print(pTable)
        elif user_choice == 5:
            name = input('Enter Player Name: ')
            age = int(input('Enter Player Age: '))
            add_new_player(name, age)
        elif user_choice == 6:
            game_name = input('Enter Game Name: ')
            game_price = float(input('Enter Game Price: '))
            game_year = int(input('Enter Game Release Year: '))
            add_new_game(game_name, game_price, game_year)
        elif user_choice == 7:
            player_name = input('Enter player name:')
            delete_player(player_name)
        elif user_choice == 8:
            game_name = input('Enter game name: ')
            delete_game(game_name)
        elif user_choice == 0:
            break
        input('Hit Enter to Continue\t')


if __name__ == "__main__":
    main()
