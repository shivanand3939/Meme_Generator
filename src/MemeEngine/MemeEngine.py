from PIL import Image, ImageDraw, ImageFont
import os, time

class MemeEngine:

    def __init__(self, output_dir):
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        self.output_dir = output_dir



    def make_meme(self, in_path, text=None, author=None, width=500) -> str:
        """Create a Postcard With a Text Greeting

        Arguments:
            in_path {str} -- the file location for the input image.
            text {str} -- The body of the Quote
            author {str} -- Author of the Quote
            width {int} -- The pixel width value. Default=None.
        Returns:
            str -- the file path to the output image.
        """

        img = Image.open(in_path)

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text is not None:
            message = text + '-' + author
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((10, 30), message, font=font, fill='white')


        output_file_name = "output_" + str(time.time()) + ".png"

        for filename in os.listdir('static/'):
            if filename.startswith('output_'):  # not to remove other images
                os.remove('static/' + filename)

        img.save('static/' + output_file_name)
        return output_file_name
