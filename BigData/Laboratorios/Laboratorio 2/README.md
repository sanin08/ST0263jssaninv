# Titulo

Laboratorio 2 Bigdata

# Autor

Juan Sebastián Sanín Villarreal

# Descripción

Instalación y uso de manera local en VS de MRJob, en donde se utilizó como base el archivo de dataempleados.txt para responder las preguntas definidas. Principalmente es plasmar el uso de MapReduce en estos 3 ejercicios prácticos.

# Diseño

Implementación de repositorio de bigdata dado por el profesor. Programación en python con uso de la biblioteca de MRJob la cual es una interfaz de MapReduce.

# Instalación

Se deberá clonar este repositorio en su respectiva máquina para así ejecutar los 3 programas que se encuentran en la carpeta de Programas y también deberá instalar MRJob.

## Comando:
  `sudo yum install git`
  
  `git clone https://github.com/sanin08/ST0263jssaninv.git`
  
  `sudo pip3 install mrjob`
  
También se tiene el archivo dataempleados.txt que nos sirve para simular el uso de los datos
  
 # Ejecución
 
 Entrar a la [CARPETA](https://github.com/sanin08/ST0263jssaninv/tree/main/BigData/Laboratorios/Laboratorio%202/Programas) descrita anteriormente la cual sería: ST0263jssaninv/BigData/Laboratorios/Laboratorio 2/Programas/
 
 Luego de estar sobre esta carpeta tendremos que escribir los siguientes comandos para ejecutar los programas (tener en cuenta que tenia problemas con mi ejecución ya que debía hacer mi comando con python más no con python3):
 
1. Salario promedio por sector económico.
 
   `python dane-mr.py ../../datasets/otros/dataempleados.txt`

2. El salario promedio por Empleado.

    `python empleado.py ../../datasets/otros/dataempleados.txt`
 
3. Número de sector económico por Empleado que ha tenido a lo largo de la estadística.
 
   `python sector.py ../../datasets/otros/dataempleados.txt`
