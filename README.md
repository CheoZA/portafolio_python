# Portafolio

## Requerimientos

Es necesario python en su version 3, en mi caso tengo python 3.9.4.

Para instalar las librerias necesarias para que el proyecto funcione es necesario desde la consola ir al directorio de este proyecto y ejecutar el siguiente comando:

```shell
   > pip install -r requirements.txt
```

De tal manera que pueda PIP (manejador de paquetes de python) instalar todas las librerias definidas en el archivo "requirements.txt" de la raíz del proyecto.

## Iniciar proyecto

Primero habria que ejecutar esto en la consola para que generar la base de datos.

```shell
   > python manage.py makemigrations
```

Y luego el siguiente:

```shell
   > python manage.py migrate
```


Para iniciar el proyecto correr los siguientes comandos en dos consolas distintas

Para correr que los cambios realizados en código se refresquen en tiempo real.

```shell
   > python manage.py livereload
```

Para desplegar el servidor de aplicaciones.

```shell
   > python manage.py runserver localhost:80
```
