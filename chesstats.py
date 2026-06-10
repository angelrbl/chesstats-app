import chess
import chess.pgn

pgn = open("chess_games.pgn", encoding="utf-8")

chess_game = chess.pgn.read_game(pgn) 
while chess_game is not None:
    headers = chess_game.headers
    print(f"{headers.get("White")} vs. {headers.get("Black")}:  {headers.get("Result")}")
    chess_game = chess.pgn.read_game(pgn) 
    