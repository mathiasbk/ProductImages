import os, requests
from urllib.parse import urlsplit
from PIL import Image
def DownloadImages(images):

    downloaded_images = []

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

            # Generate filename
            filename = os.path.basename(urlsplit(img).path)
            if not filename:
                filename = "downloaded_image"
            if not filename.endswith(extension):
                filename += "."+extension
            print("Filename: ", filename)

            # Full path to the file
            file_path = os.path.join("images", filename)

            #save the image
            with open(f"images/{filename}", 'wb') as file:
                file.write(response.content)

            downloaded_images.append(file_path)
        except requests.exceptions.RequestException as e:
            print("Error downloading image: ", e)
            continue

    return downloaded_images

#Change the fileformat
def ChangeFiletype(images, format):
    for img in images:
        
        #If format is the same, ignore it
        if format == os.path.splitext(os.path.basename(img))[1][1:]:
            continue

        #Save the old filename
        old_file = img

        f, e = os.path.splitext(os.path.basename(img))
        output_path = os.path.join("images", f + "." + format)
        
        #Check filetype
        pil_format = format.upper()
        if pil_format == "JPG":
            pil_format = "JPEG"

        #Open the image
        image = Image.open(img)
        
        #Convert to RGB if we want to save as jpeg
        if pil_format == "JPEG" and image.mode == "RGBA":
            image = image.convert("RGB")

        #Save the new file with correct format
        image.save(output_path, format = pil_format)

        #Delete the old image with wrong format
        os.remove(old_file)