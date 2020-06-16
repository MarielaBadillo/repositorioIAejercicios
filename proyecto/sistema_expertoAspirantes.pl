%declaracion de librerias para la interfaz

:-use_module(library(pce)).
:-use_module(library(pce_style_item)).

% metodo principal para iniciar la interfaz grafica, declaracion de
% botones, labels, y la pocicion en pantalla.
inicio:-
	new(Menu, dialog('Proyecto IA Sistema experto', size(1000,800))),
	new(L,label(nombre,'SISTEMA DE RECLUTACION')),
	new(A,label(nombre,'Equipo Mariela Badillo Edgar Marcial')),
	new(@texto,label(nombre,'Responda con un si o un no, de acuerdo a sus habilidades')),
	new(@respl,label(nombre,'')),
	new(Salir,button('SALIR',and(message(Menu, destroy),message(Menu,free)))),
	new(@boton,button('Realizar prueba',message(@prolog,botones))),


	send(Menu,append(L)),new(@btncarrera,button('Prueba')),
	send(Menu,display,L,point(125,20)),
	send(Menu,display,A,point(80,360)),
	send(Menu,display,@boton,point(100,150)),
	send(Menu,display,@texto,point(20,100)),
	send(Menu,display,Salir,point(20,400)),
	send(Menu,display,@respl,point(20,130)),
	send(Menu,open_centered).

%puestoyrequisitos

puestos('Usted es apto para el puesto de asistente DBA'):-dba,!.

puestos('Usted es apto para el puesto de sysadmin'):-sysadmin,!.

puestos('Usted es apto para el puesto de desarrollador backend'):-backend,!.

puestos('Usted es apto para el puesto de desarrollador frontend'):-frontend,!.


puestos('Usted no tiene las habilidades necesarias.').

% preguntas para dirigir al aspirante con su respectivo
% identificador de puesto

dba:- sdba,
	pregunta('¿Maneja MySQL?'),
	pregunta('¿Manejas diagramas entidad relacion?'),
	pregunta('¿Manejas software de monitoreo?');
	pregunta('¿Tienes habilidades en backups?').
sysadmin:- ssysadmin,
	pregunta('¿Manejas de redes?'),
	pregunta('¿Manejas servidores?'),
	pregunta('¿Manejas software de monitoreo?');
	pregunta('¿Manejo de linux?').

backend:- sbackend,
	pregunta('¿Manejo de frameworks?'),
	pregunta('¿Manejo de lenguaje HTML5 CSS JS?'),
	pregunta('¿Manejo de PostgreSQL?');
	pregunta('¿Manejo de Jquery?').

frontend:- sfrontend,
	pregunta('¿Diseño de interfaz?'),
	pregunta('¿Programacion a nivel responsive?'),
	pregunta('¿Manejo de bootstrap?');
	pregunta('¿Edicion de materiales visuales? ').

%identificador de habilidad que dirige a las preguntas correspondientes

sdba:-pregunta('¿Experiencia en DBA?'),!.
ssysadmin:-pregunta('¿Experiencia en Administracion de sistemas?'),!.
sbackend:-pregunta('¿Experiencia en desarrollo backend?'),!.
sfrontend:-pregunta('¿Experiencia en desarrollo frontend?'),!.


% proceso del evaluacion basado en preguntas de si y no, cuando el
% usuario dice si, se pasa a la siguiente pregunta del mismo ramo, si
% dice que no se pasa a la pregunta del siguiente ramo


:-dynamic si/1,no/1.
preguntar(Problema):- new(Di,dialog('Evaluacion')),
     new(L2,label(texto,'Responda las siguientes preguntas')),
     new(La,label(prob,Problema)),
     new(B1,button(si,and(message(Di,return,si)))),
     new(B2,button(no,and(message(Di,return,no)))),

         send(Di,append(L2)),
	 send(Di,append(La)),
	 send(Di,append(B1)),
	 send(Di,append(B2)),

	 send(Di,default_button,si),
	 send(Di,open_centered),get(Di,confirm,Answer),
	 write(Answer),send(Di,destroy),
	 ((Answer==si)->assert(si(Problema));
	 assert(no(Problema)),fail).

% cada vez que se conteste una pregunta la pantalla se limpia para
% volver a preguntar

pregunta(S):-(si(S)->true; (no(S)->fail; preguntar(S))).
limpiar :- retract(si(_)),fail.
limpiar :- retract(no(_)),fail.
limpiar.

% proceso de eleccion de acuerdo a la evaluacion basado en las preguntas
% anteriores

botones :- lim,
	send(@boton,free),
	send(@btncarrera,free),
	puestos(Puesto),
	send(@texto,selection(' ')),
	send(@respl,selection(Puesto)),
	new(@boton,button('inicia prueba',message(@prolog,botones))),
        send(Menu,display,@boton,point(40,50)),
        send(Menu,display,@btncarrera,point(20,50)),
limpiar.
lim :- send(@respl, selection('')).

