import pandas


def replaceMissingValues():
    if df['name'].isna().sum() != 0:
        df['name'].fillna('Unknown name')
    if df['achievements'].isna().sum() != 0:
        df['achievements'].fillna(0)
    if df['average_playtime'].isna().sum() != 0:
        df['average_playtime'].fillna(-1)
    if df['median_playtime'].isna().sum() != 0:
        df['median_playtime'].fillna(-1)
    if df['negative_ratings'].isna().sum() != 0:
        df['negative_ratings'].fillna(0)
    if df['positive_ratings'].isna().sum() != 0:
        df['positive_ratings'].fillna(0)
    if df['publisher'].isna().sum() != 0:
        df['publisher'].fillna('Unknown publisher')
    if df['developer'].isna().sum() != 0:
        df['developer'].fillna('Unknown developer')
    if df['required_age'].isna().sum() != 0:
        df['required_age'].fillna(0)
    if df['release_date'].isna().sum() != 0:
        df['release_date'].fillna('0-0-0')


df = pandas.read_csv('steam_original.csv', encoding='utf-8')

print('\nAttributes description:')
print(df.info())

print('\nPercentage of missing values:')
print(df.isnull().sum() * 100 / len(df))

print('\nNumber of rows with at least one missing data:')
count_rows_with_missing_values = df.isnull().any(axis = 1).sum()
print(count_rows_with_missing_values)

if count_rows_with_missing_values != 0:
    null_data = df.loc[df.isnull().any(axis=1)]
    print(null_data)

    replaceMissingValues()

    df.to_csv('steam_original_cleaned.csv', index=False)

print('\nPercentage of duplicates rows (False if unique, else True):')
percentage_of_duplicates = df.duplicated(keep=False).value_counts(normalize=True) * 100
print(percentage_of_duplicates)

if True in percentage_of_duplicates:
    df.drop_duplicates()

    df.to_csv('steam_original_cleaned.csv', index=False)



