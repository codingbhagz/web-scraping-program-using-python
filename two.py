import requests
from bs4 import BeautifulSoup as bs


req = requests.get("https://www.futurecodersweb.com/")

soup = bs(req.content, 'html.parser')

logo_image = soup.find('img' , {'alt' : 'Future Coders | HTML CSS JavaScript Blog - Free Source Codes'})['src']
print(logo_image)
