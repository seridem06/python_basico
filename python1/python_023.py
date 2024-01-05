#verifica si una palabra es palindromo
palabra = 'radar'
es_pa = palabra == palabra[::-1]

print(palabra,"es palindromo",es_pa)