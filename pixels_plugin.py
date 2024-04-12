from mitmproxy import http
import re
from urllib.parse import urlparse, unquote


def get_filename_from_url(url):
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    return path.split('/')[-1]

def response(flow: http.HTTPFlow) -> None:
    url = flow.request.pretty_url
    if url.find('play.pixels.xyz')!= -1:
        file_name = get_filename_from_url(url)
        if file_name.endswith(".js"):
            with open(f"src/{file_name}") as file:
                print(f"{url} done")
                flow.response.text = file.read()