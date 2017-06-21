import pandas as pd

country_data_name = '2015-11-01_RAI_country_data.csv'
regional_data_name = '2015-11-01_RAI_regional_data.csv'
mapping_lookup_data_name = 'country_code_mapping_lookup.csv'

country_data = pd.read_csv(country_data_name)
regional_data = pd.read_csv(regional_data_name)
mapping_lookup_data = pd.read_csv(mapping_lookup_data_name, keep_default_na=False)
mapping_lookup_dict = dict(zip(
	mapping_lookup_data['ISO-3166\nnumeric'],
	map(str.lower, (mapping_lookup_data['Continent'] + mapping_lookup_data['ISO-3166\nalpha3']))
))

# mapping_lookup_dict.update({
# 	'GER': 'eudeu',
# 	'JAP': 'asjpn',
# 	'ROM': 'eurou',
# 	'SAM': 'euscg',
# 	'SWI': 'euche',
# 	'KOS': 'euxkx',
# 	'INO': 'asidn',
# 	'MLY': 'asmys',
# 	'SIN': 'assgp',
# 	'BRU': 'asbrn',
# })

country_data['formatted_continent_country_id'] = map(lambda x: mapping_lookup_dict.get(x, 'n/a'), country_data['iso3166'])
country_data.to_csv(country_data_name.split('.')[0] + '_formatted.csv')