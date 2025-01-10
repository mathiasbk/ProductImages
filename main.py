
import requests, argparse, sys
from bs4 import BeautifulSoup

#Get arguments
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URl to the productpage")

args = parser.parse_args()

# URL to the productpage
url = args.url

print("Parsing productpage: ", url)
# Get pagecontent
response = requests.get(url)

if response.status_code == 200:
    
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get all images
    links = soup.find_all('img')
    print("\nImages:")
    for link in links:
        print(link.get('src'))
else:
    print("Error gettig page:", response.status_code)
