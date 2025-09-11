#!/bin/zsh

(
    cd ~/Documents/Skole/Semester5/Plott/TimerLogg
    source ../.venv/bin/activate

    python3 bar.py

    fag=('MAT300' 'MOD300' 'DAT330' 'DAT320' 'DAT120' 'STA100' 'ELE320')
    farger=('#0099ff' '#ff0000' '#f5f500' '#7700cc' '#00de55' '#0000ff' 'orange')

    for ((i = 1; i <= $#fag; i++)); do
        python3 barfag.py "${fag[i]}" "${farger[i]}";
    done

    python3 bartype.py

    for ((i = 32; i<= 37; i++)); do
        python3 plott.py "${i}"
    done
)