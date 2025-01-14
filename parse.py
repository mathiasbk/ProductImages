from urllib.parse import urljoin

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