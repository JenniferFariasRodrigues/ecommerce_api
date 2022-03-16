import mysql.connector

con = mysql.connector.connect(host='localhost', database='db_meuslivros',user='root',password='100senha')
if con.is_connected():
    db_info=con.get_server_info()
    print("conectado ao servidor MySQL versão:", db_info)
    cursor = con.cursor()
    cursor.execute("Select database();")
    linha = cursor.fetchone()
    print("conectado ao banco de dados:",linha)
    
if con.is_connected():
    cursor.close()
    con.close()
    print("conexão ao MySQL foi encerrada!")