from flask import Flask, request, Response
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

"""
Rewrite URLs in HTML soup to go through the proxy.
"""
def rewrite_urls(soup, base_url):
    #  If the link is an absolute URL, it will be rewritten to go through the proxy
    for tag in soup.find_all(["a", "img", "script", "link"], href=True):
        href = tag.get("href")
        if href.startswith("http"):
            tag["href"] = f"/?url={href}"
        else:
            tag["href"] = f"/?url={base_url}/{href}"

    for tag in soup.find_all(["a", "img", "script", "link"], src=True):
        src = tag.get("src")
        if src.startswith("http"):
            tag["src"] = f"/?url={src}"
        else:
            tag["src"] = f"/?url={base_url}/{src}"


@app.route("/")
def proxy():
    target_url = request.args.get("url")
    if not target_url:
        return "Missing URL, add ?url=https://mywebsite.com", 400

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        resp = requests.get(target_url, headers=headers, verify=True)
    except requests.RequestException as e:
        return f"Error fetching the URL: {str(e)}", 500

    content_type = resp.headers.get("Content-Type", "")

    if "text/html" in content_type:
        soup = BeautifulSoup(resp.content, "html.parser")
        base_url = re.match(r"^(http[s]?://[^/]+)", target_url).group(1)
        rewrite_urls(soup, base_url)
        modified_content = str(soup).encode("utf-8")
    else:
        modified_content = resp.content

    return Response(modified_content, content_type=content_type)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
