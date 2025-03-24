import mysql.connector
from decimal import Decimal
from typing import List, Dict

"""
conn = mysql.connector.connect(
    host="localhost", #sostituisci l'indirizzo IP del server con il DB dentro
    user="root",
    password="",
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

    print(products)
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
"""

def search_products(
    title: str = None,
    min_quantity: int = None,
    max_price: float = None,
    in_stock: bool = None
) -> List[Dict]:
    """
    cursor = conn.cursor()
        
    query = "SELECT * FROM products WHERE 1=1"
    params = []

    if title:
        query += " AND title LIKE %s"
        params.append(f"%{title}%")
    if min_quantity is not None:
        query += " AND quantity >= %s"
        params.append(min_quantity)
    if max_price is not None:
        query += " AND price <= %s"
        params.append(max_price)

    cursor.execute(query, tuple(params))
    print(cursor.description)
    results = cursor.fetchall()
    """
    results = [(1, 'Smartphone', 50, Decimal('699'), 0), (4, 'Mouse Wireless', 75, Decimal('100'), 1), (11, 'ciao', 3, Decimal('10'), 11)]
    return results


if __name__ == '__main__':
    print(search_products(title="Smartphone"))