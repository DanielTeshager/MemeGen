"""
MememEngine class takes care of meme generation.

@params:
output_dit = Takes output directory that tells
the make_meme method where to save images.
"""
from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap
from datetime import datetime as dt


class MemeEngine:
    """Memes are created here."""

    def __init__(self, output_dir):
        """Initialize ImageCaptioner."""
        self.output_dir = output_dir

    def make_meme(self, img_path: str,
                  text: str, author: str, width=500) -> str:
        """Make a meme based on text, author and image provided."""
        try:
            img = Image.open(img_path)
        except IOError as e:
            print(f'Error opening image {img_path} ')
            random_image = random.choice(os.listdir('_data/photos/dog'))
        # resize image
        basewidth = width
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        # Add caption
        meme_text = f'{text}'
        author = f'--{author}'
        meme_font = ImageFont.truetype(
            '_data/Fonts/BebasNeue-Regular.ttf', size=28)
        image_editable = ImageDraw.Draw(img)
        max_allowed = 470
        min_xy, max_xy = 17, 200
        x_start = y_start = random.randint(min_xy, max_xy)
        text_width, text_height = meme_font.getsize(meme_text)
        width = text_width+x_start
        line_height = text_height
        # randomly pick text color
        color = "#"+"%06x" % random.randint(0, 0xFFFFFF)
        # font ration links between chars, and font size
        font_width_ratio = sum(meme_font.getsize(
            i)[0] for i in meme_text) // len(meme_text)

        if width < max_xy:
            image_editable.text((x_start, y_start),
                                meme_text, (0, 230, 211), meme_font)
            image_editable.text((x_start, y_start*2),
                                author, (0, 230, 211), meme_font)
        else:
            lines = textwrap.wrap(meme_text, width=(
                (max_allowed-x_start)//font_width_ratio))
            for line in lines:
                image_editable.text((x_start, text_height),
                                    line, font=meme_font, fill=color)
                text_height += line_height
            image_editable.text((x_start, text_height),
                                author, (0, 230, 211), meme_font)
        # generate random file name
        try:
            os.makedirs(self.output_dir, exist_ok=True)
        except OSError as exc:
            raise(f'Unable to create DIR  {self.output_dir}')
        output_file = f"meme_{str(dt.now().timestamp()).split('.')[0]}"
        export_path = os.path.join(self.output_dir, output_file+'.jpg')
        try:
            img.save(export_path)
            return(export_path)
        except Exception:
            raise('File IO error, unable to save file')
