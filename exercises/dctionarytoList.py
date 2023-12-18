travel_log = [
{
    'country': 'France',
    'visits': 2,
    'cities':['Paris', 'Lille', 'Dijon']
},
{
    'country': 'Germany',
    'visits': 5,
    'cities':['Berlin', 'Hamburg', 'Stuggart']
},
]

def add_new_county(countryValue, visitsNumber, citiesValue):
    this_entry = {'country': countryValue, 'visits': visitsNumber, 'cities': citiesValue}
    travel_log.append(this_entry)

   


add_new_county('Russia', 2, ['Moscow', 'Saint Petersburg', 'Siberia'])



add_new_county('Philippines', 5, ['Cebu', 'Manila', 'Pasig'])

print(travel_log)