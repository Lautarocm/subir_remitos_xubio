from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from obtener_datos_remito import remitos

# INICIALIZANCO WEBDRIVER
options = Options()

options.add_argument("window-size=1100,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")


service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

url = "https://xubio.com/NXV/newLogin"



def abrir_pagina():
    driver.get(url)



def nueva_venta():
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID,"header")))
    driver.get("https://xubio.com/NXV/ventas/nuevo-comprobante-de-venta")



def seleccionar_de_dropdown():
    dropdown = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,"fafselector")))



def completar_cliente():    
    contenedor_input_cliente = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME,"wdg_Organizacion")))
    input_cliente = WebDriverWait(contenedor_input_cliente, 5).until(EC.presence_of_element_located((By.TAG_NAME,"input")))
    input_cliente.send_keys("CENCOSUD")
    dropdown_cliente = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,"fafselector")))
    cliente = WebDriverWait(dropdown_cliente,5).until(EC.presence_of_element_located((By.TAG_NAME,"tr")))
    cliente.click()



def abrir_mas_opciones():
    boton_mas_opciones = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.NAME,"wdg_MasOpciones")))
    boton_mas_opciones.click()



def completar_vendedor():    
    contenedor_input_vendedor = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME,"wdg_Vendedor")))
    input_vendedor = WebDriverWait(contenedor_input_vendedor,5).until(EC.presence_of_element_located((By.TAG_NAME,"input")))
    input_vendedor.send_keys("Easy")
    dropdown_vendedor = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,"dataPanel")))
    vendedor = WebDriverWait(dropdown_vendedor,5).until(EC.presence_of_element_located((By.TAG_NAME,"tr")))
    vendedor.click()



def completar_comision():    
    contenedor_input_comision = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME,"wdg_PorcentajeComision")))
    input_comision = WebDriverWait(contenedor_input_comision,5).until(EC.presence_of_element_located((By.TAG_NAME,"input")))
    input_comision.clear()
    input_comision.send_keys("10")



def completar_observaciones():
    a="abcd"
    b="1234"
    input_observaciones = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME,"wdg_Descripcion")))
    input_observaciones.send_keys(
        f"OC ${a}\nRE{b}"
        )



def cargar_datos():
    completar_cliente()
    abrir_mas_opciones()
    completar_vendedor()
    completar_comision()
    completar_observaciones()



abrir_pagina()
nueva_venta()
cargar_datos()