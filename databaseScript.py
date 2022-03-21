import mysql.connector

mydb=mysql.connector.connect(user='root',password='swarnim',
                               port='3306',
                               host='localhost',
                               database='attendance')
mycursor=mydb.cursor()


# function to create table in mysql database.
def create_data():
        mycursor.execute ("CREATE TABLE IF NOT EXISTS attendance  (fullname VARCHAR(255) not null , date_time datetime not null )")
        print('table created')
# function to insert data in mysql database.
def insert_data(name, datetime):

        sql="INSERT INTO attendance (fullname , date_time)values(%s, %s)"
        val=(name,datetime)
        mycursor.execute(sql, val)
        mydb.commit()


# fuction to fetch the data and prevent from overwtitting.
def exist_name(name, d1):
    mycursor.execute(f"SELECT fullname FROM attendance  where date_time between '{d1} 00:00:00' and '{d1} 23:59:59' ")
    row = mycursor.fetchall()
    print(row)
    for ro in row:
        if (name == ro[0]):
            return True
    return False

