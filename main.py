
import os, requests, argparse, sys
from parse import FindImages
from image import DownloadImages
from bs4 import BeautifulSoup

classes = ["product-image", "product"]
images = []

#Get arguments
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URl to the productpage")
parser.add_argument("--class", help="HTML classes")

args = parser.parse_args()


# URL to the productpage
url = args.url

print("Parsing productpage: ", url)
# Get pagecontent
response = requests.get(url)

if response.status_code == 200:

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find images
    images = FindImages(soup, classes)

    #Download images
    DownloadImages(images)

    #print("Images found: ", images)
else:
    print("Error gettig page:", response.status_code)

