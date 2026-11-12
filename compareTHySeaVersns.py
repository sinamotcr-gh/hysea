#!/usr/bin/env python3
"""
compare_netcdf.py

Compara dos archivos NetCDF (salidas de Tsunami-HySEA de distintas versiones)
utilizando la librería ncompare de NASA.

Reporta:
    - Diferencias estructurales (grupos, variables, dimensiones, atributos).
    - Diferencias en metadatos globales.

Uso:
    python compare_netcdf.py

Requisitos:
    pip install ncompare
"""

from ncompare import compare

def compare_hysea_outputs(file1_path: str, file2_path: str) -> int:
    """
    Compara dos archivos NetCDF usando ncompare.

    Args:
        file1_path (str): Ruta al primer archivo NetCDF (referencia / versión antigua).
        file2_path (str): Ruta al segundo archivo NetCDF (versión nueva).

    Returns:
        int: Número total de diferencias encontradas.
             Retorna 0 si los archivos son estructuralmente idénticos.

    Raises:
        FileNotFoundError: Si alguna de las rutas no existe.
        ImportError: Si ncompare no está instalado.
    """
    import os

    if not os.path.isfile(file1_path):
        raise FileNotFoundError(f"No se encontró el archivo: {file1_path}")
    if not os.path.isfile(file2_path):
        raise FileNotFoundError(f"No se encontró el archivo: {file2_path}")

    print("=" * 70)
    print(f"Archivo 1: {file1_path}")
    print(f"Archivo 2: {file2_path}")
    print("=" * 70)

    total_diffs = compare(
        file1_path,
        file2_path,
        only_diffs=True,        # Mostrar solo diferencias
        show_attributes=True,   # Incluir diferencias en atributos
        show_chunks=False,      # No comparar chunking (irrelevante aquí)
    )

    print("=" * 70)
    if total_diffs == 0:
        print("No se encontraron diferencias estructurales.")
    else:
        print(f" Total de diferencias encontradas: {total_diffs}")
    print("=" * 70)

    return total_diffs


if __name__ == "__main__":
    FILE1 = "/home/manuel/Tsunami-HySEA/costa_rica/NiCobano0.nc"
    FILE2 = "/home/manuel/Tsunami-HySEA/ejemplo_costa_rica/NiCobano0.nc"

    # NOTA: si trabajas dentro del Ubuntu remoto, las rutas deben ser
    # las del sistema de archivos de Ubuntu (p. ej. /home/manuel/...),
    # NO las rutas de macOS.

    compare_hysea_outputs(FILE1, FILE2)
