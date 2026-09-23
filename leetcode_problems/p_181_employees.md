Notese que lo que tenemos que hacer es comparar los salarios de los empleados con el salario de sus jefes pero tenemos a todas las personas en la misma tabla, por tanto, lo que tenemos que hacer es unir las tablas con un inner join y usar de clave primaria el id y el manager id porque de esa manera manejará los datos de los managers como una tabla aparte con las mismas variables y allí es más fácil compararlas. 

``` postgresql
SELECT e2.name as Employee
FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerID
WHERE
e1.salary < e2.salary```