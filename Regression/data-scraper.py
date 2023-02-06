import requests
from bs4 import BeautifulSoup

def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find the main container for property information
    main_container = soup.find('div', {'class': 'zsg-lg-2-3 zsg-sm-1-1'})

    # Extract the title of the property
    title = main_container.find('h1').text.strip()

    # Extract the price of the property
    price = main_container.find('span', {'class': 'value'}).text.strip()

    # Extract the address of the property
    address = main_container.find('span', {'class': 'address'}).text.strip()

    # Extract the number of beds and baths
    beds_baths = main_container.find('ul', {'class': 'bed-bath-living'}).text.strip()

    # Extract the square footage of the property
    sqft = main_container.find('ul', {'class': 'sqft'}).text.strip()

    # Return the scraped data as a dictionary
    return {
        'title': title,
        'price': price,
        'address': address,
        'beds_baths': beds_baths,
        'sqft': sqft,
    }

# Example usage
property_url = 'https://www.fakerealestatedata.com'
property_data = scrape(property_url)
print(property_data)
