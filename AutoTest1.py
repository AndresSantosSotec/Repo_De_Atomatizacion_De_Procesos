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
# edge_options.add_argument("--headless")  # Esta línea se comenta o elimina para mostrar la ventana gráfica

# Ruta al Edge WebDriver
driver_path = 'C:/Users/A2905/OneDrive/Escritorio/edgedriver_win64/msedgedriver.exe'

# Crear una instancia del navegador Edge
driver = webdriver.Edge(service=EdgeService(driver_path), options=edge_options)

# Abrir la página del generador de contraseñas
driver.get("https://www.roboform.com/es/password-generator")

# Esperar hasta que el campo de la contraseña esté presente
wait = WebDriverWait(driver, 10)
password_field = wait.until(EC.presence_of_element_located((By.ID, "text-password")))

# Obtener la contraseña generada
generated_password = password_field.get_attribute('value')

# Imprimir la contraseña generada
print("Contraseña generada:", generated_password)

# Guardar en un archivo de texto
with open("contraseñas.txt", "a") as file:
    file.write(generated_password + "\n")

# Si prefieres guardar en Excel
passwords = {'Contraseña': [generated_password]}
df = pd.DataFrame(passwords)
df.to_excel("contraseñas.xlsx", index=False)

# Cerrar el navegador
driver.quit()
