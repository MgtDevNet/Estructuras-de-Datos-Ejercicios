1. ¿JOIN es totalmente igual a INNER JOIN?
Sí, absolutamente. En PostgreSQL y en todo el estándar SQL, escribir simplemente JOIN es un atajo sintáctico de INNER JOIN. Hacen exactamente lo mismo.

2. ¿Qué pasa con los valores NULL o vacíos en un INNER JOIN?
El INNER JOIN es estricto: solo conserva las filas donde la condición del ON es verdadera (TRUE) en ambos lados.

En SQL, cuando intentas comparar un valor nulo con cualquier otra cosa (NULL = 3), el resultado no es ni verdadero ni falso, sino UNKNOWN (desconocido). Como no es TRUE, el INNER JOIN descarta automáticamente esas filas.

Resultado práctico para el problema 181: Los jefes que tienen managerId = NULL quedan fuera de la tabla combinada desde el primer instante. 

3. ¿Qué pasa si usamos LEFT JOIN o RIGHT JOIN?
Aquí la regla cambia porque los Outer Joins están diseñados para no perder registros, aunque no tengan pareja.

A. LEFT JOIN (Conserva TODO lo de la izquierda)
Mantiene a todos los registros de la tabla de la izquierda, tengan o no un par en la otra llave de la otra tabla.

B. Right Join conserva todo lo de la derecha