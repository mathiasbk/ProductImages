import os, requests
from urllib.parse import urlsplit
def DownloadImages(images):

    # Create a directory for the images
    if not os.path.exists("images"):
        os.makedirs("images")

    for img in images:

        print("Downloading image: ", img)

        try:
            # Get the image
            response = requests.get(img)
            response.raise_for_status()

            # Get the filename from the URL
            filename = os.path.basename(img)  # Ekstraher kun filnavnet fra URL

            # Get filetype from the response headers
            extension = response.headers.get("Content-Type", "").split("/")[-1]

            # Generer filnavn
            filename = os.path.basename(urlsplit(img).path)
            if not filename:
                filename = "downloaded_image"
            if not filename.endswith(extension):
                filename += "."+extension
            print("Filename: ", filename)

            # Full sti for filen
            file_path = os.path.join("images", filename)

            #save the image
            with open(f"images/{filename}", 'wb') as file:
                file.write(response.content)
        except requests.exceptions.RequestException as e:
            print("Error downloading image: ", e)
            continue
