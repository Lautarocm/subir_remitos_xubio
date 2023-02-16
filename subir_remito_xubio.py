from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import getpass
from datetime import date, time, datetime, timedelta
import time

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
    time.sleep(10)



def cargar_datos():
    fecha_factura = date.today()
    vencimiento_factura = fecha_factura + timedelta(25)
    
    contenedor_input_cliente = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME,"wdg_Organizacion")))
    input_cliente = WebDriverWait(contenedor_input_cliente, 5).until(EC.presence_of_element_located((By.TAG_NAME,"input")))
    
    time.sleep(10)
    
    # mas_opciones = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"")))
    
    # input_vendedor = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"")))
    
    # input_comision = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"")))
    
    # input_observaciones = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"")))




abrir_pagina()
nueva_venta()
cargar_datos()