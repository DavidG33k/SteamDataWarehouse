from itertools import repeat
import pandas

df = pandas.read_csv('appcategory_associations.csv')

print('\nPreview:')
print(df)

print('\nNumber of rows: ' + str(df.shape[0]))

weights = []

count = 0
actualID = df['appid'][0]


for i in range(df.shape[0]):

    if df['appid'][i] == actualID:
        count += 1

    else:
        weights.extend((1/count) for i in range(count))

        count = 1
        actualID = df['appid'][i]


    # To not skip the last weight addition of the last game. 
    if i == df.shape[0] - 1: 
        weights.extend((1/count) for i in range(count))


dfWithWeights = df.assign(weights=weights)

print('\Dataframe preview with weights:')
print(dfWithWeights)

dfWithWeights.to_csv('appcategory_associations_with_weights.csv', index=False)

# Uncomment to save the new dataframes on a csv files.
