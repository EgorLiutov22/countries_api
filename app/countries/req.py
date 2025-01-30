import requests

url = 'https://restcountries.com/v3.1/'


class Country:
    def __init__(self, country_dict):
        self.name_en = country_dict['name']['common']
        if 'nativeName' in country_dict['name']:
            self.name_native = [country_dict['name']['nativeName'][n]['official']
                                for n in country_dict['name']['nativeName']]
        self.name_ru = country_dict['translations']['rus']['official']
        if 'ccn3' in country_dict:
            self.code = country_dict['ccn3']
        if 'currencies' in country_dict:
            self.currencies = country_dict['currencies']
        if 'capital' in country_dict:
            self.capital = Capital(country_dict['capital'][0], self.name_en, country_dict['capitalInfo'])
            if len(country_dict['capital']) > 1:
                self.other_capital = country_dict['capital'][1:]
        else:
            self.capital = None
        self.coords = country_dict['latlng']
        if 'languages' in country_dict:
            self.lang = country_dict['languages']
        self.maps = country_dict['maps']
        self.population = country_dict['population']
        self.area = country_dict['area']
        self.continents = country_dict['continents']
        self.flags = country_dict['flags']
        self.capital_info = country_dict['capitalInfo']
        self.region = country_dict['region']


class Capital:
    def __init__(self, name, country, info, other_capital=None):
        self.name = name
        self.country = country
        self.info = info
        if other_capital:
            self.other_capital = other_capital


def countries_all():
    r = requests.get(url + 'all', verify=False)
    # print(r.json())
    countries = [Country(c) for c in r.json()]
    return countries


def country_name(name):
    r = requests.get(url + f'name/{name}', verify=False)
    country = Country(r.json()[0])
    return country


def regions_api():
    countries = countries_all()
    regions = {c.region for c in countries}
    return regions


def get_capitals():
    r = countries_all()
    capitals = [country.capital for country in r if country.capital]
    return capitals


def capital(name):
    capitals = get_capitals()
    for c in capitals:
        if c.name == name:
            return c


if __name__ == '__main__':
    countries_all()
    c = country_name('South Georgia')
    print(c.name_ru)
    print(regions_api())
