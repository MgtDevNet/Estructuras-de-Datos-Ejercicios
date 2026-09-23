Primero que nada recordemos que el group by es un operador par hacer operaciones sobre conjuntos de categorías de variables categóricas y poder tener mediciones o valores acerca de todos estos grupos teniendo tablas que no están agrupadas. 

En adición, es necesario tener en cuenta que para poder realizar una de estas operaciones usamos simplemente las funciones como count, avg, sum, etc. Pero en caso que se quiera poner una condición sobre estos datos agrupados hay que usar la palabra reservada HAVING que sirve para EJECUTAR UN FILTRO DESPUÉS DE AGRUPAR. 

HAVING ES EL EQUIVALENTE AL WHERE PERO PARA DATOS AGRUPADOS, ES DECIR, EL WHERE SE USA PARA PONER CONDICIONES EN LOS DATOS QUE SE EVALUAN FILA POR FILA, EN CAMBIO EL HAVING ES PARA PONER CONDICIONES EN LOS DATOS PERO LUEGO DE ESTAR AGRUPADOS. 

```
SELECT departamento, AVG(salario) AS salario_promedio
FROM Empleados
WHERE tipo_contrato = 'Tiempo Completo'  -- 1. Filtra filas individuales primero
GROUP BY departamento                     -- 2. Agrupa lo que sobrevivió
HAVING AVG(salario) > 50000;              -- 3. Filtra los grupos resultantes
```

Es importante mencionar que el HAVING NO ES OBLIGATORIO, solo se usa para condiciones en datos luego de estar agrupados. Si se quiere simplemente crear columnas no hay necesidad de usar el HAVING. 

-- Esto es perfectamente válido sin HAVING
```
SELECT departamento, COUNT(*) AS total_empleados
FROM Empleados
GROUP BY departamento;```

Mostrar el número de empleados por departamento