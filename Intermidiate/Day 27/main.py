import requests
from send_email import send_email

topic = "openai"
api_key = "872a2184158643219aee2679e6484bdd"
url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}"
       f"&sortBy=publishedAt"
       f"&language=en"
       f"&apiKey={api_key}")

# Make request
r = requests.get(url)

# Get a dictionary with data
content = r.json()

# Start the body with the subject line
body = "Subject: Today's Top News\n\n"

# Check if 'articles' is in the content dictionary
if 'articles' in content:
    # Access the article titles and description
    for article in content["articles"][:20]:
        title = article.get("title")
        description = article.get('description')
        address = article.get("url")
        if title and description and address:
            body = body + title + "\n" + description +"\n"+ address + 2*"\n"

    # Encode the body variable
    body = body.encode("utf-8")

    # Send the email
    send_email(body)
else:
    print("No articles found in the response.")