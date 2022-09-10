import json

import requests

# https://products.wolframalpha.com/docs/WolframAlpha-API-Reference.pdf
URL = "https://api.wolframalpha.com/v2/query?input=1%2B1&format=image,plaintext&output=JSON&appid=[redacted]"
print(json.dumps(requests.get(URL).json(), indent=4))
