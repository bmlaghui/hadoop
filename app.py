import json
from _csv import reader

import pandas as pd
from flask import Flask, render_template, jsonify, Response, redirect, request
from sqlalchemy import create_engine
import mysql.connector

app = Flask(__name__)

SECRET = {'username':'hive', 'password': 'cloudera'}
user_name = SECRET.get('username')
passwd = SECRET.get('password')

host_server = '192.168.177.128'
port = '10000'
database = 'Restaurants'
conn = f'hive://{user_name}@{host_server}:{port}/{database}'
engine = create_engine(conn, connect_args={'auth': 'NOSASL'})

dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="restaurants"
    )


@app.route('/')
def hello_world():
    query = "select * from restaurants"
    data = pd.read_sql(query, con=engine)
    print(data)

    #restosDatas = ["idrestaurant": "", "siretrestaurant": "", "nomrestaurant": "", "adresserestaurant":"", "note":""]
    # complementadresserestaurant (string)
    # codepostalrestaurant (string)
    # communerestaurant (string)
    # typeactiviterestaurant (string)
    # telephonerestarant (string)
    # emailrestaurant (string)
    # specialiterestaurant (string)
    # horairesrestaurant (string)
    # mobilitereduiterestaurant (string)
    # sitewebrestaurant (string)
    # geometryrestaurant (string)}

    retosDatas = []
    for item in data.values:
        if (float(note(item[0]))!=0):
            noteElement  = note(item[0])
        else:
            noteElement = "Non noté"
        retosDatas.append([item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14], noteElement])

        #else : restosDatas.append(item)
    print(retosDatas)
    data3 = data.values.tolist()
    # for resto in data3:
    #     print(resto)
    return render_template('index.html', listRestaurants = retosDatas, nbRestaurants = len(retosDatas))

@app.route('/rating')
def rate():
    return render_template('rating.html')

@app.route('/csv')
def csv():
    app.config['JSON_AS_ASCII'] = False

    import csv
    i = 0
    # read csv file as a list of lists
    with open('C:/Users/mlagh/Downloads/communes-dile-de-france-au-01-janvier.csv', 'r',  encoding="utf8") as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        arr = []
        for elem in list_of_rows:
            print ("<option value=0>"+str(elem)[2:len(str(elem))-2]+"</option>")
            arr.append('<option value="'+str(i)+'">'+str(elem)[2:len(str(elem))-2]+'</option>')
            i+=1
    response = Response(json.dumps(arr, ensure_ascii=False).encode("utf-8"), content_type="application/json; charset=utf-8")
    return response

@app.route('/retrieveData')
def datas():
    query = "select * from restaurants"
    data = pd.read_sql(query, con=engine)
    print(data)
    data3 = data.values.tolist()
    response = Response(json.dumps(data3, ensure_ascii=False).encode("utf-8"), content_type="application/json; charset=utf-8")
    return response

@app.route('/csvmysql')
def mysqldatas():
    query = "select * from restaurants"
    data = pd.read_sql(query, con=engine)
    data3 = data.values.tolist()


    # # preparing a cursor object
    # cursorObject = dataBase.cursor()
    # for item in data3:
    #     q = "INSERT INTO  restaurants VALUES ("+item[0]+", 0, 0, 0, 0, 0)"
    #     cursorObject.execute(q)
    # dataBase.commit()
    #
    # # disconnecting from server
    # dataBase.close()

    return "yes"

@app.route('/update', methods=['GET','POST'])
def update():
    id = request.form['id']
    print("id= "+str(id))
    cursorObject = dataBase.cursor()
    print(type(request.form["note"]))
    if request.form['note'] == "1" : q = "Update  restaurants set notea = notea +1 where id="+id
    elif  request.form['note'] == "2" : q = "Update  restaurants set noteb = noteb +1 where id="+id
    elif  request.form['note'] == "3" : q = "Update  restaurants set notec = notec +1 where id="+id
    elif  request.form['note'] == "4" : q = "Update  restaurants set noted = noted +1 where id="+id
    elif  request.form['note'] == "5" : q = "Update  restaurants set notee = notee +1 where id="+id

    cursorObject.execute(q)
    dataBase.commit()
    #
    # # disconnecting from server
    # dataBase.close()
    return redirect("/", code=200)


@app.route('/note/<id>')
def note(id):

    crsr = dataBase.cursor()

    # execute the command to fetch all the data from the table emp
    crsr.execute("SELECT id, notea as notea, noteb*2 as noteb, notec*3 as notec, noted*4 as noted, notee*5 as notee FROM restaurants where id="+id)

    # store all the fetched data in the ans variable
    ans = crsr.fetchone()

    # Since we have already selected all the data entries
    # using the "SELECT *" SQL command and stored them in
    # the ans variable, all we need to do now is to print
    # out the ans variable

    nb=0
    sumnote=ans[1]+ans[2]+ans[3]+ans[4]+ans[5]
    sumcoeff=ans[1]/1+ans[2]/2+ans[3]/3+ans[4]/4+ans[5]/5
    if sumcoeff==0: sumcoeff=1
    note = sumnote/sumcoeff
    #print("sum note= " + str(sumnote) + ", sumcoeff= " + str(sumcoeff) + ", id= " + str(id) + ", note="+str(note))
    return str(note)


if __name__ == '__main__':
    app.run()
