import os, requests, argparse, sys, csv
from parse import FindImages, ParseProduct
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
parser.add_argument("--productlist", help="File containt list of images to fetch")


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

#Check if we have a CSV file with products to download
if args.productlist:
    print("Parsing from productlist")
    with open(args.productlist) as f:

        #Get lines containing two rows
        raw_lines = csv.reader(f, delimiter=';')
        lines = [line for line in raw_lines if len(line) >= 2]

        
    totalcount = len(lines)
    count = 0
    for lines in lines:
        count += 1
        print(f'Downloading product {lines[0]}.  {count} / {totalcount}')
        ParseProduct(lines[0], lines[1], classes, format)
        #print("Parsing productnr.: ", lines[0] + ". URL: " + lines[1])

else:
    url = args.url

    print("Parsing productpage: ", url)
    ParseProduct(url, args.filename, classes, format)

