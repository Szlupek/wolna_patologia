import psycopg2

connection = psycopg2.connect(database="wolna_patologia", user="szlup", password="", host="localhost", port=5432)

cursor = connection.cursor()
cursor.execute("create table visitor_ip (ip text, time text);")
#cursor.execute("drop table visitor_pi;")

aa = cursor.execute("SELECT * from visitor_ip;")
print(aa)
