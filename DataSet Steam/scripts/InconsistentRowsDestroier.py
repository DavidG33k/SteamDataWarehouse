# Given a set of developer ID, publisher ID or appID, the script destroy all rows of all CSV files that match with that IDs.

import pandas

# Dataset to clean
appcategory_associations_with_weights = pandas.read_csv('appcategory_associations_with_weights.csv', encoding='ISO-8859-1') # To clean with appID
appgenre_associations_with_weights = pandas.read_csv('appgenre_associations_with_weights.csv', encoding='ISO-8859-1') # To clean with appID
appplatform_associations_with_weights = pandas.read_csv('appplatform_associations_with_weights.csv', encoding='ISO-8859-1') # To clean with appID
appdeveloper_associations_with_weights = pandas.read_csv('appdeveloper_associations_with_weights.csv', encoding='ISO-8859-1') # To clean with appID/developer ID
apppublisher_associations_with_weights = pandas.read_csv('apppublisher_associations_with_weights.csv', encoding='ISO-8859-1') # To clean with appID/publisher ID
steam_cleaned = pandas.read_csv('steam_cleaned.csv', encoding='ISO-8859-1') # To clean with appID
steam_developers = pandas.read_csv('steam_developers.csv', encoding='ISO-8859-1') # To clean with developer ID
steam_publishers = pandas.read_csv('steam_publishers.csv', encoding='ISO-8859-1') # To clean with publisher ID

# Dataset with the IDs references
developers_id_to_remove = pandas.read_csv('developers_id_to_remove.csv', encoding='ISO-8859-1')
appid_to_remove_by_developers = pandas.read_csv('appid_to_remove_by_developers.csv', encoding='ISO-8859-1')
publishers_id_to_remove = pandas.read_csv('publishers_id_to_remove.csv', encoding='ISO-8859-1')
appid_to_remove_by_publishers = pandas.read_csv('appid_to_remove_by_publishers.csv', encoding='ISO-8859-1')

# Delete all rows of all CSV files that match with this developers IDs
for i in range(developers_id_to_remove.shape[0]):
    devToRemove = developers_id_to_remove['developer_id'][i]

    steam_developers.drop(steam_developers[(steam_developers['developer_id'] == devToRemove)].index, inplace=True)
    appdeveloper_associations_with_weights.drop(appdeveloper_associations_with_weights[(appdeveloper_associations_with_weights['developer_id'] == devToRemove)].index, inplace=True)

# Delete all rows of all CSV files that match with this publishers IDs
for i in range(publishers_id_to_remove.shape[0]):
    pubToRemove = publishers_id_to_remove['publisher_id'][i]

    steam_publishers.drop(steam_publishers[(steam_publishers['publisher_id'] == pubToRemove)].index, inplace=True)
    apppublisher_associations_with_weights.drop(apppublisher_associations_with_weights[(apppublisher_associations_with_weights['publisher_id'] == pubToRemove)].index, inplace=True)

# Delete all rows of all CSV files that match with this app IDs (obtained from the developer bridge table)
for i in range(appid_to_remove_by_developers.shape[0]):
    appToRemove = appid_to_remove_by_developers['appid'][i]

    appcategory_associations_with_weights.drop(appcategory_associations_with_weights[(appcategory_associations_with_weights['appid'] == appToRemove)].index, inplace=True)
    appplatform_associations_with_weights.drop(appplatform_associations_with_weights[(appplatform_associations_with_weights['appid'] == appToRemove)].index, inplace=True)
    appplatform_associations_with_weights.drop(appplatform_associations_with_weights[(appplatform_associations_with_weights['appid'] == appToRemove)].index, inplace=True)
    appdeveloper_associations_with_weights.drop(appdeveloper_associations_with_weights[(appdeveloper_associations_with_weights['appid'] == appToRemove)].index, inplace=True)
    apppublisher_associations_with_weights.drop(apppublisher_associations_with_weights[(apppublisher_associations_with_weights['appid'] == appToRemove)].index, inplace=True)
    steam_cleaned.drop(steam_cleaned[(steam_cleaned['appid'] == appToRemove)].index, inplace=True)

# Delete all rows of all CSV files that match with this app IDs (obtained from the publisher bridge table)
for i in range(appid_to_remove_by_publishers.shape[0]):
    appToRemove = appid_to_remove_by_publishers['appid'][i]

    appcategory_associations_with_weights.drop(appcategory_associations_with_weights[(appcategory_associations_with_weights['appid'] == appToRemove)].index, inplace=True)
    appplatform_associations_with_weights.drop(appplatform_associations_with_weights[(appplatform_associations_with_weights['appid'] == appToRemove)].index, inplace=True)
    appplatform_associations_with_weights.drop(appplatform_associations_with_weights[(appplatform_associations_with_weights['appid'] == appToRemove)].index, inplace=True)
    appdeveloper_associations_with_weights.drop(appdeveloper_associations_with_weights[(appdeveloper_associations_with_weights['appid'] == appToRemove)].index, inplace=True)
    apppublisher_associations_with_weights.drop(apppublisher_associations_with_weights[(apppublisher_associations_with_weights['appid'] == appToRemove)].index, inplace=True)
    steam_cleaned.drop(steam_cleaned[(steam_cleaned['appid'] == appToRemove)].index, inplace=True)

# Export cleaned datasets
appcategory_associations_with_weights.to_csv('final tables/appcategory_bridgetable.csv', index=False)
appgenre_associations_with_weights.to_csv('final tables/appgenre_bridgetable.csv', index=False)
appplatform_associations_with_weights.to_csv('final tables/appplatform_bridgetable.csv', index=False)
appdeveloper_associations_with_weights.to_csv('final tables/appdeveloper_bridgetable.csv', index=False)
apppublisher_associations_with_weights.to_csv('final tables/apppublisher_bridgetable.csv', index=False)
steam_cleaned.to_csv('final tables/steam_maintable.csv', index=False)
steam_developers.to_csv('final tables/steam_developers.csv', index=False)
steam_publishers.to_csv('final tables/steam_publishers.csv', index=False)