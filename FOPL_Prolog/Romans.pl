
pompeian(marcus).

roman(X) :-
    pompeian(X).

assassinate(marcus,caesar).

not_loyal(X,caesar) :-
    assassinate(X,caesar).

hate(marcus,caesar) :-
    roman(marcus),
    not_loyal(marcus,caesar).

