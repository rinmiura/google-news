from requests import get


def get_article_url(path):
    return f'https://news.google.com/article{path}'


def get_all_urls():
    content = get('https://news.google.com/home').text

    pattern = 'href="./article'
    urls = []

    start_index = content.find(pattern)

    while start_index > 0:
        start_index += len(pattern)
        content = content[start_index:]
        end_index = content.find('"')
        urls.append(get_article_url(content[:end_index]))
        start_index = content.find(pattern)

    return urls
