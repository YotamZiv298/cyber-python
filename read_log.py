import os
import re
import urllib.request
import webbrowser
from urllib.error import HTTPError

# Log file no.1 path
LOG1_PATH = 'log_suspect1.cyberbit.log'
# Images directory no.1 path
IMAGES1_DIR = r'images1'
# HTML page from images directory no.1
IMAGE_1_PAGE = 'suspect1.html'

# Website no.1 from which the images are
WEBSITE1 = 'https://cyber-blich-bitballoon.herokuapp.com'

# Regex for extracting the images
FILE_RE = r'/cyberbit/.*\.jpg'


def run_html(html):
    """
    Opening HTML page in browser.

    :param html: HTML page code.
    """
    with open(os.path.join(os.getcwd(), IMAGE_1_PAGE), 'w') as file:
        file.write(html)
    print("Opening browser...")
    webbrowser.open_new_tab(IMAGE_1_PAGE)


def get_images(urls, dir_path):
    """
    Downloading images from server and creating a HTML page.

    :param urls: URLs of the images.
    :param dir_path: Path for the images directory.
    """
    dir_path = os.path.join(os.getcwd(), dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    image_page = '''
    <html>
        <body>
    '''

    for url in urls[1:]:
        if not os.path.isfile(os.path.join(dir_path, url.split('/')[2])):
            try:
                print(f"downloading {url.split('/')[2]} ...")
                urllib.request.urlretrieve(urls[0] + url, '{0}/{1}'.format(dir_path, url.split('/')[2]))
                print("download complete.")
            except HTTPError:
                print("could not connect to server...")
                continue

        image_page += '<img src="{0}"\n>'.format(os.path.join(dir_path, url.split('/')[2]))

    print('images successfully downloaded.')

    image_page += '''
        </body>
    </html>
    '''
    run_html(image_page)


def extract_urls(log_file):
    """
    Extracting the images URLs from the log file.

    :param log_file: Log file.
    :return: URLs
    """
    with open(log_file, 'r') as file:
        data = file.read()
        urls = [WEBSITE1] + sorted(set(re.findall(FILE_RE, data)))

    return urls


def main():
    """
    The main program.
    """
    urls = extract_urls(LOG1_PATH)
    get_images(urls, IMAGES1_DIR)


if __name__ == '__main__':
    main()
