# challenge

Este repo contiene los siguientes scripts:

  *  pycurl-http.py (Solo GET)
  *  pycurl-https.py
  *  ntp-traffic.py
  *  http_https_traffic_generator.py (Se trae las paginas completas)
  *  capturing_v1.py

  pycurl-http: Recorre un diccionario con sitios realizando un simple GET de los mismos utilizando la libreria request de python.

  pycurl-https: Recorre un diccionario con sitios HTTPs realizando un simple GET de los mismos utilizando la misma libreria que en pycurl-http.

  ntp-traffic: Es el mismo caso que ambos pycurl pero utilzando la libreria ntplib de python para realizar request a los ntpservers designados.

  http_https_traffic_generator: En este caso utilice urllib2 para traer el contenido completo, simplemente otra forma de generar trafico, para el caso de uso seria lo mismo que usar pycurl-http.

  capturing_v1: Este script realiza una captura de trafico hasta 10000 paquetes mediante pyshark donde solamente guardo los siguientes campos de mi interes:

          1) Número del paquete capturado.
          2) Tamaño del paquete en bytes.
          3) Datetime de la captura del paquete.
          4) Timestamp del paquete.
          5) IP de origen
          6) Puerto origen
          7) IP de Destino
          8) Puerto Destino
          9) Cuando se encuentra presente el host donde se intentan conectar los clientes.


Luego proceso los datos capturados para generar 3 archivos json con los datos interesantes en las siguientes categorias:

          A) clients_vs_sites --> En el mismo espero encontrar una relacion entre los clientes y los sitios visitados.
          B) traffic_by_protocol --> En el mismo obtengo una estadistica de uso por protocolo.
          C) top_sites --> Sitios visitados.
          D) Un archivo con el siguiente formato de nombre: "%H%M%S-%d%m%Y". Donde se guardan todos los paquetes capturados.


Los comando de ejecucion para los scrips son los siguientes:

(En todos los casos el ultimo parametro significa la cantidad de veces que voy a realizar el GET, o el NTP request.)

pycurl-http:
            python pycurl-http 10

pycurl-https:
            python pycurl-https.py 20

ntp-traffic:
            python ntp-traffic.py 15

http_https_traffic_generator:
            python http_https_traffic_generator.py 12

capturing_v1.py:
          python capturing_v1.py --list  (List las interfaces donde ser pueden realizar capturas)

          sudo python capturing_v1.py --nic "inteface de interes" (realiza la captura en la interfaz especificada)

          sudo python capturing_v1.py --nic wlp2s0 --dump (ademas de la interface donde capturar con la opcion dump generamos los 4 archivos json descritos previamente)

          Existe una cuarta opcion para este comando que sirve para leer un archivo pcap y se utiliza de la siguiente manera:

            sudo python capturing_v1.py --file capture.pcap

Para realizar mas facil la captura y si se cuenta con docker instalado se puede ejecutar desde dentro de la carpeta del repo el siguiente comando:

      docker build -t python:2.7-challenge .

Luego ejecutar:

      docker run -v /home/user/challenge:/root/challenge --net "host" python:2.7-challenge

El resultado es que tendremos 4 archivos en nuestro home dentro de la carpeta challenge que es la que generamos luego de clonarnos el repo.
