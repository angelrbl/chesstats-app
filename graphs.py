import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from Player import Player

def heatmap(player):
    matriz_np = np.array(player.get_first_moves_matrix())
    matriz_np = np.flipud(matriz_np)

    cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
    files = ["8", "7", "6", "5", "4", "3", "2", "1"]

    fig, ax = plt.subplots(figsize=(7, 7))
    sns.heatmap(matriz_np, annot=True, fmt="d", cmap="YlOrRd", square=True, cbar=False, xticklabels=cols, yticklabels=files, ax=ax)
    fig.patch.set_alpha(0.0)
    ax.tick_params(colors='white')

    return fig

def results_graph(player, color):
    if color == "white":
        wins = player.get_win_count(color="white")
        draws = player.get_draw_count(color="white")
        losses = player.get_loss_count(color="white")
        color="#ebebeb"
    elif color == "black":
        wins = player.get_win_count(color="black")
        draws = player.get_draw_count(color="black")
        losses = player.get_loss_count(color="black")
        color = "#373737"
    else:
        wins = player.get_win_count(color="")
        draws = player.get_draw_count(color="")
        losses = player.get_loss_count(color="")
        color = "#838282"
    
    
    chess_results_data = {
        "Results": ["Wins", "Losses", "Draws"],
        "Games": [wins, losses, draws]
    }

    fig, ax = plt.subplots(figsize=(8,6))
    sns.barplot(x='Results',y='Games', data=chess_results_data, color=color, ax=ax)
    sns.despine(left=True, bottom=True)
    ax.tick_params(colors='white', labelsize=12)
    ax.set_xlabel('', color='white')
    ax.set_ylabel('Game Number', color='white', fontsize=12)
    fig.patch.set_alpha(0.0)
    return fig


if __name__ == "__main__":
    pgn_file = open("chess_games.pgn", encoding="utf-8")
    user = "TensiKReyDama"

    usr = Player(user, pgn_file)
    heatmap(usr)
    plt.show()