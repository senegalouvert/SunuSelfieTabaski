with open('photo_urls.csv') as photos:
    lines = photos.readlines()[1:]
    for line in lines:
        username, url = line.split(',')
        from bs4 import BeautifulSoup
        from urllib.request import urlopen, urlretrieve, HTTPError
        doc = urlopen(url)
        soup = BeautifulSoup(doc, 'html.parser')
        images = soup.findAll('img')
        for img in images:
            try:
                src = img.attrs['src']
                import re
                r = re.search('https://pbs.twimg.com/media/(.*)', src)
                found = []
                if r:
                    found = r.group(0)
                dir_name = f"data/pictures/{username}/"
                import os
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name)
                dl = None
                if type(found) == type(list()):
                    dl = found
                else:
                    dl = [found]
                if len(dl) > 0:
                    for f in dl:
                        print(f)
                        try:
                            urlretrieve(f, dir_name + f.split('/')[-1])
                        except:
                            continue
            except KeyError:
                continue
            