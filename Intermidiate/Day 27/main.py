import requests
from send_email import send_email

api_key = "872a2184158643219aee2679e6484bdd"
url = f"https://newsapi.org/v2/everything?q=apple&sortBy=publishedAt&apiKey={api_key}"


# Make request
r = requests.get(url)


# Get a dictionary with data
content = r.json()

body = ""

# Access the article titles and description
for article in content["articles"]:
    title = article["title"]
    description = article['description']
    if title is not None:
        body = body + title + "\n" + description + 2*"\n"

body = body.encode("utf-8")

send_email(message=body)





