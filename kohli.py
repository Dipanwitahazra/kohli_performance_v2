import pandas as pd
df=pd.read_csv("Virat_Kohli.csv")
print(df)
#
# print(df.head(10))
# print(df.tail(10))

# df.info()
# print(df.shape)

# print(df.describe())
#
# print(df["Opposition"].describe())
#
# # run_frequency=df["Runs"].value_counts()
# run_frequency=df["Opposition"].value_counts()
# print(run_frequency)

# new_df=df[["Runs","SR","Opposition"]]
# print(new_df)
#
#
# vs_aus=df[df["Opposition"]=="v Australia"]
# print(vs_aus)

#find all the match virat koheli=cenchury
century=df[df["Runs"]>=100]
print(century)
#virat stike rate>100
stike=df[df["SR"]>100]
print(stike)
#vs srilanka and score a cenchury
