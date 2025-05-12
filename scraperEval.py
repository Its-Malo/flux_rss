import feedparser
import asyncio
from time import process_time, sleep

async def scraper(url):
    d = feedparser.parse(url)
    articles = []
    try:
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries:
            articles.append({
                "title": entry.get("title", "N/A"),
                "link": entry.get("link", "N/A"),
                "summary": entry.get("summary", ""),
                "published": entry.get("published", "N/A")
            })
        return articles
    except Exception as e:
        print(f"[!] Erreur sur {url} : {e}")
        return []

async def main():
    start = process_time()
    with open('rss_list.txt', 'r', encoding='utf-8') as f:
        rss_urls = [line.strip() for line in f if line.strip()]
    
    with open('mots_cles.txt', 'r', encoding='utf-8') as f:
        mots_cles = [line.strip() for line in f if line.strip()]

    for url in rss_urls:
        articles = await scraper(url)
        for article in articles:
            resultat = open("resultat.txt", "a")
            for mot in mots_cles:
                if mot in article["title"].lower() or mot in article["summary"].lower():
                    print(f"{article['title']} ({article['summary']})")
                    print(f"{article['link']}")
                    resultat.write(f"Titre : {article["title"]}")
                    resultat.write('\n')
                    resultat.write(f"Date : {article["published"]}")
                    resultat.write('\n')
                    resultat.write(f"Lien : {article["link"]}")
                    resultat.write('\n')
                    resultat.write(f"Mot cles : {mot}")
                    resultat.write('\n')
                    resultat.write('\n')
            resultat.close()
    end = process_time()
    print(end - start)

asyncio.run(main())