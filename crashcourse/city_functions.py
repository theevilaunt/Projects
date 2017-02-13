def city_country(city, country, population=''):
  if population == '':
    return city.title() + ", " + country.title()
  else:
    return city.title() + ", " + country.title() + ", population=" + str(population)
