
american(george).

enemy(iraq,america).

hostile(X) :-
    enemy(X,america).

missile(m1).
missile_of(m1,iraq).

sold_by(m1,george).

weapon(X) :-
    missile(X).

criminal(X) :-
    american(X),
    sells_weapon_to(X,iraq),
    hostile(iraq).

sells_weapon_to(george,iraq) :-
    sold_by(m1,george),
    missile_of(m1,iraq).

