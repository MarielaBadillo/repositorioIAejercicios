hermanos(Pa,Pb) :- Pa \== Pb, padres(Pa,X),padres(Pb,X).
primos(Pa,Pb) :- padres(Pa,X),padres(Pb,Y),hermanos(X,Y).
abuelos(Pa,Pb) :- padres(Pa,Y),padres(Y,Pb).
nietos(Pa,Pb):- abuelos(Pb,Pa).
bisabuelos(Pa,Pb) :- abuelos(Pa,X), padres(X,Pb).
tios(Pa,Pb):- padres(Pa,X), hermanos(X,Pb).
bisnietos(Pa,Pb) :- bisabuelos(Pb,Pa).
tiosdos(Pa,Pb) :- padres(Pa,X),primos(X,Pb).
sobrinosdos(Pa,Pb) :- tios(Pa,X),nietos(X,Pb).
