import urllib.request

def data_uri_to_bytes(data_uri: str) -> bytes:
    with urllib.request.urlopen(data_uri) as r:
        return r.read()