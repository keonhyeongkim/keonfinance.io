#!python
print( 'Content-Type: text/html' )
print()
import cgi
form = cgi.FieldStorage()
a = { 'fm':'Factor Models',
      'dl':'Data Library',
      'ci':'Contact Info.' }
if 'id' in form:
    pageId = form['id'].value
    dataName = 'data/' + pageId + '.html'
    description = open( dataName, 'r' ).read()
    headTitle = a[ pageId ]
    bodyTitle = a[ pageId ]
else:
    description = open( 'data/motivation.html', 'r' ).read()
    headTitle = 'Welcome'
    bodyTitle = 'Motivation of This Project'
print( '''
<!doctype html>
<html>
<head>
  <title>Keon's Financial Data - {ht}</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">Keon's Financial Data</a></h1>
  <ul>
    <li><a href="index.py?id=fm">Factor Models</a></li>
    <li><a href="index.py?id=dl">Data Library</a></li>
    <li><a href="index.py?id=ci">Contanct Info.</a></li>
  </ul>
  <h2>{bt}</h2>
  {desc}
</body>
'''.format( ht = headTitle,
            bt = bodyTitle,
            desc = description ) )
