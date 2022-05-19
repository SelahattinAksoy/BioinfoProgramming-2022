#!/usr/bin/env python3
import cgi;
import cgitb;cgitb.enable()

print("Content-Type: text/html")
print()


form=cgi.FieldStorage()

id=form.getvalue("id")
type=form.getvalue("type")
db=form.getvalue("db")


print(f'''

idiniz : {id}
type : {type}
db : {db}

''')
