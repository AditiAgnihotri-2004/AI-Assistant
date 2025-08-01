#https://www.google.com/search?q=https://www.google.com/search?q=weather+kanpur
#user agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36
# span  id="wob_tm"
from requests_html import HTMLSession

def Weather():
    s = HTMLSession()
    query = "kanpur"
    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    })

    temp = r.html.find('span#wob_tm', first=True)
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
    desc = r.html.find('span#wob_dc', first=True)

    if temp and unit and desc:
        return f"{temp.text} {unit.text}, {desc.text}"
    else:
        return "Weather information not found."