import requests, os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from image import DownloadImages, ChangeFiletype

def ParseProduct(filename, url, classes, format):
    # Get pagecontent
    response = requests.get(url)

    if response.status_code == 200:

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find images
        images = FindImages(soup, classes, url)

        #Download images
        downloaded_images = DownloadImages(images, filename)

        #Convert images to desired format
        if format:
            ChangeFiletype(downloaded_images, format)

        #print("Images found: ", images)
    else:
        print("Error gettig page:", response.status_code)
    
def FindImages(soup, classes, base_url):
    images = set()

    for c in classes:

        # Get all images with a classname matching the classes array
        img_tags = soup.find_all("img", class_=c)

        for img in img_tags:
            src = img.get('src')
            #images.append(src)
            if src:
                absolute_url = urljoin(base_url, src)
                images.add(absolute_url)

        # Find all images with parent class matching the classes array
        parent_tags = soup.find_all(class_=c)
        for parent in parent_tags:
            img_tags = parent.find_all("img")
            for img in img_tags:
                src = img.get('src')
                if src:
                    absolute_url = urljoin(base_url, src)
                    images.add(absolute_url)
    return list(images)