import requests
from bs4 import BeautifulSoup

# function that returns raw html text
def get_raw_website(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    return soup


# scrapes gas prices from given url and returns a list containing all information
def europe_prices():
    html_code = get_raw_website(url="https://www.cargopedia.net/europe-fuel-prices")

    all_prices = []

    # searching the website for desired elements (in this case the country and prices of fuel)
    country_table = html_code.find("tbody")
    country_list = country_table.find_all("tr")
    for country in country_list:
        name = country.find("td").text.strip()
        ninetyfive_price = country.find_all("td")[1].text
        diesel_price = country.find_all("td")[2].text
        lpg_price = country.find_all("td")[3].text

        all_prices.append(
            {
                "name": name,
                "95": ninetyfive_price,
                "diesel": diesel_price,
                "lpg": lpg_price,
            }
        )
    return all_prices
