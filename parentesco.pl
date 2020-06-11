%HECHOS

%padres(mariela,alfredo).
%padres(mariela,elena).
%padres(ross,alfredo).
%padres(ross,elena).
%padres(dalila,alfredo).
%padres(dalila,elena).
%padres(alfredo,roberto).
%padres(alfredo,delfina).
%padres(carlos,roberto).
%padres(carlos,delfina).
%padres(adelina,roberto).
%padres(adelina,delfina).
%padres(elena,simon).
%padres(elena,juanita).
%padres(delfina,juan).
%padres(delfina,maria).
%padres(roberto,sergio).
%padres(roberto,luisa).
%padres(karina,sergio).
%padres(karina,luisa).


%padres(sheila,dalila).
%padres(sheila,luis).
%padres(daniel,carlos).
%padres(daniel,ana).
%padres(omar,carlos).
%padres(omar,ana).
%padres(felipe,omar).
%padres(felipe,zule).
%padres(lupita,jesus).
%padres(lupita,adelina).
%padres(mateo,jesus).
%padres(mateo,adelina).
%padres(fernando,jaime).
%padres(fernando,karina).

%pareja(sergio,luisa).
%pareja(luisa,sergio).
%pareja(juan,maria).
%pareja(maria,juan).
%pareja(roberto,delfina).
%pareja(delfina,roberto).
%pareja(jaime,karina).
%pareja(karina,jaime).
%pareja(jesus,adelina).
%pareja(adelina,jesus).
%pareja(carlos,ana).
%pareja(ana,carlos).
%pareja(alfredo,elena).
%pareja(elena,alfredo).
%pareja(simon,juanita).
%pareja(juanita,simon).
%pareja(luis,dalila).
%pareja(dalila,luis).
%pareja(omar,zule).

%PARENTESCOS REGLAS

hermanos(Pa,Pb) :- Pa \== Pb, padres(Pa,X),padres(Pb,X).
primos(Pa,Pb) :- padres(Pa,X),padres(Pb,Y),hermanos(X,Y).
abuelos(Pa,Pb) :- padres(Pa,Y),padres(Y,Pb).
nietos(Pa,Pb):- abuelos(Pb,Pa).
bisabuelos(Pa,Pb) :- abuelos(Pa,X), padres(X,Pb).
tios(Pa,Pb):- padres(Pa,X), hermanos(X,Pb).
bisnietos(Pa,Pb) :- bisabuelos(Pb,Pa).
tiosdos(Pa,Pb) :- padres(Pa,X),primos(X,Pb).
sobrinosdos(Pa,Pb) :- tios(Pa,X),nietos(X,Pb).
