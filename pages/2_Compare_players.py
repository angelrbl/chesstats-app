import streamlit as st
from Player import Player
import general as general

if "player" not in st.session_state:
    st.session_state["player"] = Player("TensiKReyDama", general.pgn_file)
player = st.session_state["player"]

player_to_compare = st.selectbox(label="Player", placeholder="Select a player to compare with", options=player.get_rivals(), index=None)