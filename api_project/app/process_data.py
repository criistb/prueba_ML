import requests
import json

def process_data(input_file_path, output_file_path, api_url):
    # Leer el archivo JSON desde el path
    with open(input_file_path, 'r') as file:
        input_data = json.load(file)

    # Crear una lista para almacenar los resultados
    results = []

    # Enviar cada entrada del JSON a la API
    for entry in input_data:
        # Enviar la solicitud POST a la API
        response = requests.post(api_url, json=entry)
        
        # Verificar el estado de la respuesta
        if response.status_code == 200:
            result_data = response.json()  # Guardar el resultado en una variable
            results.append(result_data)  # Agregar el resultado a la lista
        else:
            print(f"Error {response.status_code}: {response.text}")
            results.append({'error': response.text})

    # Guardar los resultados en un archivo JSON
    with open(output_file_path, 'w') as file:
        json.dump(results, file, indent=4)

    print(f"Resultados guardados en '{output_file_path}'")

if __name__ == "__main__":
    input_file_path = 'input_data.json'   # Ruta al archivo JSON de entrada
    output_file_path = 'output_results.json'  # Ruta al archivo JSON de salida
    api_url = "http://127.0.0.1:8000/predict/"  # URL de la API

    process_data(input_file_path, output_file_path, api_url)