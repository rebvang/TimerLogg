#!/bin/zsh

(
    cd ~/Documents/Sem5/plotting/TimerLogg
    source ../.venv/bin/activate

    python3 bar.py
    python3 plott.py "$1" "$2"
    python3 lengde_blokk.py
    python3 integrert.py
    python3 integrert.py 0.5
    python3 total_filtrert.py
)