#fixear la url para que solo necesite el handle y pasar los parametros a la UI

def get_youtube_channel_ID():
    import requests
    from lxml import etree
    import re
    url = "https://www.youtube.com/@midulive/videos"

    response = requests.get(url)
    text = response.text
    hrefUrls = re.findall(r'hrefUrl":"(.*)', text)
    id_pattern = r'https://m\.youtube\.com/channel/([^\s]+)'
    matches = re.findall(id_pattern, text)
    my_string = ' '.join(map(str, matches))  # This handles non-string elements in the list
    return (my_string[0:24])


get_youtube_channel_ID()
