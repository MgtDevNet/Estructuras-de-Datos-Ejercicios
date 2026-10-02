Notese que lo que tenemos que hacer es comparar los salarios de los empleados con el salario de sus jefes pero tenemos a todas las personas en la misma tabla, por tanto, lo que tenemos que hacer es unir las tablas con un inner join y usar de clave primaria el id y el manager id porque de esa manera manejará los datos de los managers como una tabla aparte con las mismas variables y allí es más fácil compararlas. 

``` postgresql
SELECT e2.name as Employee
FROM employee e1
INNER JOIN employee e2 ON e1.id = e2.managerID
WHERE
e1.salary < e2.salary```

```python
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(
        employee, # la unimos con ella misma,
        left_on = "managerId", # llave BD izquierda
        right_on = "id", # llave BD Derecha
        
        # tiene todo el sentido usar managerId de la izquierda así 
        # se toman es todos los registros que están en manager id
        # y los relaciona con id

        suffixes = ("_emp","_mng") # tupla de subfijos para varibles repetidas 
    # Las variables name y salary se repiten, pero se diferencian
    # por el subfijo
    )
    
    # seleccionar los registros donde el salario 
    # del empleado es mayor al del manager
    r = df.loc[df["salary_emp"] > df["salary_mng"], ["name_emp"]]
    # al seleccionar la variable entre corchetes se obtiene un data frame
    r = r.rename(columns={"name_emp":"Employee"}) # se cambia como nombre_viejo=nombre_nuevo
    # y se usa como un diccionario
    #ya 'r' es el data frame con la solución, pero hay que cambiar el nombre

    return r  
```