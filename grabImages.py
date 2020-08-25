import os, requests
from bs4 import BeautifulSoup

usr_agent = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive",
}
count = 0


def download(img):
    global count
    f = open("raw_image/%s.jpg" % count, "wb")
    print("downloaded %s.jpg" % count)
    f.write(img.content)
    f.close()
    count += 1
    print("done")


def grab(url):
    r = requests.get(url, headers=usr_agent)
    soup = BeautifulSoup(r.text, "html.parser")
    imgs = soup.find_all("img")
    for img in imgs:
        try:
            link = img["src"]
            if link.endswith("png"):
                # to avoid icons
                continue
            img = requests.get(link)
            download(img)
        except Exception as e:
            print(e)


def main():
    if not os.path.exists("raw_image"):
        print("making raw_image folder")
        os.makedirs("raw_image")
    for x in range(1, 51):
        url = (
            """https://www.gettyimages.co.uk/photos/mahendra-singh-dhoni?family=editorial&page="""
            + str(x)
            + """&phrase=mahendra%20singh%20dhoni&sort=mostpopular"""
        )
        print("starting...")
        grab(url)


main()
