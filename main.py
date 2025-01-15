import os, requests, argparse, sys
from parse import FindImages
from image import DownloadImages, ChangeFiletype
from bs4 import BeautifulSoup


classes = ["product-image", "product-images", "product"]
images = []

#Get arguments
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URl to the productpage")
parser.add_argument("--classes", help="HTML classes")
parser.add_argument("--format", help="Fileformat")
parser.add_argument("--filename", help="Filename")

args = parser.parse_args()
downloaded_images = []
format = None
#Check arguments
if not args.url:
    print("No URL specified")
    sys.exit()

if args.format:
    format = args.format

#add classes to array
if args.classes:
    classes.append(args.classes)


# URL to the productpage
url = args.url

print("Parsing productpage: ", url)
# Get pagecontent
response = requests.get(url)

if response.status_code == 200:

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find images
    images = FindImages(soup, classes, url)

    #Download images
    downloaded_images = DownloadImages(images, args.filename)

    #Convert images to desired format
    if format:
        ChangeFiletype(downloaded_images, format)

    #print("Images found: ", images)
else:
    print("Error gettig page:", response.status_code)

