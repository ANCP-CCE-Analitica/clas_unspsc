# Recomendación UNSPSC

El Código Estándar de Productos y Servicios de Naciones Unidas (Código UNSPSC, por sus siglas en inglés) implementado en el sistema de contratación pública de Colombia con la versión 14.08 es una metodología de codificación de productos y servicios que de forma clara y siguiendo un arreglo jerárquico de cuatro niveles, les permite a las entidades públicas estandarizar las diferentes adquisiciones requeridas y  permite que proveedores y demás actores del sistema de contratación pública identifiquen de manera sencilla la demanda de los compradores. Así mismo, facilita la implementación de modelos de optimización de compra (como el modelo de abastecimiento estratégico propuesto por la Subdirección de Estudios de Mercado y Abastecimiento Estratégico de la entidad), permite la generación de cubos de gasto y el cálculo de penetración de productos en el sistema de compra pública y, finalmente, es una herramienta bastante útil para la creación de instrumentos de agregación de demanda y acuerdos marco de precio.

Aquí encontrará una herramienta muy sencilla que le hace una recomendación del código apropiado desde el detalle del objeto contractual.

## La librería clasunspsc

El paquete ```clasunspsc``` proporciona funcionalidad para sugerir códigos de Naciones Unidas que pueden utilizarse para ingresar productos correctamente al SECOP.

### Instalación

Para instalar el paquete, ejecuta el siguiente comando:

```
pip install clasunspsc
```

### Uso básico

#### Función recomendador(descripcion_del_producto, numero_de_elementos_a_recomendar)

Realiza recomendaciones de códigos de Naciones Unidas basadas en una descripción de productos.

```
from clasunspsc.clasunspsc import recomendador

# Descripción de productos
descripcion = "Haga una breve descripción de los productos que quiere usar ..."

# Número de elementos a recomendar
topk = 5

# Obtener recomendaciones
recomendador(descripcion, topk)
```

#### Función recomendador_api(descripcion_del_producto, numero_de_elementos_a_recomendar)

Similar a la función recomendador(), pero diseñada para ser utilizada en una API.

```
from clasunspsc.clasunspsc import recomendador_api

# Descripción de productos
descripcion = "Haga una breve descripción de los productos que quiere usar ..."

# Número de elementos a recomendar
topk = 5

# Obtener recomendaciones en formato de diccionario
recomendador_api(descripcion, topk)
```

#### Función recomendador_int()

Muestra una interfaz interactiva para utilizar la función recomendador().

```
from clasunspsc.clasunspsc import recomendador_int

# Ejecutar la interfaz interactiva
recomendador_int()
```

### Notas adicionales

* Asegúrate de tener una conexión a Internet activa, ya que el paquete accede a los datos actualizados de Naciones Unidas en tiempo real.
* Para obtener resultados más relevantes, proporciona una descripción precisa de los productos en la función recomendador() o recomendador_api().
* Los códigos de Naciones Unidas recomendados se devuelven en forma de tabla o diccionario, dependiendo de la función utilizada.