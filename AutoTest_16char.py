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

# Encontrar el botón para generar la contraseña y hacer clic
generate_button = driver.find_element(By.ID, "button-password")
generate_button.click()

# Esperar a que la nueva contraseña sea generada
time.sleep(2)  # Se puede ajustar el tiempo según el rendimiento de la página

# Obtener la contraseña generada
password_field = driver.find_element(By.ID, "text-password")
generated_password = password_field.get_attribute('value')

# Imprimir la contraseña generada
print("Contraseña generada de 16 caracteres:", generated_password)

# Guardar en un archivo de texto
with open("contraseñas_16_caracteres.txt", "a") as file:
    file.write(generated_password + "\n")

# Si prefieres guardar en Excel
passwords = {'Contraseña': [generated_password]}
df = pd.DataFrame(passwords)
df.to_excel("contraseñas_16_caracteres.xlsx", index=False)

driver.quit()
