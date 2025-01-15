# Web Image Scraper

A simple Python script that extracts all prodductimages from a weshop.

## Requirements

- Python 3.x
- BeautifulSoup4
- Requests
- Pillow

## Installation

Install the required packages:

```sh
pip install beautifulsoup4 requests pillow
```

## Usage
With custom class and PNG format.

```sh
python main.py --url "https://example.com/product" --classes "custom-class" --format "png" --filename "productimage"
```

## Options
| Flag         | Description                                                                                                        | Example                                                   |
|--------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| `--url`      | **(Required)** The URL of the product page (or any other page) to scrape.                                          | `python main.py --url "https://example.com/product"`      |
| `--classes`    | (Optional) One or more HTML classes used to find the images.                                                       | `python main.py --url "..." --class "product-image"`      |
| `--format`   | (Optional) Convert the downloaded images to the specified format (e.g., `png`, `jpg`).                             | `python main.py --url "..." --class "..." --format "png"` |
| `--filename` | (Optional) Base name/prefix for the downloaded images. If omitted, the name is derived from the URL's file name.    | `python main.py --url "..." --filename "myproductimages"` |
