from selenium import webdriver
from selenium.webdriver.common.by import By

from mongo import MongoConnection

db_client = MongoConnection().client
db = db_client.get_database('autos')
col = db.get_collection('modelos')


driver = webdriver.Chrome()

#Abre la pág web de donde vamos a extraer los datos
url = 'https://autos.trovit.com.ec/autos/quito'
driver.get(url)

# Encuentra todos los elementos con la clase 'snippet-content'
elementos_snippet = driver.find_elements(By.CLASS_NAME, 'snippet-content')
# Imprime el modelo y el precio
for snippet_elemento in elementos_snippet:
    # Encuentra el elemento con la clase 'item-title' dentro del snippet (modelo)
    modelo_elemento = snippet_elemento.find_element(By.CLASS_NAME, 'item-title')
    modelo = modelo_elemento.text
    # Encuentra el elemento con la clase 'actual-price' dentro del snippet (precio)
    precio_elemento = snippet_elemento.find_element(By.CLASS_NAME, 'actual-price')
    precio = precio_elemento.text
    document = {
        "modelo": modelo_elemento.text,
        "precio" : precio_elemento.text
    }
    col.insert_one(document=document)
    # Imprime el modelo y el precio
    print(f'Modelo: {modelo}, Precio: {precio}')

# Cierra el navegador
driver.quit()
