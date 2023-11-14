#Source: https://pythonspot.com/flask-hello-world/
#https://www.dataquest.io/blog/tutorial-connect-install-and-query-postgresql-in-python/
from flask import Flask
import psycopg2
app = Flask(__name__)

connection = psycopg2.connect(database="default_database",
                        host="database",
                        #extremely dumb idea for real application, don't do this ... pretty please
                        user="postgres",
                        password="postgres",
                        port="5432")    #default Postgres

@app.route("/")
def hello():
    #as per: https://stackoverflow.com/questions/44405708/flask-doesnt-print-to-console
    print("Użytkownik odwiedził stronę główną.", flush=True)
    return "<h1>Hello World!</h1>"

@app.route("/data")
def data():
    #as per: https://stackoverflow.com/questions/44405708/flask-doesnt-print-to-console
    print("Użytkownik odwiedził stronę data.", flush=True)
    data=""
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM data_table")
        data=cursor.fetchall()
        connection.close()
    except:
        data="Error connecting to database"
    return data

if __name__ == "__main__":
    app.run()