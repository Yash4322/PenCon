import base64
import urllib.parse


def encode_data(data, method):
    if method == "base64":
        return base64.b64encode(data.encode()).decode()

    elif method == "url":
        return urllib.parse.quote(data)

    elif method == "hex":
        return data.encode().hex()

    else:
        return "[-] Invalid encoding type"
