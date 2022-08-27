from pprint import pprint

from bs4 import BeautifulSoup


def get_data(url):
    values = []
    # headers = {
    #     "accept": "*/*",
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    # }
    # req = requests.get(url, headers)
    # with open("Y_news.html", "w", encoding="utf-8") as file:
    #     file.write(req.text)

    with open("Y_news.html", encoding="utf-8") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")

    try:
        news = soup.find_all("div", class_="news-list__item")
    except Exception:
        news = "Objects not found"

    for i in news[:10]:
        try:
            title = i.find("div", class_="news-list__item-header").text.strip()
            datetime = i.find("time", class_="news-list__item-date").get("datetime")
        except Exception:
            title = "Objects not found"
            datetime = "Date not found"
        finally:
            # print(f"{title_news}\n{date_news}")
            values.append(title.replace("\xa0", " "))
            values.append(datetime)

    return values


send_url = "https://market.yandex.ru/partners/news"

pprint(get_data(send_url))
