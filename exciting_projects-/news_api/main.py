import requests

query = "artificial intelligence"
api = "e2c4ff8947bd421d81e83f4ba4eccd9c"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-03-29&sortBy=publishedAt&apiKey={api}"
print(url)

r = requests.get(url)
data = r.json()  # <-- fix here

articles = data["articles"]  # <-- fix variable name and spelling

for article in articles:     # <-- fix loop variable name
    print(article["title"])
    print(article["url"])
    print("\n*********************************************\n")
