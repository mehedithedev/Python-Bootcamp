import requests

api_key = "872a2184158643219aee2679e6484bdd"
url = f"https://newsapi.org/v2/everything?q=apple&sortBy=publishedAt&apiKey={api_key}"


# Make request
r = requests.get(url)


# Get a dictionary with data
content = r.json()


# Access the article titles and description
for article in content["articles"]:
    print(article["title"])