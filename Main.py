import pymssql
import streamlit as st

connection = pymssql.connect(
    server='192.168.2.14',
    user='HOC_Portal_DEV_User',   
    password='P@ss123!!',
    database='HOC_Employee_Portal_V2'
)

cursor = connection.cursor()
cursor.execute('SELECT * FROM employees')
result = cursor.fetchall()
print(result)
connection.close()


st.dataframe(result)

