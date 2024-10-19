import mysql.connector

try :
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
    )

    mycursor = mydb.cursor()
    creat_DB = "CREATE DATABASE IF NOT EXISTS alx_book_store;"
    mycursor.execute(creat_DB)
except mysql.connector.Error as err :
    print(err)

finally:
    if mydb.is_connected() :
        print("Database 'alx_book_store' created successfully!")
        mycursor.close()
        mydb.close()
    else :
        print("not working")
        
    