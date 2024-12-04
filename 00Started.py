import pandas as pd

mydataset = { #cria o dataset
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings': [3,7,2]
}

myvar = pd.DataFrame(mydataset) #cria o dataframe(uma planilha 2d) do pandas
print(mydataset)