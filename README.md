# Windows 98 IE5/6 HTTP Proxy

A Flask-based proxy server designed to enable of modern HTTPS websites via Internet Explorer 5/6 on Windows 98 and other older operating system and browser combos. 
This proxy handles SSL/TLS handshakes and serves content over HTTP, bypassing the encryption limitations of older browsers.

## Features

- **HTTPS Forwarding:** Allows IE5/6 to access content served over HTTPS by handling the encryption/decryption process.
- **Content Rewriting:** Modifies HTML content to ensure all resources (images, scripts, stylesheets) are loaded through the proxy (as much as possible, it's Internet Explorer 5, come on).
- **User-Agent Forwarding:** Optionally forwards a modern User-Agent string to ensure compatibility (to a futile degree).

## Requirements

- Python 3.6+
- Flask
- BeautifulSoup4
- Requests
- A smile on your face

## Installation

1. Clone the repository:
`git clone https:/github.com/snacsnoc/windows98-ie-proxy.git`
2. Navigate to the project directory:
`cd windows98-ie-proxy`
3. Install dependencies:
`pip install -r requirements.txt`



## Usage

Run the Flask application:

`python app.py`
or
`flask run --host=0.0.0.0 -p 80`


Access the proxy by visiting `http://<server-ip>/?url=<target-url>` from Internet Explorer 5/6 on your Windows 98 machine. 
Replace `<server-ip>` with the IP address of the machine running the Flask application and `<target-url>` with the URL of the website you'd like to visit.

## Configuration

The application runs on port 80 by default. This can be configured in `app.py` by changing the `port` parameter in the `app.run()` method or changing the Flask runtime args.

## Security Considerations

This proxy is intended for demonstration use, such as running virtual machines. Please don't run this on a public server.
## Contributing

Contributions are welcome. All IE 5/6 web developers are welcome. Please open an issue or submit a pull request with your improvements.

## License

[GPL v3](LICENSE)
