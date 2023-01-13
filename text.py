import pandas as pd

data ={
    "apples": [4,3,6,1],
    "oranges": [3,7,4,1]
}
    
index_titles =[
"aaron","shaun","james","willson"
]
df = pd.DataFrame(data, index= index_titles)
print (df)
print(df.loc["aaron"]["apples"])
print(type(df))