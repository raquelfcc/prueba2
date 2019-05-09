lista= ['Raquel','Judit','Ana','Marcos','David','Samuel']
cabecera="""
<!DOCTYPE html>
<html>
<body>

<ul style="list-style-type:square;">
"""
cierre="""
</ul>
</body>
</html>
"""
element=""
for elem in lista:
    element +=('<li>'+elem+'</li>\n')

content=cabecera+element+cierre
print(content)
