from sql_connection import get_sql_connection  #importing fromsql.connection.py

def get_all_products(connection): #for getting list of products
    cursor=connection.cursor() 
    
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit," #SQL QUERY WITH INNER JOIN
             "uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    
    cursor.execute(query)
    
    response = []
    
    for (product_id, name, uom_id, price_per_unit, uom_name)in cursor:
        response.append(
        {
            'product_id': product_id,
            'name': name,                      #LIST OF ITEMS
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        }
    )       
    return response
def insert_new_product(connection, product):#for insertion of new item in products table
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"  #SQL QUERY
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection,product_id): #for deletion of an item in products table
    cursor=connection.cursor()
    query=("delete from products where product_id=" +str(product_id)) # SQL QUERY
    cursor.execute(query)
    connection.commit()
    
    return cursor.lastrowid

if __name__=='__main__':
    connection=get_sql_connection()
    #print(get_all_products(connection))
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '1',
        'price_per_unit': 10
    }))
    