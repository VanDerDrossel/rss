import requests
import xml.etree.ElementTree as ET


URL = 'http://static.feed.rbc.ru/rbc/logical/footer/news.rss'


def main():
    txt = get_rss(URL)
    parsing_xml(txt, 'category', 'rbc_news:anons')


def get_rss(url: str) -> str:
    """Return text response."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text


def parsing_xml(data: str, *tags: str) -> None:
    """
    Parsing XML from arg data
    and extract content for need tags.
    And print content.
    """
    root = ET.fromstring(data)
    items = root.findall('.//item')
    for item in items:
        for tag in tags:
            if ':' in tag:
                tag = tag.split(':')[1]
                tag_ns = f'{{http://www.rbc.ru}}{tag}'
                tag_text = item.find(tag_ns).text
            else:
                tag_text = item.find(tag).text
            print(tag_text, end=' -> ')
        print()


if __name__ == '__main__':
    main()
