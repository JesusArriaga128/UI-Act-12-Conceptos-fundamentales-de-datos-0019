# ============================================
# ACTIVIDAD 12 - CONCEPTOS FUNDAMENTALES DE DATOS
# Número de lista: 5
# Jesus Arriaga 
# NC = 0019
# ============================================

# --------------------------------------------
# 1. Crear el dataset correspondiente
#    al número de lista 5
# --------------------------------------------
import pandas as pd
print(pd.__version__)
datos5 = {
    'distancia_km': [2.1, 5.5, 1.8, 4.2, 3.0],
    'trafico_nivel': [2, 2, 1, 3, 2],
    'edad_repartidor': [31, 26, 43, 34, 23],
    'tiempo_entrega_min': [18, 45, 12, 38, 22]
}

# Crear DataFrame
df = pd.DataFrame(datos5)

# --------------------------------------------
# 2. Mostrar todos los datos
# --------------------------------------------

print("============================================")
print("DATOS COMPLETOS")
print("============================================")
print(df)

# --------------------------------------------
# 3. Separar las variables de entrada (X)
#    y la variable objetivo (y)
# --------------------------------------------

X = df[
    ['distancia_km',
     'trafico_nivel',
     'edad_repartidor']
]

y = df['tiempo_entrega_min']

# --------------------------------------------
# 4. Mostrar las Features (X)
# --------------------------------------------

print("\n============================================")
print("DATOS DE ENTRADA - FEATURES (X)")
print("============================================")
print(X)

# --------------------------------------------
# 5. Mostrar el Target (y)
# --------------------------------------------

print("\n============================================")
print("VARIABLE OBJETIVO - TARGET (y)")
print("============================================")
print(y)

# --------------------------------------------
# 6. Mostrar las primeras dos filas de X
# --------------------------------------------

print("\n============================================")
print("PRIMERAS 2 FILAS DE X")
print("============================================")
print(X.head(2))

# --------------------------------------------
# 7. Mostrar las primeras dos filas de y
# --------------------------------------------

print("\n============================================")
print("PRIMERAS 2 FILAS DE y")
print("============================================")
print(y.head(2))

# --------------------------------------------
# 8. Información del DataFrame
# --------------------------------------------

print("\n============================================")
print("INFORMACIÓN DEL DATAFRAME")
print("============================================")
print(df.info())

# --------------------------------------------
# 9. Estadísticas básicas
# --------------------------------------------

print("\n============================================")
print("ESTADÍSTICAS BÁSICAS")
print("============================================")
print(df.describe())
print("Programa realizado por Jesus Arriaga 0019")