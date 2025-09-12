#!/bin/zsh

(
    cd ~/Documents/Sem5/plotting/TimerLogg
    source ../.venv/bin/activate

    python3 bar.py

    fag=('MAT300' 'MOD300' 'DAT330' 'DAT320' 'DAT120' 'STA100' 'ELE320' 'ELE210')
    farger=('#0099ff' '#ff0000' '#f5f500' '#7700cc' '#00de55' '#0000ff' 'orange' '#9900ff')

    for ((i = 1; i <= $#fag; i++)); do
        python3 barfag.py "${fag[i]}" "${farger[i]}";
    done

    python3 bartype.py

    python3 plott.py 
)