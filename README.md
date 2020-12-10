# **P1 SCAV VIDEO**
En este repositorio se encuentras los ejercicios adjuntos de la primera práctica de codificacion de video de la asignatura para la Universidad Pompeu Fabra. 

## 1. Crear  un script de Python que permita convertir colores en RGB a YUB y viceversa. 
Al ejecutar el script por consola se dan distintas opciones de conversión. Después de elegir la que nos interas solo es necesario determinar los valores a convertir. 

## 2. Reescalar una imagen usando ffmpeg 
En este caso se han hecho pruebas con varias imagenes que pueden encontrarse en la carpeta resultados del repositorio.

Usando lo encontrado en la fuente [Traf.ffmeg](https://trac.ffmpeg.org/wiki/Scaling). 

Sabemos que para reescalar imagenes mediante ffmpeg podemos usar los siguientes comandos por consola, 
`ffmpeg -i input.jpg -vf "scale=iw*.5:ih*.5" input_half_size.png` 

`ffmpeg -i input.jpg -vf "scale=iw/2:ih/2" input_half_size.png`

Donde `iw` es el _input width_ y `ih` el _input height_. 

En nuestro caso ejecutamos el reescalado con los factores 2, 3 y 10. 

`ffmpeg -i abstract.jpg -vf "scale=iw/2:ih/2" abstract_2.png`
`ffmpeg -i abstract.jpg -vf "scale=iw/3:ih/3" abstract_3.png`
`ffmpeg -i abstract.jpg -vf "scale=iw/10:ih/10" abstract_10.png`

Como resultado obtenemos que el peso de la imagen original (72KB) se ve reducido a 26KB para el reescalado con factor 2, 14KB para el reescalado por factor 3 y 4K para el reescalado por factor 10. <br>

![original](./Resultados/abstract.jpg) 
![half_original](/Resultados/abstract_2.jpg)
![3_original](/Resultados/abstract_3.jpg)
![10_original](/Resultados/abstract_10.jpg)

## 3. Tranformar una imagen a blanco y negro usando FFMPEG

Para este ejercicio usamos la instrucción 

`ffmpeg -i abstract.jpg -vf hue=s=0 abstract_BW.jpg` 

Con esto lo que estamos indicando es que de la imagen que pasamos por referencia unicamente queremos quedarnos con la información de luminancia(Y) convirtiendo así nuestra imagen original en color a una imagen en blanco y negro. Esta imagen usa una compresión 4:2:0 o 4:0:0 (obteniendo el mismo resultado en KB), y su peso será de 52KB ya que no usamos toda la información de la imagen original. 

![original_BW_](/Resultados/abstract_BW_.jpg)

## 4. Implementacion del algoritmo Run Lenght
Este algoritmo codifica una secuencia de entrada mediante el calculo de la repeticion de simbolos.

Para ello usamos el [codigo](https://www.geeksforgeeks.org/run-length-encoding-python/) implementado en el script _run_length_algorithm_. 

Mediante el menu mostrado por consola podemos introducir la cadena de simbolos a la que aplicar el algoritmo. 

## 5. Codificador/Decodificador usando DCT
En este ejercicio se implementa el script _DCT.py_ en el que se pasa la imagen de referencia de Lenna y se aplica una compresion de 8 por defecto. Para ello usamos parte del [código](https://inst.eecs.berkeley.edu/~ee123/sp16/Sections/JPEG_DCT_Demo.html) en este scrypt. Como resultado obtenemos una imagen comparativa entre la original y la compresión. 
