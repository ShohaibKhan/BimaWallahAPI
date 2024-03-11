from flask import Flask, Response, send_file, request, jsonify
from io import BytesIO
import requests
from flask_cors import CORS
import ast


from PIL import Image, ImageDraw,ImageFont
from io import BytesIO
from datetime import datetime
import pytz 
from pdf2image import convert_from_bytes
import fitz

app = Flask(__name__)
CORS(app)

IST = pytz.timezone("Asia/Kolkata")

#convert to bytes
import json
@app.route('/get_image', methods=['POST'])
def get_image():
    # Send the image as a response
    json_data = request.data.decode("utf-8")
    print(json_data)
    data_dict = json.loads(json_data)
    img_data = data_dict.get("body")
    if (type(img_data) == str):
        img_data = ast.literal_eval(img_data)

    byte_data_bytes = bytes(img_data)

    image_result = Image.open(BytesIO(bytes(byte_data_bytes)))

    draw = ImageDraw.Draw(image_result)
    # Specify the text and font
    text = "BimaWallah"
    current_time = datetime.now(IST)
    formatted_time = current_time.strftime("%b %d %Y %H:%M")

    font = ImageFont.load_default()

    # Specify the position to draw the text (top-left corner)
    text_position1 = (10, 10)
    text_position2 = (10, image_result.size[1] - 10 - 35)

    # Specify the text color
    text_color = (0, 0, 255)  
    # White color in RGB
    # Draw the text on the image
    draw.text(text_position1, text, font=font_size_60, fill=text_color)
    draw.text(text_position2, formatted_time, font=font_size_40, fill=text_color)

    #image_result.show()
    output_buffer = BytesIO()
    image_result.save(output_buffer, format="JPEG")
    output_buffer.seek(0)

    return send_file(output_buffer, mimetype='image/jpeg')

@app.route('/download_image', methods=['POST'])
def download_image():
    # Replace 'image_url' with the actual URL of the image you want to download
    json_data = request.data.decode("utf-8")
    print(json_data)
    data_dict = json.loads(json_data)
    image_url = data_dict.get("body")

    #image_url = 'https://firebasestorage.googleapis.com/v0/b/bimawallah-deb52.appspot.com/o/users%2FzkQC4OqK0aX1jYTmPRXu1Rv1ws63%2Fsample?alt=media&token=ffcaafa0-e53c-4b9a-adff-265b2a863011'
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        # Open the image using PIL
        image = BytesIO(response.content)
        print("done")
        return send_file(image, mimetype='image/jpeg', as_attachment=True, download_name='downloaded_image.jpg')

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_pdf2image', methods=['POST'])
def convert_pdf_to_image():
    # Convert PDF to images
     json_data = request.data.decode("utf-8")
     data_dict = json.loads(json_data)
     pdf_url = data_dict.get("body")
     response = requests.get(pdf_url)
     pdf_content=response.content
     pdf_document = fitz.open("pdf", BytesIO(pdf_content))
     page = pdf_document[0]
     image = page.get_pixmap()
     pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
    # Convert the image to bytes using BytesIO
     image_bytes_io = BytesIO()
     pil_image.save(image_bytes_io, format="JPEG")
     pdf_document.close()
    #  return image_bytes_io.getvalue()
     return Response(image_bytes_io.getvalue(), mimetype='image/jpeg')


@app.route('/get_image2', methods=['POST'])
def get_image2():
    # Send the image as a response
    json_data = request.data.decode("utf-8")
    print(json_data,"inside get_image2")
    data_dict = json.loads(json_data)
    image_url = data_dict.get("body")

    try:
        response = requests.get(image_url)
        response.raise_for_status()

        # Open the image using PIL
        image = BytesIO(bytes(response.content))

        image_result = Image.open(image)

        draw = ImageDraw.Draw(image_result)
        # Specify the text and font
        text = "BimaWallah"
        current_time = datetime.now(IST)
        formatted_time = current_time.strftime("%b %d %Y %H:%M")

        font = ImageFont.load_default()

        # Specify the position to draw the text (top-left corner)
        text_position1 = (10, 10)
        text_position2 = (10, image_result.size[1] - 10 - 35)

        # Specify the text color
        text_color = (0, 0, 255)  
        # White color in RGB
        # Draw the text on the image
        draw.text(text_position1, text, font=font, fill=text_color)
        draw.text(text_position2, formatted_time, font=font, fill=text_color)

        #image_result.show()
        output_buffer = BytesIO()
        image_result.save(output_buffer, format="JPEG")
        output_buffer.seek(0)
        return send_file(output_buffer, mimetype='image/jpeg')
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

