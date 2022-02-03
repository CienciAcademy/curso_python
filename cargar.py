from os import sep
import pandas as pd

df = pd.read_csv('datos-venta.csv', sep=';')
df1 = pd.read_excel("datos-venta.xlsx")
#incluso se puede escoger las hojas del excel
df2 = pd.read_csv('datos-venta.txt', sep="\t")
#tambien se puede abrir con fwf pero hay ciertas

#Ya sabemos abrir un archivo, ahora queremos controlar las columnas
variable = df['Nombre']
#nombre de las columnas o headers
#print(df.columns.values.tolist()) 

#filtrar las ventas de juan 
#df['Nombre']=='Juan' un "listado" true and false
#Estas son las ventas de juan -> print(df.loc[df['Nombre']=='Juan'])
# print(len(df.loc[(df['Nombre']=='Juan') & (df['Producto']=='Celular')].index))
# print(len(df.loc[(df['Nombre']=='Juan') & (df['Producto']=='Cargador')].index))
# print(len(df.loc[(df['Nombre']=='Juan') & (df['Producto']=='Bateria')].index))
# print(len(df.loc[(df['Nombre']=='Juan') & (df['Producto']=='Audifonos')].index))
ventas_juan = df.loc[df['Nombre']=='Juan']
print("venta juan: %3f",ventas_juan['Precio final'].sum())
ventas_juan = df.loc[df['Nombre']=='Maria']
print("venta maria: %3f",ventas_juan['Precio final'].sum())