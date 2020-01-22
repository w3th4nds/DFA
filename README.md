# DFA - Deterministic Finite Automata in python3.

```sh
Usage: python3 <dfa.py> <path_to_file>
```
```sh 
Usage: python3 <dfa.py> --help
```
#### The script takes a file as argument in the format of: 

```
Total States
Symbols-Alphabet
Initial State
Final State
Transition 1
.
.
Transition N
```

#### Example:
```
7
n o s t h a  
0
6 	
0 t 1
1 h 2
2 a 3
3 n 4
4 o 5
5 s 6
```
#### User input is checked whether it is accepted or rejected. Also detects invalid characters.

[(./images/auto1.png)]

[![(./images/auto2.png)]]
