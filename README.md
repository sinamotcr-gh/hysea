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

* */01_utils*: scripts para visualización y análisis preliminar de inputs a los modelos.

