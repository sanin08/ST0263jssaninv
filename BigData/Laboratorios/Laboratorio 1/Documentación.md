# Titulo

Laboratorio 1 Bigdata

# Autor

Juan Sebastián Sanín Villarreal

# Descripción

Creación de un cluster con todas sus respectivos pasos (esto está resulto en el laboratorio 0) para la gestion de archivos en HUE en HDFS y aS3.

# Diseño

Cluster en AWS(EMR) con un bucket público en S3 de AWS llamado datasetsjssaninv.

# Instalación

* Iniciamos entrando en la URL que nos da el cluster de HUE como se muestra en la imagen 

![image](https://i.ibb.co/87T3W14/Inicial.png)

* Seguido nos encontramos con el login de Hue en donde crearemos nuestro respectivo usuario y contraseña (El usuario debería ser hadoop).

![image2](https://discuss.cloudxlab.com/uploads/default/original/2X/f/fefa1785d3eb4ff8584ee3cb09a040e3d18b7099.png)

* Creamos en el file Store una carpeta nos nuestro.

![image3](https://i.ibb.co/N1Qt3S5/1.png)

* Dentro de la carpeta con nuestro nombre crearemos una segunda carpeta llamada datasets
 
![image4](https://i.ibb.co/SmDkctL/2.png)

* Despues de crear las respectivas carpetas nos conectaremos al cluster (Se utilizó el programa putty para ingresar a la terminal) y por consola copiaremos el siguiente github para clonar el github en la carpeta de datasets (no olvidar instalar git)

**Para instalar git debemos hacer el siguiente comando:** `git yum intall git`
**Para clonar:** `git clone https://github.com/st0263eafit/st0263_20212.git`

* Ingresaremos ahora a la carpeta de datasets del github en la terminal y copiaremos sus datos en Hue en la carpeta de datasets.

`cd st0263_20212/bigdata/datasets/`
`hdfs dfs -copyFromLocal ./* /user/hadoop/datasets/`

Debe quedar de la siguiente forma:

![image5](https://i.ibb.co/VvLtYQ4/3.png)

* Otra forma que tenemos para verificar la copia de los datos es con los siguientes comandos en la terminar.

![image6](https://i.ibb.co/DQGSmdy/4.png)
![image7](https://i.ibb.co/hyxXB6k/5.png)

* Por ultimo en Hue haremos el envio de los datos a S3 y en este mismo getionador de archivos crearemos un bucket con el nombre de la siguiente forma datasets[usuario] para así crear una subcarpeta [usuario] y dentro de esta subcarpeta creamos otra subcarpeta llamada datasets.

![image8](https://i.ibb.co/ZGbXnKr/7.png)

![image9](https://i.ibb.co/7gRGSxQ/8.png)

**Comando para la copia de datos de hdfs a aS3:** `hadoop distcp /user/hadoop/datasets/* s3a://datasetsjppenaf/datasets/`

* Confirmamos el copiado de datos en aS3 si nos sale lo siguiente:

![image8](https://i.ibb.co/N3cnMmx/6.png)

(También lo podemos hacer entrando directamente en nuestro bucket de aS3)

![](https://i.ibb.co/bmFFJQ9/ultima.png)
