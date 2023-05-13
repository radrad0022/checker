from apps.check import blueprint
from flask import render_template, redirect, request, url_for
from flask_table import Table, Col
from . import mysql
import requests
import time

@blueprint.route('/gate1', methods=['POST'])
def gate1():
    lista = request.form['lista']
    gate = request.form['gate']
    linhaenviar = lista.split("\n")
    total = len(linhaenviar)
    tested = total
    ap = 0
    rp = 0
    up = 0
    value=""
    # send each credit card number in the list to the API endpoint using a loop and track the responses
    for index, value in enumerate(linhaenviar):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = {'value': value}
        req = requests.post(url=gate, data=payload, headers=headers)
        response_text = req.text
        
        if "Approved" in response_text:
            ap += 1
            tested -= 1
            cvvfunc(response_text)
        elif "LIVE CCN" in response_text:
            rp += 1
            tested -= 1
            ccnfunc(response_text)
        else:
            up += 1
            tested -= 1
            deadfunc(response_text)

        time.sleep(1) # wait 1 second between requests

    # pass the results to the template
    return render_template('result.html', value=value, ap=ap, rp=rp, up=up, total=total)

def cvvfunc(str):
    msg = str + '\n'
    with open('cvv_lives.txt', 'a') as f:
        f.write(msg)

def ccnfunc(str):
    msg = str + '\n'
    with open('ccn_approved.txt', 'a') as f:
        f.write(msg)

def deadfunc(str):
    msg = str + '\n'
    with open('declined_cc.txt', 'a') as f:
        f.write(msg)

# def getresult():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT * FROM results''')
#     data = cur.fetchall()
#     cur.close()

#     # Create an instance of the DataRow class for each row of data
#     table_data = [DataRow(row['id'], row['card'], row['result'], row['message'], row['userid']) for row in data]

#     return render_template('index.html', table_data=table_data)

# class DataRow(Table):
#     id = Col('ID')
#     card = Col('card')
#     result = Col('result')
#     message = Col('message')
#     userid = Col('userid')

# @blueprint.route('/')
# def route_default():
#     return getresult()