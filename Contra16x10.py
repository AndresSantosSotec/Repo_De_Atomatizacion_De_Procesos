from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Configurar opciones de Edge (sin el argumento headless)
edge_options = Options()

# Ruta al Edge WebDriver
driver_path = 'C:/Users/A2905/OneDrive/Escritorio/edgedriver_win64/msedgedriver.exe'

# Crear una instancia del navegador Edge
driver = webdriver.Edge(service=EdgeService(driver_path), options=edge_options)

# Abrir la página del generador de contraseñas
driver.get("https://www.roboform.com/es/password-generator")

# Esperar hasta que el campo del número de caracteres esté presente
wait = WebDriverWait(driver, 10)
number_of_characters_field = wait.until(EC.presence_of_element_located((By.ID, "number-of-characters")))

# Usar JavaScript para asegurarse de que el campo esté vacío antes de escribir "16"
driver.execute_script("arguments[0].value = '';", number_of_characters_field)
number_of_characters_field.send_keys("16")

# Lista para almacenar todas las contraseñas generadas
all_passwords = []



# Ejecutar el ciclo para generar 10 contraseñas
for i in range(10):
    # Encontrar el botón para generar la contraseña y hacer clic
    generate_button = driver.find_element(By.ID, "button-password")
    generate_button.click()

    # Esperar a que la nueva contraseña sea generada
    time.sleep(2)  # Se puede ajustar el tiempo según el rendimiento de la página

    # Obtener la contraseña generada
    password_field = driver.find_element(By.ID, "text-password")
    generated_password = password_field.get_attribute('value')

    # Agregar la contraseña a la lista
    all_passwords.append(generated_password)

    # Imprimir la contraseña generada en cada iteración
    print(f"Contraseña generada {i+1}: {generated_password}")

# Guardar todas las contraseñas en un archivo de texto
with open("contraseñas_16_caracteres_serie.txt", "a") as file:
    for password in all_passwords:
        file.write(password + "\n")

# Si prefieres guardar en Excel
passwords = {'Contraseña': all_passwords}
df = pd.DataFrame(passwords)
df.to_excel("contraseñas_16_caracteres_serie.xlsx", index=False)

# Cerrar el navegador
driver.quit()
