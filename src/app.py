import random
import os
import requests
from flask import Flask, render_template, abort, request, make_response
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine
from PIL import Image, ImageDraw, ImageFont
from io import StringIO


# @TODO Import your Ingestor and MemeEngine classes

app = Flask(__name__, static_url_path='/static')

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for each in quote_files:
        if Ingestor.parse(each):
            quotes.extend(Ingestor.parse(each))

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    img = random.choice(imgs)
    quote = random.choice(quotes)
    print(img, quote.body, quote.author)
    path = meme.make_meme(img, quote.body, quote.author)
    print('mahi', path)
    return render_template('meme.html', path=path)



@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    data = request.form

    output_file_path = '/tmp/temp_file.jpg'

    img_url = data['image_url']
    img = Image.open(requests.get(img_url, stream=True).raw)
    img.save(output_file_path)

    body = data['body']
    author = data['author']

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    path = meme.make_meme(output_file_path, body, author)
    os.remove(output_file_path)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True)
