import feedparser
import asyncio

mots_cles = ["argent","finance","guerre"]

with open('rss_list.txt', 'r', encoding='utf-8') as f:
    rss_urls = [line.strip() for line in f if line.strip()]

async def scraper():
    d = feedparser.parse("https://flux.saynete.com/encart_rss_informatique_programmation_fr.xml")
    articles = []
    articles.append({
        "titre": d.feed.title,
        "description": d.feed.description
    })
    print(articles)

for article in articles:
    if mots_cles.lower() in article.feed.title.lower() or mots_cles.lower() in article.feed.description.lower():
        print(f"{article.feed.title} ({article.feed.published})")
        print(f"{article.feed.link}")

asyncio.run(scraper())