import requests
import re
from bs4 import BeautifulSoup

class MediafireLinkExtractor:
    def __init__(self, link):
        self.link = link

    def check_link_response_type(self):
        response = requests.head(self.link)
        content_type = response.headers.get('content-type', '')

        if 'text/html' not in content_type:
            raise Exception(f'Expected "text/html" but received "{content_type}"')

    def get_link(self):
        valid_link_pattern = r'^(http|https)://(?:www\.)?(mediafire)\.com/[0-9a-z]+(/.*)'

        if not re.match(valid_link_pattern, self.link):
            raise Exception('Unknown link')

        try:
            self.check_link_response_type()
            response = requests.get(self.link)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            download_button = soup.find(id='downloadButton')

            if not download_button:
                raise Exception('Could not find download button')

            return download_button['href']
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                raise Exception('The key you provided for file access was invalid.')
            else:
                raise Exception(f'Mediafire returned status {e.response.status_code}')
        except Exception as e:
            raise e

