% N-Queens Problem

queens(N, Queens) :-
    length(Queens, N),
    generate(Queens, N),
    safe(Queens).

generate([], _).

generate([Q|Qs], N) :-
    between(1, N, Q),
    generate(Qs, N).

safe([]).

safe([Q|Qs]) :-
    no_attack(Q, Qs, 1),
    safe(Qs).

no_attack(_, [], _).

no_attack(Q, [Q2|Qs], D) :-
    Q =\= Q2,
    abs(Q - Q2) =\= D,
    D1 is D + 1,
    no_attack(Q, Qs, D1).
