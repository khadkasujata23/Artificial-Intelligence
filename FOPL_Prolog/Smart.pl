
oversmart(hari).

stupid(X) :-
    oversmart(X).

child(ram,hari).

naughty(X) :-
    child(X,Y),
    stupid(Y).
