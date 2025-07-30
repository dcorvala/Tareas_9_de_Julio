# abre el archivo .dbf

from dbfread import DBF
import pandas as pd
table = DBF('C:\TABIVA.dbf', load=True)

# Itera sobre los registros y haz algo con ellos
for record in table:
    print(record)

db = pd.DataFrame(iter(table))

db = pd.DataFrame(table, columns=["NUMERO", "DESCRIP", "PORCENT1", "PORCENT2"])
# db.loc[db["NUMERO"] = 6, "PORCENT1"] = 0
agregar = {
    "NUMERO": 7,
    "DESCRIP": "ESPECIAL",
    "PORCENT1": 10.50,
    "PORCENT2": 5.25
}

db = db.append(agregar, ignore_index=True)
db=db.sort_values(by='NUMERO')
print(db)

db.to_excel("TABLAIVA.xlsx", index=False)   

from simpledbf import Dbf5

# Create a Dbf5 object from the DataFrame and save it
output_dbf_path = "" # Replace with your desired output DBF file path
Dbf5("TABLAIVA.xlsx").to_dbf