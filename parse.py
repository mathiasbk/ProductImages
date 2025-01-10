def FindImages(soup, classes):
    images = []

    for c in classes:

        # Get all images with a classname matching the classes array
        img_tags = soup.find_all("img", class_=c)

        for img in img_tags:
            src = img['src']
            images.append(src)

        # Find all images with parent class matching the classes array
        parent_tags = soup.find_all(class_=c)
        for parent in parent_tags:
            img_tags = parent.find_all("img")
            for img in img_tags:
                src = img['src']
                images.append(src)
                print("Found from parent image: ", src)
    return images