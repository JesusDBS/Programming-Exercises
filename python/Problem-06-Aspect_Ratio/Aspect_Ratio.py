#Aspect Ratio:
# Create a program that calculates the aspect ratio of an image from a url.
#  - Example url: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
#  - By ratio we refer for example to the "16:9" of a 1920*1080px image.

import requests

from PIL import Image
from io import BytesIO
from fractions import Fraction

#Exceptions
class StatusCodeError(Exception):
    """Checks if the status_code is 200.
    """
    def __init__(self, code, message="Status code"):
        self.code = code
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return f"Request error! --> {self.message}: {self.code}"

class ResponseTypeError(Exception):
    """Checks if response.content is a binary type.
    """
    def __init__(self, response, message="The type of response is not binary!"):
        self.response = response
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return f"{type(self.response.content)} --> {self.message}"


#Calculates aspect ratio as width over height
def aspect_ratio(w,h):
    """Calculates the aspect ratio of an image.

    Parameters
    ----------
    w: int
        Width of the image.
    h: int
        Height of the image.
    """
    #validations
    assert isinstance(w, int), 'The width of the image must be an integer'
    assert isinstance(h, int), 'The height of the image must be an integer'

    aspect_ratio = Fraction(round(w/h,2)).limit_denominator()

    return aspect_ratio

def main():
    #Setting the Image URL
    image_uri = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png'

    #Getting the Image
    try:
        response = requests.get(image_uri)

        if response.status_code == requests.codes.ok:
            if isinstance(response.content, bytes):
                image = Image.open(BytesIO(response.content))

                if image.width and image.height:
                    ratio = aspect_ratio(image.width,image.height)

                    print(f"The aspect ratio of the image is {ratio.numerator}:{ratio.denominator}.")

            else:
                raise ResponseTypeError(response)
        else:
            raise StatusCodeError(response.status_code)

    except Exception as e:
        print(str(e))
        raise e

if __name__ == "__main__":
    main()



