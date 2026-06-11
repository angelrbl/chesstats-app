import chess
import chess.pgn
from ChessGame import ChessGame

pgn = open("chess_games.pgn", encoding="utf-8")

chess_games = []
cg = chess.pgn.read_game(pgn) 
while cg is not None:
    chess_games.append(ChessGame(cg))
    cg = chess.pgn.read_game(pgn) 

wins = 0
user = "TensiKReyDama"

for cg in chess_games:
    print(f"{cg.white} vs. {cg.black}:  {cg.result}")
    if (cg.get_winner() == user):
        print(user + " won.")
        wins += 1
    else:
        print(user + " did not win.")

    print()

print(f"{user} won {wins} games out of {len(chess_games)}, making a win % of: {(wins / len(chess_games)) * 100} %")