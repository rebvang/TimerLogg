#!/bin/zsh

(
    cd ~/Documents/Sem5/plotting/TimerLogg
    source ../.venv/bin/activate

    python3 bar.py
    python3 barfag.py
    python3 bartype.py
    python3 plott.py "$1" "$2"
    python3 lengde_blokk.py
)