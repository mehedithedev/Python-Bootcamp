import requests

url= "https://as2.ftcdn.net/v2/jpg/02/66/72/41/1000_F_266724172_Iy8gdKgMa7XmrhYYxLCxyhx6J7070Pr8.jpg"
response = requests.get(url)

with open("image.jpg", "wb") as file:
    file.write(response.content)
