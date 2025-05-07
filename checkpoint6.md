# **Checkpoint 6**



## **¿Para qué usamos Clases en Python?** 

![Clases en python](Images\clases_python.png)

Las clases provee una frome de empaquetar datos y funcionalidad juntos, y ya que python es un lenguaje **orientado a objetos**, tiene un soporte de primer nivel en la creacion de clases, pero no es imprescindible usarlas para hacer un programa.  
Para crear una clase, primero usamos la palabra reservada *class* seguida del nombre que le queramos dar a esa clase, pero tiene que estar escrito, **primera letra en mayuscula**, y **el resto en minuscula**  

~~~
class Checkpoint:
~~~  

Las clases pueden contener funciones, a las que se llaman metodos, que son funciones comunes, pero la diferencia es que la indentacion las coloca dentro de la clase.

~~~
class Checkpoint:
    def completed(self):
        print("¡Checkpoint completado!")
~~~

En las clases, todas las funciones definidas debene tener al menos un argumento, que por convencion, se le llama *self*, y eso es una referencia a la *instancia*, que crearemos ahora mismo.  

~~~
checkpoint = Checkpoint()
checkpoint.completed()
~~~  

Como podemos observar, al invocar el metodo de una clase, no tenemos porque indicar *self*, ya que python lo hace por nosotros. Aunque si quisieramos asegurarnos, seria tal que asi:  

~~~
checkpoint = Checkpoint()
Checkpoint.completed(checkpoint)
~~~  

Una clase tambien puede contener *variables*, que se las conoce con el nombre de *atributos*, y para estos atributos definimos un metodo especial llamado **__init__**, pero esto lo mencionaremos en la siguiente pregunta.

Tambien tenemos la herencia, y trabquil@s, no quiere decir que vayamos a recibir unos cuantos millones, si no que nos permite definir las jerarquias que comparten metodos y atributos.  
Digamos que creamos dos codigos muy similares, como por ejemplo, para medir las areas de un triangulo o de un rectangulo:

~~~
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2
~~~  

Si miramos atentamente, las dos comparten argumentos, lo unico que las diferencia es la formula para calcular el area, ¿y como funciona aqui la jerarquia y la herencia?  
Pues creamos lo que se llamaria una **clase padre**, que recogeria como argumento las base y la altura que se pide en las formulas, y luego cada clase individual recibiria esos argunemtos de la *clase padre*, pero cambiando una cosa, ahora en las clases, tendremos que poner como argumento en nombre de la *clase padre*, ya que si no python no encontraria esos argumentos.  
Finalmente podemos ver eso en el siguiente ejemplo:  

~~~
class Medidas_poligono:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Rectangulo(Medidas_poligono):

    def area(self):
        return self.base * self.altura
    
class Triangulo(Medidas_poligono):

    def area(self):
        return (self.base * self.altura) / 2
~~~







## **¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?**  

Como hemos mencionado antes, el metodo `__init__`, que se escribe con dos guiones bajos al principio y al final, es el metodo que se ejecuta automaticamente cuando se crea una instancia en una clase. Este metodo tambien tiene el nombre de *contructor*. Vamos a poner un ejemplo:

~~~
class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, {self.nombre}!"
~~~

Aqui tenemos un codigo, con una clase, un metodo `__init__` dentro y una funcion, esta funcion acoge el nombre que le demos y nos devuelve un saludo, como por ejemplo:  

~~~
class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola {self.nombre}!"
~~~

En este ejemplo hemos creado una clase, a la que si le damos un nombre como argumento:

~~~
saludo = Saludo('Pablo')
saludo.saludar()
~~~

Si incluimos la segunda linea del codigo anterior en el argumento de *print*, veremos que nos devuelve *'Hola Pablo!'*, pero a diferencia de si hubieramos hecho *hardcode* el nombre de Pablo en el codigo, ahora la funcion puede aceptar cualquier nombre, ya que igual el programa no siempre saluda a la misma persona.

## **¿Cuáles son los tres verbos de API?**  

Los verbos en las APIs sirven para realizar diversas funciones, estas funciones se realizan utilizando una URL, *Localhost5000/User* por ejemplo, empezamos por el primero

+ POST: este verbo sirve para crear nuevos recursos en el servidor, pero hay que tener cuidado, si se envia varias veces puede crear dupicados. La informacion que se envia va en el *body* de la solicitud, seleccionando la opcion POST y escribiendo la URL correcta.

~~~
{
    "nombre" : "Pablo"
    "curso" : "Full Stack"
}
~~~

+ GET: este verbo realiza la funcion de recuperar la informacion de la API, pero ni cambia el estado del servidor, no debe modificar ningun dato y se puede utilizar parametros de la URL para filtrar lo que se quiere recuperar. Si mandamos una solicitud con GET a la URL correcta y el proceso va bien recibiremos lo siguiente

~~~
[
    "nombre" : "Pablo"
    "curso" : "Full Stack"
]
~~~

+ PUT: finalmente, este verbo sirve para reemplazar o actualizar un recurso que ya existe, reemplazando o actualizando todos sus atributos, pero mandar varias solicitudos no generara cambios adicionales, y no es recomendable hacerlo si el recurso no existe, ya que algunas APIs pueden crearlo y podria crear problemas. Para realizar la funcion de este verbo, mandamos solicitud con PUT a la URL correcta, y si queremos cambiar los atributos de las solicitudes anteriores, tenemos que hacer lo siguente, y una vez hecho, si sale un mensaje correcto, el cambio estara hecho.

~~~
{
    "nombre" : "Pedro"
    "curso" : "Coding Foundations"
}
~~~







## **¿Es MongoDB una base de datos SQL o NoSQL?**  

![MongoDB Logo](Images\logo_mongodb.png)

Mongo DB nes una base de datos NoSQL, ¿y esto porque es?  
1. Esto es porque utiliza JSON/BSON
2. No utiliza ni filas ni columnas, si no que funciona con colecciones y documentos
3. Las consultas a la base de datos se hacen tambien en un idioma parecido al JSON
4. En SQl se utilizan *foreing keys*, es decir, que se le asigna un id para poder relacionar tablas, pero en MongoDB, se anidan los datos directamente en el documento.

Aqui tenemos varios ejemplos de comandos en MongoDB

+ Importante, para abrir la base de datos, en el terminal
~~~
mongod
~~~
+ Y para abrir Mongo Shell:
~~~
mongosh
~~~

+ Para crear una base de datos:
~~~
use mydatabase
~~~

+ Para crear una coleccion:
~~~
db.createCollection("users")
db.users.insertOne({ user1 : "Pablo"})
~~~
(La segunda opcion toma el argumento y crea automaticamente una coleccion)


+ Para insertar un documento en la coleccion:
~~~
db.users.insertOne({
    user : "Pablo",
    age : 23
})
~~~

+ Para inserter varios documentos en la coleccion:
~~~
db.users.insertMany({
    user : "Pablo",
    age : 23
},
{
    user : "Luis",
    age : 45
})
~~~

+ Para realizar una busqueda de todos los documentos:
~~~
db.users.find()
~~~

+ Para realizar una busqueda con una condicion:
~~~
db.users.find({name : "Pablo"})
~~~

+ Para realizar una busqueda con varias condiciones:
~~~
db.users.find({name : "Pablo"}, {age : 23})
~~~

+ Para actualizar, One o Many si es uno o varios
~~~
db.users.update()
~~~

+ Para eliminar un documento:
~~~
db.usuarios.deleteOne({name : "Luis"})
~~~

+ Para eliminar todos en una coleccion
~~~
db.usuarios.deleteMany({})
~~~

+ Para eliminar varios con condiciones
~~~
db.usuarios.deleteMany({name : "Luis"}, {name : "Pablo})
~~~

+ Para eliminar una coleccion
~~~
db.usuarios.deleteMany({name : "Luis"}, {name : "Pablo})
~~~

+ Finalmente para eliminar la base de datos:
~~~
db.dropDatabase()
~~~

En conclusion, MongoDB es una base de datos muy versatil, facil de entender y de usar, y se puede usar en formato de consola, con la propia Shell de Mongo(mongosh)






** ##¿Qué es una API?**  

**API**, que quiere decir *Apliccation Programmin Interface* o *Interfaz de Programacionde Aplicaciones* es un conjunto de normas o herramientas que permiten dos sistemas de software comunicarse entre si para poder compartir datos o funciones sin que este construida internamente.
Por ejemplo, la aplicacion de tiempo del movil, no mide ella misma los datos, si no que se comunica con una API de meteorologia, realiza una peticion para poder recibir esos datos y mostrartelos a ti.  

Las APIs usan los verbos GET, POST, PUT, DELETE, que realizan funciones como creacion, consulta, actualizacion o borrado de recursos. Estas pueden ser ademas, privada, publicas o las de partners, que son un termino medio entre las publicas y las privadas.

Las APIs son muy importantes en el dia a dia, ya que algunos de los ejemplos mas llamativos o mas importantes son por ejemplo las sincronizaciones de galerias para guardar fotos en la nube, el acceso en mapas en aplicaciones o webs





## **¿Qué es Postman?**  


![Logo de Postman](Images\logo_postman.png)  
**Postman** es una herramienta que permite a los desarrolladores probar y documentar APIs, ya que permite hacer sencillamente peticiones HTTP, es decir, los verbos que hemos hablado anteriormente: GET, POSt, PUT y DELETE; ademas permite ver las respuestas entregadad por la API a la solicitud sin tener que escribir el codigo.

En resumen, nos permite:

1. Enviar datos con metodos HTTP a la URL que queramos
2. Visualizar la respuesta usando GET en el formato que decidamos seleccionar, ya sea JSON, XLM, HTML o texto
3. Guardar y compartir colecciones.
4. Incluir datos en el *body* usando POST y PUT
5. Ademas, es un entorno que facilita la configuracion, la pruebas y la produccion

En conclusión, **Postman** resulta una herramienta comoda para trabajar con APIs de forma profesional, permitiendo peticiones, viendo las respuestas y funciones mas profundas que evitan tener que desarrollar una API completa, por lo que reulta ideal para el propio desarrollo, pruebas e incluso educacion sobre APIs

**##¿Qué es el polimorfismo?**  

El **polimorfismo** es un principio fundamental en programacion, que esta basado en objetos que permiten que diferentes clases implementen metodos con el mismo nombre, pero que en cambio, tengan distinto comportamiento, esto facilita la programacion ya que abre las puertas a codigos mas flexibles y escalables.

+ Curiosidad: El termino *polimorfismo* viene del griego, que a traduccion quiere decir "Muchas formas"

Para representar el polimorfismo, vamos a crear un codigo muy basico:

~~~
class Pollito:
    def sonido(self):
        return 'Pio Pio'
    
class Pez:
    def sonido(self):
        return 'Blup Blup'
    
class Oveja:
    def sonido(self):
        return 'Beee'
~~~

Si crearamos un codigo que iterara por cada una de estas clases:

~~~
animales = [Pollito(), Pez(), Oveja()]

for animal in animales
    print(animal.sonido())
~~~

Nos devolveria esto:

~~~
Pio Pio
Blup Blup
Beee
~~~

Podemos ver que se ha iterado clase por clase, y nos ha devuelto el resultado de la funcion, de forma individual, a pesar de que todas tienen el mismo nombr, que es una de las ventajas, ademas de las siguientes:

+ Permite escribir funciones genericas(como hemos hecho en el ejemplo)
+ Promueve la flexibilidad en el codigo, y permite un uso mas beneficioso del sistema de programacion por objetos. 

**#¿Qué es un método dunder?**  

El metodo **dunder**, que es la abreviatura de *double underscore*(doble guion bajo). Este metodo nos permite definir **comportamientos especiales y personalizados** para los objetos.

Por ejemplo, `__init__` es un metodo dunder que se que se ejecuta automaticamente al crear una instancia de una clase, y se usa concretamente para inicializar atributos. Tambien podemos encontrar otros metodos, como por ejemplo `__str__`, `__len__`, ...

+ `__str__`(self)': Devuelve una representacion legible, similar al uso de *print*.  
+ `__repr__`(self): nos devuelve una representacion debuggeada el objeto.
+ `__add__`(self): define el comportamiento del operador **+**, usado para sumar y combinar objetos.
+ `__len__`(self): Devuelve la cantidad o la longitud interna.
+ `__getitem__`(self, index): permite acceder a los objetos mediando el index.

Aqui vamos a demostrar un ejempl, que nos va a mostrar una funcion donde meteremos cada uno de estos metodos dunder y veremos que output no da. Esta funcion consta de una clase, donde nos permitira crear una "caja" con elementos que podemos contar, consultar, añadir e incluso combinarlas:

~~~
class Caja:
    def __init__(self, nombre, elementos):
        self.nombre = nombre
        self.elementos = elementos

    def __str__(self):
        return f"Caja(nombre={self.nombre}, elementos={self.elementos})"

    def __repr__(self):
        return f"Caja(nombre={self.nombre!r}, elementos={self.elementos!r})"

    def __add__(self, otro):
        nuevo_nombre = f"{self.nombre}+{otro.nombre}"
        nuevos_elementos = self.elementos + otro.elementos
        return Caja(nuevo_nombre, nuevos_elementos)

    def __len__(self):
        return len(self.elementos)

    def __getitem__(self, index):
        return self.elementos[index]


caja_A = Caja("Herramientas", ["martillo", "destornillador, "llave inglesa"])
caja_B = Caja("Materiales", ["clavos", "tornillos", "tuercas"])

print(str(caja_A))
print(repr(caja_A))

caja_combinada = caja_A + caja_B
print(caja_combinada)

print("Total de elementos:", len(caja_combinada))
print("Primer elemento:", caja_combinada[0])
print("Último elemento:", caja_combinada[-1])
~~~

Primero tenemos la funcion `__init__`, que es lo basico al trabajar en una clase con objetos, que toma los argumentos necesarios. Segundo tenemos el metodo `__str__`, que nos devuelve los elementos que hemos declarado en las variables como si hubieramos hecho print con la propia varible, pero ademas hemos puesto que nos diga cuantos elementos hay. Luego tenemos el `__repr__`, que nos muestra algo parecido a `__str__`, pero se considera que es mas oficial o mejor para los desarrolladores.  
Luego tenemos `__add__`, con la que podemos juntar los elementos que tenemos en la caja A y B, podemos usarlo a traves del operador **+**, los que nos mostrara cuantos elementos hay combinando las dos listas
Por ultimo, tenemos las funciones `__len__` y `__getitem__`, la primera nos muestra cuantos elementos hay contando los indices del objeto, y la segunda, hemos programado la funcion para que declarando print con ul nombre de la variable y el indice te muestra el objeto seleccionado.  
En la siguiente caja de codigo se muestran la manera de utiliar print con estos metodos y los resultados que tendrian o que se espera que tendrian.  

~~~
print(str(caja_A))  # Caja(nombre='Herramientas', elementos=['martillo', 'destornillador'])
print(repr(caja_A))  # Caja(nombre='Materiales', elementos=['clavos', 'tornillos', 'tuercas'])
print(caja_A + caja_B)  # Caja(nombre='Herramientas+Materiales', elementos=['martillo', 'destornillador', 'clavos', 'tornillos', 'tuercas'])
print(len(caja_A))  # 2

print(caja_A, [1])  # destornillador
print(caja_B, [0])  # clavos
~~~




## **¿Qué es un decorador de python?**  

Los **decoradores** son funciones que modifican el comportamiento de otras funciones, y nos permite optimizar y acortar los codigos. Se les identifica por la presencia de **@** a la hora de implementarlo en la funcion que queremos. En resumen, los decoradores son funciones que reciben otras funciones como parametros, y te devuelven una cosa diferente.  
Imaginemos que queremos una calculadora que nos presente los resultados:
~~~
def calcu_deco(funcion):
    def wrapper(arg1, arg2):
        a = arg1
        b = arg2
        print("Calculando...")
        result = funcion(a, b)
        print("Calculo completado.")
        return result
    return wrapper

@calcu_deco
def suma(a, b):
    return a + b

print(suma(5, 10))
~~~
 
 Y el resultado de esta funcion seria:

 ~~~
Calculando...
Calculo completado.
15
 ~~~

Primero realizara el print de la decoracion, y luego se hara la funcion que tenga el decorador puesto.  

Por otra parte, un truco para realizar o programar los decoradores es seguir los siguientes pasos:  

+ Primero declaramos la funcion a decorar, en este caso 'suma'
+ Luego pensamos en como decorarla, y nos fijamos en los argumentos que acoge esa funcion, em este caso queriamos que presentara el calculo de una manera distinta. 
+ Una vez codificado el decorador, es muy importante poner la linea que decora la funcion(@calcu_deco)

Hecho esto, si el codigo esta correcto y todos los argumentos estan en orden, deberia funcionar sin problemas. Pero, y que pasaria si en esa suma quisieramos sumar valores indeterminados. Pues en ese caso podemos usar *args y **kwargs, como por ejemplo, la misma suma de antes, que podria recibir una cantidad de argumentos indeterminada:

~~~
def calcu_deco(funcion):
    def wrapper(*args):
        print("Calculando...")
        result = funcion(*args)
        print("Calculo completado.")
        return result
    return wrapper

@calcu_deco
def suma(*args):
    return sum(args)

print(suma(5, 10, 10))
~~~

Y el resultado de esta funcion seria el siguiente:

~~~
Calculando...
Calculo completado.
25
~~~

En conclusion, los decoradores son muy versatiles a la hora de modificar unas funciones mas simples, y que con una simple linea(@calcu_deco), podemos crear una funcion decoradora y llamarla desde la parte del codigo que la necesitemos y asi ahorrar lineas de codigo y posibles errores.
