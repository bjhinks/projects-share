from mysql.connector import connect

host = 'localhost'
user = 'root'
password = ''


# With statements automatically close connection object and cursor
def get_rows(query):
    # Step 1: Create Connection Object
    with connect(host=host, user=user, password=password) as mysql_connection_object:
        # Step 2: Create Cursor Object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Execute a simple query
            mysql_cursor.execute(query)
            column_names = mysql_cursor.column_names
            rows = mysql_cursor.fetchall()

            return column_names, rows


def get_player_info(player_id):
    query = f"SELECT * FROM fantastic_games.players WHERE player_id={player_id}"
    col_names, rows = get_rows(query)

    player_name = rows[0][1]
    player_age = rows[0][2]

    return player_name, player_age


def get_game_info(game_id):
    query = f'SELECT * FROM fantastic_games.game WHERE game_id={game_id}'
    col_names, rows = get_rows(query)
    game_name, game_price, game_year = rows[0][1], rows[0][2], rows[0][3]

    return game_name, game_price, game_year


def add_new_player(player_name: str, player_age: int):
    """
    Adds a new row in the players table
    """
    # Step 1: Create Connection Object
    with connect(host=host, user=user, password=password) as mysql_connection_object:
        # Step 2: Create Cursor Object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Execute a simple query
            add_player_sql = f"INSERT INTO fantastic_games.players (player_name, player_age) VALUES ('{player_name}', '{player_age}')"
            mysql_cursor.execute(add_player_sql)
            # Step 4 Commit Changes
            mysql_connection_object.commit()

def add_new_game(game_name: str, game_price: float, game_year: int):
    """
    Adds a new row in the game table
    """
    # Step 1: Create Connection Object
    with connect(host=host, user=user, password=password) as mysql_connection_object:
        # Step 2: Create Cursor Object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Execute a simple query
            add_game_sql = f"INSERT INTO fantastic_games.game (game_name, price, year) VALUES ('{game_name}', '{game_price}', '{game_year}')"
            mysql_cursor.execute(add_game_sql)
            # Step 4 Commit Changes
            mysql_connection_object.commit()

def delete_player(player_name: str):
    """
    Deletes a player from the player table
    """
    # Step 1: Create Connection Object
    with connect(host=host, user=user, password=password) as mysql_connection_object:
        # Step 2: Create Cursor Object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Execute a simple query
            del_player_sql = f"DELETE FROM fantastic_games.players WHERE player_name = '{player_name}'"
            mysql_cursor.execute(del_player_sql)
            # Step 4 Commit Changes
            mysql_connection_object.commit()

def delete_game(game_name: str):
    """
    Deletes a game from the game table
    """
    # Step 1: Create Connection Object
    with connect(host=host, user=user, password=password) as mysql_connection_object:
        # Step 2: Create Cursor Object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Execute a simple query
            del_game_sql = f"DELETE FROM fantastic_games.game WHERE game_name = '{game_name}'"
            mysql_cursor.execute(del_game_sql)
            # Step 4 Commit Changes
            mysql_connection_object.commit()
