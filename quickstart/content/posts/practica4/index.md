+++
date = '2025-11-18T16:40:05-08:00'
draft = false
title = 'Practica 4 PARADIGMA LOGICO'
+++

# PRACTICA 4
### ADRIAN BALDERAS ROSAS 373488
## Primera sesion
### Instalación del entorno de desarrollo e introduccion a Prolog
En esta sesión se realizó la instalación del entorno necesario para trabajar con Prolog, incluyendo el editor y el intérprete. Se introdujeron los conceptos básicos del lenguaje y su funcionamiento basado en reglas y hechos.

## Segunda sesion
### Continuación de programacion con Prolog
Se profundizó en la sintaxis de Prolog, el uso de predicados, consultas, listas y recursión. Se realizaron ejercicios prácticos para reforzar el pensamiento lógico declarativo.
### Sintaxis de hechos

relation(object1,object2...).
### Sintaxis de Reglas

rule_name(object1, object2, ...) :- fact/rule(object1, object2, ...)
Supo una clausula del tipo:
P :- Q;R.
También puede ser reescrita como:
P :- Q.
P :- R.

Si una clausula es así:
P :- Q,R;S,T,U.
Es entendida como:
P :- (Q,R);(S,T,U).
O puede ser reescrita como:
P :- Q,R.
P :- S,T,U.

### Tipos de relaciones

Existen varios tipos de relaciones, algunas de las cuales también pueden ser reglas. Una
regla puede determinar una relación incluso si esta no está definida explícitamente
como un hecho.

Podemos definir una relación fraternal, dos personas son hermanos sí:
Los dos son varones.
Tienen el mismo progenitor.

### Ejemplos de objetos de datos (términos)
Átomos − tom , pat , x100 , x_45
Cadenas especiales - :- , =======> , ... , .:. , ::=
Cadenas de caracteres - 'Rubai' , 'Hello, World!'
Números − 100 , 1235 , 2000.45
Variables − X , Y , Xval , _X
Estructuras − día(9, jun, 2017) , punto(10, 25)

### Operadores de comparación

X > Y X es mayor que Y
X < Y X es menor que Y
X >= Y X es mayor o igual que Y
X =< Y X es menor o igual que Y
X =:= Y Los valores X e Y son iguales
X =\= Y Los valores X e Y no son iguales

### Operadores Aritmeticos

+Suma 

-Resta 

*Multiplicación 

/ División 

** Potencia 

// División de enteros mod Módulo

### Representación de listas

Se representa como [rojo, verde, azul, blanco, oscuro]
Una lista puede estar o no vacía.
El primer elemento, llamado cabecera de la lista.
La parte restante de la lista, llamada cola.
Ahora, supongamos que tenemos una lista, L = [a, b, c] . Si escribimos Tail = [b,
c] entonces también podemos escribir la lista L como L = [a | Tail] . Aquí la barra
vertical ( | ) separa las partes de cabeza y cola.

[a, b, c] = [a | [b, c] ]

[a, b, c] = [a, b | [c] ]

[a, b, c] = [a, b, c | [ ] ]

## Tercera sesion
### Aplicaciones con Prolog
Se analizaron aplicaciones reales utilizando Prolog, como sistemas expertos, razonamiento lógico y resolución de problemas complejos. Se desarrolló una práctica integradora del paradigma lógico.

### Temas de la Tercera Sesion

- Estructuras de datos y recursión
- Backtracking
- Diferente y no
- Estudio de caso: Árbol
- Programas básicos
- Mínimo y máximo
- Circuitos resistivos
- Segmentos de recta Torre de Hanoi
- Lista enlazados
- El mono y el plátano

## REPOSITORIO
## https://github.com/adrianbalderas373488/Portafolio
