# -*- coding: utf-8 -*-
import scrapy

# Lista de estaciones: Extraida de  http://aire.nl.gob.mx/airemapbing/airebing.php >> Linea 87
lista_estaciones_web = [
    ['CENTRO', 25.67602, -100.335847, 4, 'Obispado',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=CENTRO', 'centro'],
    ['SURESTE', 25.66827, -100.249580, 2, 'Pastora',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=SURESTE', 'sureste'],
    ['NORESTE', 25.74543, -100.255020, 3, 'San Nicolás',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=NORESTE', 'noreste'],
    ['NOROESTE', 25.75712, -100.365974, 5, 'San Bernabé',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=NOROESTE', 'noroeste'],
    ['SUROESTE', 25.675674, -100.465018, 6, 'Santa Catarina',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=SUROESTE', 'Suroeste'],
    ['NOROESTE 2', 25.783456, -100.585874, 7, 'García',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=GARCIA', 'noroeste2'],
    ['NORTE', 25.80194, -100.343056, 8, 'Escobedo',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=NORTE', 'Norte'],
    ['NORESTE 2', 25.77722, -100.188055, 1, 'Apodaca',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=NORESTE2', 'noreste2'],
    ['SURESTE 2', 25.64611, -100.095555, 9, 'Juárez',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=SURESTE2', 'sureste2'],
    ['SUROESTE 2', 25.66528, -100.412778, 10, 'San Pedro',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=[SAN Pedro]', 'suroeste2'],
    ['SURESTE 3', 25.600874, -99.995298, 11, 'Cadereyta',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=SURESTE3', 'sureste3'],
    ['NORTE 2', 25.729787, -100.310028, 12, 'Universidad',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=NORTE2', 'norte2'],
    ['SUR', 25.575383, -100.249371, 13, 'Pueblo Serena',
     'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=SUR', 'sur']
]
# Extracto
lista_url_estaciones = ['http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=CENTRO',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=SURESTE',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=NORESTE',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=NOROESTE',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=SUROESTE',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=GARCIA',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=NORTE',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=NORESTE2',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=SURESTE2',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=[SAN Pedro]',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=SURESTE3',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=NORTE2',
                        'http://aire.nl.gob.mx:81/SIMA2017reportes/ReporteDiariosima.php?estacion1=SUR',
                        ]


class TablasSpider(scrapy.Spider):
    name = 'tablas'
    allowed_domains = ['aire.nl.gob.mx']
    start_urls = lista_url_estaciones

    def parse_item(self, response):
        for item in response.selector.xpath('div.body'):
            yield {
                # 'estacion': #/html/body/div[1]/section/div[2]/h3[1]
            }
