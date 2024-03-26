
import re

from urllib.request import Request, urlopen

# Define the main URL
main_url = "https://www.worldometers.info/coronavirus/country/"
import os
# Predefined regions
predefined_regions = ["Europe", "North America", "Asia", "South America", "Africa", "Oceania"]

# Read and preprocess the country list
with open('worldometers_countrylist.txt', 'r') as file:
    data = file.read()

current_region = ""
data = re.sub(r":", "", data)
data = re.sub(r"-+", "START", data)
country_dict = {}
data = data.replace("\n\n", "\nEND\n") + "END"
lines = data.split("\n")

# Initialize the dictionary to hold regions and countries

inside_country_block = False

# Parse the country list
for line in lines:
    temp = line.strip()
    if temp in predefined_regions:
        country_dict[temp] = []
        current_region = temp
    elif temp == "START":
        inside_country_block = True
    elif temp == "END":
        inside_country_block = False
    elif inside_country_block:
        temp = temp.replace(" ", "-")
        country_dict[current_region].append(temp)

# Function to fetch and save HTML content for a given URL
def fetch_and_save_html(country_name, url):
    html_file = country_name + ".html"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as response:
        webpage_content = response.read().decode("utf-8")
    with open(html_file, 'w', encoding="utf-8") as f:
        f.write(webpage_content)
    print(f"Saved {html_file}")

# Fetch and save pages for each country
for region, countries in country_dict.items():
    for country in countries:
        country_url = main_url + country + "/"
        fetch_and_save_html(country, country_url)
