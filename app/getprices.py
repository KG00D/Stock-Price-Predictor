import requests

response = requests.get("https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey=bXSJUxjypggininnkMAGgNsf2utFs2YU")
print(response)