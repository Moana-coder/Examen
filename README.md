# Examen:
<h1>Web Scrapping de Amazon1</h1>
Prueba final

Hola a todos!
>Esta práctica busca extraer información de precios de hoteles, habitaciones, disponibilidad de habitaciones; desde la página de BOOKING que es una plataforma de reserva de viajes y alojamiento con tarifas nacionales e internacionales.

Inicialmente había pensado hacer scrapping a Amazon pero no lo logré.. así que así llegamos a Booking. :D

Y algo me dice que tampoco terminaré esta práctica.... 

Ok. He vuelto en mi tercer intento!

<h1>Web Scrapping a Trovit </h1>
Trovit es un sitio de anuncios clasificados. ( Está en 51 países en todo el mundo, estando disponible en 19 idiomas y recibiendo más de 90 millones de visitantes únicos cada mes)
La información que recolectemos la vamos a almacenar de forma estructurada en una base de datos en la nube, tipo MongoDB (Mongo Atlas)

<h1>En qué consiste el Web Scrapping? </h1>
El web scraping es un conjunto de prácticas utilizadas para extraer automáticamente — o «scrapear» — datos de la web.

![Web Scrapping!](https://kinsta.com/wp-content/uploads/2022/07/Web-scraping.png "Web Scrapping")


Para esta práctica utilizaremos la librería Selenium.

<h2>Requerimientos 2</h2>
Para extraer datos con Selenium en Python, primero necesitarás instalar Selenium. Puedes hacerlo ejecutando el siguiente comando en tu terminal:


>pip install selenium
<h2>Configuración</h2>
Es necesario configurar las variables de entorno en un archivo .env:


>MONGO_USER=user
>
>MONGO_PASSWORD=password
>
>MONGO_HOST=cluster0.t2zotyt.mongodb.net****

El script de Python llamado nuevo.py es el que realiza web scraping en el sitio de Trovit. Este script abre la página web, espera a que se cargue y luego extrae datos de alojamientos y los guarda en la BD MOANABD.

