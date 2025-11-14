girl(priya).
girl(natasha).
girl(jasmin).
can_cook(priya).

sing_a_song(ana).
listens_to_music(rodrigo).
listens_to_music(ana) :- sing_a_song(ana).
happy(ana) :- sing_a_song(ana).
happy(rodrigo) :- listens_to_music(rodrigo).
plays_guitar(rodrigo) :-listens_to_music(rodrigo).

can_cook(priya).
can_cook(jasmin).
can_cook(timoteo).
likes(priya, jasmin) :- can_cook(jasmin).
likes(priya, timoteo) :- can_cook(timoteo).

parent(simon, pedro).
parent(simon, raj).
male(pedro).
male(raj).

brother(X, Y) :-parent(Z, X), parent(Z, Y), male(X), male(Y).