
mammal(horse).
mammal(cow).
mammal(pig).

horse(X) :-
    offspring(X,Y),
    horse(Y).

horse(bluebeard).

parent(bluebeard,charlie).

offspring(X,Y) :-
    parent(Y,X).
