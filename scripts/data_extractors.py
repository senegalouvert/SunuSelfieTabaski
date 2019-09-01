def combine_urls(base_dir, start_day=11, end_day=17, month=8):
    """ Allows to read all the chunks of files 
        holding the urls and combine them in one huge list
    """
    urls = []
    for day in range(start_day, end_day + 1):
        month_r = f'0{month}' if month < 10 else f'{month}'
        filename = f"{base_dir}/{day}-{month_r}"
        with open(filename) as file:
            urls += [line.replace('\n', '') for line in file.readlines()]
    return urls

def gen_pictures_csv(urls, filename="photo_urls.csv"):
    """ Allows to split urls and generates a csv file 
        holding every twitter @ with the corresponding photos 
    """
    first = True
    for url in urls:
        try:
            username = url.split("/")[3]
            with open(filename, 'a+') as file:
                if first:
                    file.write("username,url\n")
                else:
                    file.write(f"{username},{url}\n")
            first = False
        except IndexError:
            continue
    
if __name__ == "__main__":
    base_dir = "data/urls_files"
    gen_pictures_csv(combine_urls(base_dir))