﻿# BimaWallah API's
 # Flask Image Processing App

This Flask app provides endpoints to perform various image processing tasks including adding text to images, converting images to PDFs, and downloading images.

## Endpoints

### `/get_image`

- **Description:** This endpoint accepts an image and text input, adds the provided text to the image, and returns the modified image as a response.
- **Method:** POST
- **Request Parameters:**
  - `image`: The image file to process.
  - `text`: The text to add to the image.
- **Response:**
  - The modified image file with the text added.

### `/convert_pdf_to_image`

- **Description:** This endpoint accepts a PDF file, converts it into an image, and returns the image as a response.
- **Method:** POST
- **Request Parameters:**
  - `pdf`: The PDF file to convert.
- **Response:**
  - The converted image file.

### `/download_image`

- **Description:** This endpoint allows downloading images stored on the server.
- **Method:** GET
- **Query Parameters:**
  - `image_name`: The name of the image file to download.
- **Response:**
  - The image file to download.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt

