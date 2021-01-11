--------------------------------------Curso POO----------------------------------------------------

--------------------------------------Teoría-------------------------------------------------------

#POO: Paradigma que relaciona los problemas en objetos, como seria en la vida real.

#Objeto: Combinacion de propiedades o atributos que describen el objeto y una serie de metodos o acciones que puede ejecutar.

#Ejemplo: Una marcador es un objeto que se subdivide en otros objetos, como los son la punta, la tinta, el cuerpo. La POO, buesca trabajar con cada objeto individualmente para que no afecte a los demas objetos. En vez de pensar en el marcador como un objeto complejo, se piensa como una composición de objetos simples con funcionalidades especificas y sencillas.

#Clases: Son documentos donde se definen el comportamiento del objeto, sus propiedades y su función.

#Instancias: Es un objeto creado a partir de una clase.

#Estado: son un conjunto de valores almacenados que pueden ser modificados cuando el programa se ejecuta.

------------------------------Definir clase en Python-----------------------------------------------

class Curso: #llamando la clase con nombre "curso"
    pass     #Aqui se definen las clases
curso_python = Curso()  #Primer objeto, instancia de la clase "Curso"

------------------------------Propiedades de un objeto----------------------------------------------

#Son una coleccion de datos que el objeto guarda y tiene relacion con la tarea que tiene que realizar el objeto.
#Las propiedades de cada objeto son distintas entre ellos.
#Al valor de todas las propiedades de un objeto lo llamamos el estado del objeto.
#Pueden almacenar cualquier tipo de dato que el lennguaje permita.

--------------------------------Atributos en Python----------------------------------------------

class Usuario:  #llamando la clase con nombre "Usuario"
    nombre = "Anthony Vizcarrondo"  #Propiedad de la clase
                        #Colocando la propiedad, se asume que cualquier objeto que utilice la propiedad "nombre", arrojara como resultado "anthony vizcarrondo"
anthony = Usuario() #En este paso se  crea la instancia de la clase Usuario llamado "anthony"
print(anthony.nombre)

#Segunda forma de crear una propiedad a raiz de una instancia
alexander = Usuario() #Se crea la instancia de la clase Usuario llamado Alexander
alexander.nombre = "Alexander" 
print(alexander.nombre)

--------------------------------Métodos de un objeto----------------------------------------------

#Son funciones que le pertenecen a un objeto, modifican propiedad, retornan la propiedad o hacen calculos con los datos del objeto.

class Usuario:  
    nombre = "Anthony Vizcarrondo"  
    def saludar(self): #Definiendo método de la clase llamado "saludar".
        print("Hola, mi nombre es "+ self.nombre)  
        #Cuerpo del método, es donde se coloca las acciones que se deben de inciiar al mencionar el método.
anthony = Usuario() 
anthony.saludar() #Forma de ejecutar el método.

#Otra forma

class Usuario:  
    nombre = "Anthony Vizcarrondo"  
    def saludar(self, saludo): #Se define saludo como una variable.
        print(saludo + self.nombre)  
anthony = Usuario() 
anthony.saludar("Efectivamente, mi nombre es: ") #Forma de ejecutar el método.

 ----------------------------Método constructor--------------------------------------------

 #Este metodo se ejecuta de manera automatica cuando instanciamos una nueva clase, tiene un nombre ya definidio en el lenguaje.

 class Usuario:  
     def __init__(self,nombre): #Método constructor.
     self.nombre = nombre

    def saludar(self, saludo): 
        print(saludo + self.nombre)  

anthony = Usuario("Anthony Vizcarrondo") #Aca cuando creamos un nuevo objeto, se ejecuta automaticamente el método constructor.
anthony.saludar("Efectivamente, mi nombre es: ")

class Contador: 
    def __init__(self):
        self.conteo = 0

#Todas aquellas variables que se necesitan definir si o si al crear la clase, deben estar presentes en el método constructor, por ejemplo si un contador se necesita que su valor inicial siempre sea 0, se debe especificar con un método constructor como se muestra arriba.

#Tips: No realizar constructores muy complicados, sino que deben mantenerse simples para establecer la inicializacion de una clase
#Usarlo para inicializar el valor del objeto y nada más.

----------------------------------------Herencia----------------------------------------------------

#Herencia: Permite que un objeto herede propiedades de un Padre a uno hijo, en el cual se le puede añadir otras propiedades a partir de las existentes,  Nos permite ir de los más general a lo más específico.

#Ejemplo

#Animal (Padre)
#- Puede respirar
#- Puede reproducirse
#- Tiene una edad
#- Tiene una fecha de nacimiento

#Mamífero (Hijo)
#- Puede respirar
#- Puede reproducirse
#- Tiene una edad
#- Tiene una fecha de nacimiento
#- Puede amamantar
#- Tienen un periodo de gestación

#Perro (Específico)
#-Todas las propiedades de un Animal
#-Todas las propiedades de un mamífero

--------------------------------------Heredar entre clases------------------------------------------

class Usuario:  
     def __init__(self,nombre): 
     self.nombre = nombre

    def saludar(self, saludo): 
        print(saludo + self.nombre)  

class Empleado(Usuario): #La clase usuario se convierte en la clase "Padre" de la clase Empleado
    salario = 0          #Es decir, ahora en la clase Empleado se heredaron las propiedades dentro 
                         #de la clase Usuario y se pueden "reciclar" sin reescribirlo
    def modificar_salario(self.salario):
        self.salario = salario

    def ver_salario(self):
        print(self.salario)

empleado = Empleado("Anthony")
empleado.saludar("Hola!, me llamo: ")
empleado.modificar_salario(1000)
empleado.ver_salario()

--------------------------------Función super----------------------------------------------

#Se encarga de modificar las propiedades heredadas de la clase padre dentro de la clase hijo

class Pagina:
    def imprimir_pie_pagina(self):
        print(self.pie_pagina)

class PaginaLegal(Pagina):
    def imprimir_pie_pagina(self):
        print("Derechos reservados")
        super().imprimir_pie_pagina()

html = PaginaLegal()
html.pie_pagina = "<p>Hola</p>"

html.imprimir_pie_pagina()

----------------------------------Encapsulación------------------------------------------

#Encapsulación: En vez de exponer el objeto, o sea sus propiedades, se crean mecanismos que los muestren.
#Por ejemplo: En un telefono las configuraciones tienen parametros que limitan las capacidades del dispositivo, como lo es la opción de regular el brillo, la misma posee un limite establecido encapsulado, de no poseerlo, se le podría aumentar el brillo sin detenerse, provocando una falla en el sistema y que se dañe el dispositivo. 
#El encapsulamiento busca ofrecerle al usuario un módulo controlado que se pueda modificar, y el mismo modifique las propiedades sin salirse del parámetro establecido

#Visibilidad de la propiedad: Permite establecer los permisos de cuales usuarios pueden acceder a una propiedad de un objeto

#Formar de acceder a las propiedades:

#En la propia clase padre:

class Usuario:
    nombre = "Anthony"
    def mi_nombre(self):
        return self.nombre ----->Aqui

#Apartir de la clase padre, acceder en la clase hija:

class Usuario:
    nombre = "Anthony"

class Empleado(Usuario):
    def nombre(self):
        return self.nombre   ----> Aqui

#Desde la instancia:

empleado = Empleado()

empleado.nombre  --------- Aqui

#Propiedad pública: Se pueden acceder desde los 3 tipos de accesos

#Propiedad protegida: Se puede acceder solo desde la clase padre y desde la clase que se haya heredado, pero no se puede acceder desde la instancia

#Propiedad privada: Solo se puede acceder desde la clase padre, o sea la misma clase que lo declaró

#Métodos accesores
#Una sola propiedad debee poseer dos métodos accesores, los cuales son:

#Método Getter: Retorna el valor actual de la propiedad

#Método Setter: Modifica el valor de la propiedad

#Ejemplo: Si un dispositivo posee la función de ajustar el brillo, estos métodos facilitan la lectura y la modificación de dicha propiedad

#Tip: Antes de trabajar con los métodos accesores, se recomienda trabajar primero directamente con los atributos/propiedades, hasta que haya algo que nos oblige a hacer una modificación

#Ejemplo en Python:

class Empleado(Usuario): 
    __salario = 0          

    def modificar_salario(self.salario):  #Setter
        self.__salario = salario

    def ver_salario(self): #Getter
        print(self.__salario)

#Otra forma:

class Usuario:
    __edad = 0

@property     #Getter
def edad(self):
    return self.__edad

@edad.Setter   #Setter
def edad(self.valor):
    if(valor < 9):
        raise ValueError('Edad no puede ser menor que 0')
    self.__edad = valor

class Empleado(Usuario):
    __salario = 0

empleado = Empleado("Uriel")
empleado.edad = 26

#Tips: Todas las propiedades deben iniciarse siendo privadas, y solo se haran públicas al menos que se tenga un requirimiento especial

--------------------------------Abstracción------------------------------------------

#Es tomar un concepto o problema, ignorar los detalles y ver el problema de forma más general, no se discute el como, sino el porque.

#Significa ocultar detalles innecesarios y exponer lo esencial, para enfocarse en lo que hara el objeto y no como lo hace.

Ejemplo 1

class FilaBanco:
    usuarios = {}

    def siguiente_usuario(self,numero):
        #Implementación
        return usuarios[numero]

    def formar_usuario(self,numero,usuario):
        usuario[ticket] = usuario

Ejemplo 2

class Hash():
    datos = {}

    def obtener(self,llave):
        datos[llave]

    def agregar(self,llave,valor):
        datos[llave] = valor

#Hacen la misma función solo que el ejemplo 2 cumple con el paradigma de abstracción, ya que la implementación es muy general.
#Se recomienda ir desde lo muy general, como es lo abstractos, hasta lo más específicos que es ya la implementación

--------------------------------------------Polimorfismo------------------------------------------------------------------------

#Se le dice asi a la habilidad de un objeto de tomar varias formas
#Un objeto se considera polimorfico si pasa más de una prueba "Es un"

#Ejemplo

class User:

class Employee(user):

#Se dice que la clase Employee cumple una función polimorfica ya que puede tomar las propiedades de empleado y usuario

#Se utiliza normalmente en las interfaces, pero en el caso de Python se utiliza el Duck Typing

--------------------------------------------Examen----------------------------------------------------

1.- Qué nivel de alcance tiene una propiedad cuando podemos acceder a ella desde la clase misma que lo declaró y desde clases que hayan heredado:
R= protegida 

2.- Qué imprimirá el siguiente código:

class Page:
 def print_footer(self):
   print(“Hola”)

class LegalPage(Page):
 def print_footer(self):
   print("Mundo")-
   super().print_footer()

   R= Mundo Hola 

3.- Quiere decir que los datos y las funciones que manipulan estos datos se envían como una sola unidad:

R= Encapsulación

4.- Podemos decir que un objeto se puede considerar polimórfico sí:

R= Pasa más de una prueba "es un"

5.- Es una combinación de propiedades y atributos que lo describen, además de métodos y acciones que puede ejecutar:

R= Objetos

6.- Cuál es considerado el primer lenguaje de programación que implementa programación orientada a objetos

R= Simula

7.- Selecciona la que NO es una ventaja o característica de la herencia:

R= Permite crear objetos escribiendo menos codigo

8.- Significa ocultar detalles innecesarios y exponer únicamente lo esencial, de manera que te enfoques en qué es lo que hará el objeto, en lugar de cómo lo va a realizar:

R= Abstracción

9.- Imagina que estás implementando una clase para mostrar los cursos de un Plan de estudios, cuál de las siguientes implementaciones estaría usando abstracción:

R= class PlanEstudios:
  cursos = []

  def siguiente_curso(self):
    # Implementación
plan = PlanEstudios()
plan.siguiente_curso()

10.- Es una estrategia de la programación orientada a objetos para reciclar código

R= Composición

11.- Son documentos en los que se define el comportamiento del objeto, las propiedades que tiene y las acciones que puede realizar:

R= Clases

#12.- Cuál de estos NO es un paradigma de programación

#R= Prototipos 

13.- Tiene el propósito de guiar la implementación del lenguaje de programación, es un estilo o una forma de solucionar algo:

R= Un paradigma de programación

#14.- Qué es una instancia en programación orientada a objetos

#R= Una variable inicializada 

15.- Buscan definir la estructura de un objeto de manera general, sin definir los detalles de la implementación

R= Clases abstractas

16.- Los getters y setters son dos tipos de:

R= Métodos accesores

17.- Son los principios en los que se basa la programación orientada a objetos

R= Abtracción, encapsulación. heencia y polimorfismo

