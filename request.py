# import requests
#
# # Search GitHub's repositories for requests
# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
# )
#
# # Inspect some attributes of the `requests` repository
# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Repository name: {repository["name"]}')
# print(f'Repository description: {repository["description"]}')

import requests
import lxml.html

html = requests.get('https://scrapeme.live/shop/').text
doc = lxml.html.fromstring(html)
print(doc)
