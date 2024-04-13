import psycopg2
from tkinter import messagebox

def abrirConexiones():
    conexionOrigen = psycopg2.connect(
        user='postgres',
        password='Tec19260974',
        host='localhost',
        port='5432',
        database='sales'
    )

    conexionDestino = psycopg2.connect(
        user = 'postgres',
        password = 'Tec19260974',
        host = 'localhost',
        port = '5432',
        database = 'prueba'
    )

    return conexionOrigen, conexionDestino

def cerrarConexiones(conexionOrigen, conexionDestino):
    #Cierra las conexiones a las bases de datos
    conexionOrigen.close()
    conexionDestino.close()

def cargaDatos(conexionOrigen, conexionDestino):
    cursorOrigen = conexionOrigen.cursor()
    cursorDestino = conexionDestino.cursor()

    sqlClient = 'SELECT first_name, country, job_title FROM client;'
    cursorOrigen.execute(sqlClient)
    registrosEnClient = cursorOrigen.fetchall()
    n = 0
    try:
        for registro in registrosEnClient:
            n += 1
            id_client = n
            first_name = registro[0]
            country = registro[1]
            job_title = registro[2]

            consultaInsertarDimClient = '''INSERT INTO public."dimclient"(id_client, first_name, country, job_title) VALUES (%s, %s, %s, %s);'''
            insertValues = (id_client, first_name, country, job_title)
            cursorDestino.execute(consultaInsertarDimClient, insertValues)

        sqlProduct = 'SELECT product FROM product;'
        cursorOrigen.execute(sqlProduct)
        registrosEnProduct = cursorOrigen.fetchall()
        n = 0
        for registro in registrosEnProduct:
            n += 1
            id_product = n
            product = registro[0]
            consultaInsertarDimProduct = '''INSERT INTO public."dimproduct"(id_product, product) VALUES (%s, %s);'''
            insertValues = (id_product, product)
            cursorDestino.execute(consultaInsertarDimProduct, insertValues)

        sqlCard = 'SELECT card FROM card;'
        cursorOrigen.execute(sqlCard)
        registrosEnCard = cursorOrigen.fetchall()
        
        n = 0
        for registro in registrosEnCard:
            n += 1
            id_card = n
            card = registro[0]
            
            consultaInsertarDimCard = '''INSERT INTO public."dimcard"(id_card, card) VALUES (%s, %s);'''
            insertValues = (id_card, card)

            cursorDestino.execute(consultaInsertarDimCard, insertValues)


        sqlSale = 'select s.date_sale, s.sale_paid, s.articles, cl.first_name, p.product, c.card from sale s, card c, client cl, sale_product sp, product p where s.id_card = c.id_card and c.id_client = cl.id_client and s.id_sale = sp.id_sale and sp.id_product = p.id_product;'
        cursorOrigen.execute(sqlSale)
        registrosEnSale = cursorOrigen.fetchall()
        
        n = 0

        for registro in registrosEnSale:
            n += 1
            print(n)
            id_sale = n
            date_sale = registro[0]
            sale_paid = registro[1]
            articles = registro[2]
            first_name = registro[3]
            product = registro[4]
            card = registro[5]

            #dimClient
            sqlAux = f"select id_client from dimclient where first_name = '{first_name}';"
            #values = (first_name)
            cursorDestino.execute(sqlAux)
            registroAux = cursorDestino.fetchone()
            id_client = registroAux[0]

            #dimProduct
            sqlAux2 = f"select id_product from dimproduct where product = '{product}';"
            cursorDestino.execute(sqlAux2)
            registroAux2 = cursorDestino.fetchone()
            id_product = registroAux2[0]

            #dimCard
            sqlAux3 = f"select id_card from dimcard where card = '{card}';"
            cursorDestino.execute(sqlAux3)
            registroAux3 = cursorDestino.fetchone()
            id_card = registroAux3[0]

            id_date = n
            consultaInsertarDimDate = '''INSERT INTO public."dimdate"(id_date, date_sale) VALUES (%s, %s);'''
            insertValuesAux = (id_date, date_sale)
            cursorDestino.execute(consultaInsertarDimDate, insertValuesAux)

            consultaInsertarFactSale = '''INSERT INTO public."factsale"(id_sale, id_client, id_card, id_product, id_date, sale_paid, articles) VALUES (%s, %s, %s, %s, %s, %s, %s);'''
            insertValues = (id_sale, id_client, id_card, id_product, id_date, sale_paid, articles)
            cursorDestino.execute(consultaInsertarFactSale, insertValues)

        conexionDestino.commit()  

        messagebox.showinfo("CORRECTO", "Se han almacenado los datos")
   
    except (Exception, psycopg2.Error) as error:
        print(error)
        messagebox.showerror("ERROR", error)

    finally:
        cursorOrigen.close()
        cursorDestino.close()


