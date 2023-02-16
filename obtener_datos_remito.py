import fitz
import pandas as pd

words = []

remitos = []

remito = {
    "orden": [],
    "productos": [],
    "precio": []
}



def obtener_palabras():
    global words

    doc = fitz.open("remitos/4397.pdf")
    page1 = doc[0]
    words = page1.get_text("words")



def ordenar_palabras():
    line_dict = {}
    words.sort(key=lambda w: w[0])

    for w in words:  
        y1 = round(w[3], 1)  
        word = w[4] 
        line = line_dict.get(y1, [])
        line.append(word)
        line_dict[y1] = line

    lines = list(line_dict.items())
    lines.sort()

    return lines



def crear_remito(lines):
    productos = []

    for l in lines:
        if ("JUMBO" or "EASY" or "EZEIZA" or "TORTUGUITAS" or "CUYO" or "CORDOBA" in l[1]):
            for numero in l[1]:
                if numero.isdigit() and (len(numero) == 9 or len(numero) == 10):
                    orden = numero
                    remito["orden"] = [orden]
        
        if len(l[1])>1 and (len(l[1][1]) == 11 or len(l[1][1]) == 7):
            unidades = l[1][0]
            sap = l[1][1]
            productos.append({"sap": sap, "unidades": unidades})

        if "$" in l[1]:
            precio = l[1][1]
            remito["precio"] = [precio]
    remito["productos"] = [productos]
    remitos.append(remito)



def crear_tabla_de_datos(remitos):
    # df = pd.DataFrame()
    # df["Orden"] = remitos[0]["orden"]
    # df.at[1, "Productos"] = remitos[0]["productos"]
    # df["Precio"] = remitos[0]["precio"]
    # print(df)

    df = pd.DataFrame(remitos[0])
    df.to_csv('final.csv',index=False, sep=";")
    print(df)



obtener_palabras()
ordenar_palabras()
crear_remito(ordenar_palabras())
crear_tabla_de_datos(remitos)