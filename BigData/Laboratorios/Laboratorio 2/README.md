# Titulo

Laboratorio 2 Bigdata

# Autor

Juan Sebastián Sanín Villarreal

# Descripción

Instalación y uso de manera local en VS de MRJob, en donde se utilizó como base el archivo de dataempleados para responder las preguntas definidas. Principalmente es plasmar el uso de MapReduce en estos 3 ejercicios practicas.

# Diseño

Implementación de repositorio de bigdata dado por el profesor. Programación en python con uso de la biblioteca de MRJob la cual es una interfaz de MapReduce.

# Instalación

Se deberá clonar este repositorio en su respectiva máquina, para así ejecutar los 3 programas que se encuentran en la carpeta de Programas y también deberá instalar MRJob.

## Comando:
  `sudo yum install git`
  
  `git clone https://github.com/sanin08/ST0263jssaninv.git`
  
  `sudo pip3 install mrjob`
  
También se tiene el archivo dataempleados.txt que nos sirve para simular el uso de lso datos
  
 # Ejecución
 
 Entrar a la carpeta descrita anterior mente la cual seria: ST0263jssaninv/BigData/Laboratorios/Laboratorio 2/Programas/
 
 Luego de estar parados en esta carpeta tendremos que escribir los siguientes comandos para ejecutar los programas (tener en cuenta que tenia problemas con mi ejecución ya que el debía hacer mi comando con python más no con python3):
 
1. Salario promedio por sector económico.
 
   `python3 dane-mr.py ../../datasets/otros/dataempleados.txt`

2. El salario promedio por Empleado.

    `python3 empleado.py ../../datasets/otros/dataempleados.txt`
 
3. Número de sector económico por Empleado que ha tenido a lo largo de la estadística.
 
   `python3 sector.py ../../datasets/otros/dataempleados.txt`
