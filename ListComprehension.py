countries = ['Bangladesh', 'India', 'Pakistan']

countryListCom=[]
for country in countries:
    if len(country)>5:
        countryListCom.append(country)
print(countryListCom)

countryListCom=[country for country in countries if len(country)>5]
print(countryListCom)

        