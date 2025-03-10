import mysql.connector
from getpasswd import *
from decimal import Decimal

conn = mysql.connector.connect(
    host="localhost", #sostituisci l'indirizzo IP del server con il DB dentro
    user="root",
    password=getpass(),
    database="pnrr_new_pon",
    port=3306, #porta default di mySQL
    )

# a tutti passerei un dizionario così che dentro abbia le informazioni per presonalizzare le query 
def db_get_products(diz):
    cur = conn.cursor()

    # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
    query = "SELECT * FROM products"
    cur.execute(query)
    dati = cur.fetchall()

    column_names = [desc[0] for desc in cur.description]

    # Converte le tuple in dizionari
    products = []
    for row in dati:
        product = {column_names[i]: (float(row[i]) if isinstance(row[i], Decimal) else row[i]) for i in range(len(row))}
        products.append(product)

    cur.close()
    conn.close()
    return products

def db_set(diz): 
    # query di insert
    pass

def db_update(diz):
    # query update
    pass

def db_delete(diz):
    # query delete
    pass


if __name__ == '__main__':
    db_get_products({})