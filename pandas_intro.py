import pandas as pd

data = {
    'rocket': [
        'Falcon 1',
        'Falcon 9',
        'Falcon Heavy',
    ],
    'launches': [5, 100, 3],
}

df = pd.DataFrame(data)

# print(df)

#print(df['rocket'])

df2 = df[df['launches'] > 5]

# df['sucess_rate'] = [0.4, 0.98, 1.0]

print(df2)