import streamlit as st
from Player import Player
import general as general

if "player" not in st.session_state:
    st.session_state["player"] = Player("TensiKReyDama", general.pgn_file)
player = st.session_state["player"]
if "pgn_file" not in st.session_state:
        st.session_state["pgn_file"] = general.pgn_file
pgn_file = st.session_state["pgn_file"]

st.write("# Player comparison")
st.write("###### Compare different stats between players.")
st.space("small")

try:
    player_to_compare = st.selectbox(label="Player", placeholder="Select a player to compare with", options=player.get_rivals(), index=None)
except:
    raise Exception("Error: No player selected.")

if player_to_compare:
    opponent = Player(player_to_compare, pgn_file)
    st.write(f"Comparing games between **{player.get_username()}** and **{opponent.get_username()}**")