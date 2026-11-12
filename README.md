# hysea
# Análisis de Modelado Numérico de Tsunamis - Costas de Costa Rica

Este repositorio contiene una colección de scripts desarrollados para el procesamiento, análisis y visualización de resultados provenientes de simulaciones numéricas de tsunamis aplicadas a las costas de Costa Rica (litoral Pacífico y Caribe).

## Objetivo
Facilitar la evaluación de la amenaza por tsunami mediante herramientas automatizadas que permiten extraer parámetros clave del oleaje, tiempos de arribo, alturas máximas de inundación y series temporales en mareógrafos virtuales de interés.

## Requisitos previos
Para ejecutar estos scripts es necesario contar con:
* *Lenguaje:* [Python 3.x / MATLAB / R] (ajusta según el lenguaje que uses)
* *Librerías principales:* numpy, pandas, matplotlib, xarray, netCDF4 (modifica según tus dependencias)
* *Datos de entrada:* Archivos de salida de modelos numéricos (ej. COMCOT, GeoClaw, NEOWAVE, FUNWAVE) en formato .nc, .dat o .csv.

## Estructura del Repositorio

A continuación se presenta una introducción general a la organización de las carpetas y los scripts incluidos en este proyecto:

* */01_preprocesamiento*: Scripts destinados a la limpieza, recorte de grillas batimétricas/topográficas y preparación de condiciones iniciales para las costas de Costa Rica.
  * nombre_script_1.py: Breve descripción de lo que hace este archivo.
* */02_analisis_series*: Herramientas para extraer y procesar mareógrafos virtuales, calcular tiempos de llegada y amplitudes máximas.
  * nombre_script_2.py: Breve descripción de lo que hace este archivo.
* */03_mapas_inundacion: Códigos enfocados en el cálculo de alturas máximas de ola (*run-up), profundidades de flujo y generación de mapas de peligro.
  * nombre_script_3.py: Breve descripción de lo que hace este archivo.
* */04_visualizacion*: Scripts para la creación de gráficos, perfiles costeros y animaciones de propagación.
  * nombre_script_4.py: Breve descripción de lo que hace este archivo.

## Uso básico
1. Clona este repositorio en tu máquina local:
   bash
   git clone https://github.com
   
2. Configura las rutas de tus archivos de entrada dentro del script correspondiente.
3. Ejecuta el análisis desde la terminal:
   bash
   python ruta/al/script.py
   
