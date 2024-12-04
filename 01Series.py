#series é tipo uma coluna é uma tabela aka um array com uma dimensão 

import pandas as pd

a = [1,7,2]

myVar= pd.Series(a)

#print(myVar)

#se não especificado, os indices são especificados por números inteiros normais (vide exemplo de cima)

#também podemos especificar os indices 

myvar2 = pd.Series(a, index = ["x", "y", "z"])
#print(myvar2)

#posso me referir pelas labels
#print(myvar2["y"])

#também posso usar um key tipo em um dicionário pra criar a série

calories = {"day 1": 420, "day 2": 380, "day 3" : 390}
myvar3 = pd.Series(calories)
#print(myvar3)

#a key do dicionário vira a label
myvar4 = pd.Series(calories, index = ["day 1", "day 2"])
#print(myvar4) #note que só apareceu o que a gente escolheu


#serie é uma coluna, dataframe é a tabela inteira

data = {
    "calories":[420,380,390],
    "duration" : [50,40,15]
}

myvar5 = pd.DataFrame(data, index = ["dia 1", "dia 2", "dia 3"]) #precisa igualar index a uma lista n rola deixar solto
print(myvar5)