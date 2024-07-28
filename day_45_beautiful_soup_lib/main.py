from bs4 import BeautifulSoup
import requests
# with open("website.html", "r") as html_page:
#     page_content = html_page.read()

response = requests.get("https://news.ycombinator.com/news")
page_content = response.text

soup = BeautifulSoup(page_content, "html.parser")
# print(soup.prettify())

articles = soup.find_all("span", class_="titleline")
for article in articles:
    article_tag = article.find("a")
    title_text = article_tag.get_text()
    title_link = article_tag.attrs["href"]
    print(title_text)
    print(title_link)
    article_upvote = soup.find("span", class_="score").text
    print(article_upvote)


yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

# Find all articles, identified by <a> tags with the class "storylink"
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

# Iterate over each article tag found
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# Find all <span> tags with the class "score" and extract the upvote count
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])