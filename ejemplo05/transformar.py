import pandas as pd
import json

def csv_a_json(ruta_csv, ruta_json, separador=',', orient='records', indent=4):
    """
    Convierte un archivo CSV a JSON.

    Parámetros:
    - ruta_csv: str -> Ruta del archivo CSV de entrada
    - ruta_json: str -> Ruta donde se guardará el archivo JSON
    - separador: str -> Separador del CSV (por defecto ',')
    - orient: str -> Orientación del JSON (default: 'records', otras: 'columns', 'index', etc.)
    - indent: int -> Espacios de indentación en el JSON

    Más info sobre orientaciones aquí: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html
    """

    try:
        df = pd.read_csv(ruta_csv, sep=separador)
        df.to_json(ruta_json, orient=orient, indent=indent, force_ascii=False)
        print(f"✅ Conversión completada. Archivo JSON guardado en: {ruta_json}")
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso:
if __name__ == "__main__":
    csv_a_json(
        ruta_csv="datos.csv",         # Cambia esto por tu archivo
        ruta_json="datos.json",       # Y esto por donde quieras guardarlo
        separador='|',                # Cambia si tu CSV tiene otro separador
        orient='records',             # Puedes usar 'columns', 'index', etc.
        indent=2                      # Para que el JSON sea más bonito
    )
