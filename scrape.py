from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request as req

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
my_url = 'http://downloadming.fm/naam-shabana-2017-mp3-songs'

filename = "songs.csv"

f = open(filename, 'a')

headers = {'User-Agent': user_agent, }

complete_request = req(my_url, None, headers)

uClient = uReq(complete_request)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

title_container = page_soup.findAll("h2", {"class": "post-title"})

movie_name = title_container[0].text
movie_name = movie_name.replace(",", " |")
print(movie_name)
containers = page_soup.findAll("div", {"class": "entry"})

image = containers[0].p.img["src"]
print(image)
try:
    star_cast = containers[0].find(text="Star Cast:").parent.parent.text.replace("\xa0", " ").replace('\n', ' ')
    star_cast = star_cast.replace(",", " |")
except (AttributeError):
    try:
        star_cast = containers[0].find(text="Star Cast:\xa0").parent.parent.text.replace("\xa0", " ").replace('\n', ' ')
        star_cast = star_cast.replace(",", " |")
    except AttributeError:
        star_cast = ""
        pass
print(star_cast)

table_body = containers[0].table.tbody
row=table_body.findAll("td")
j = 3
k=4
l=5
run = True
for i in row:

    while run:
        try:
            song_name = row[j].contents[1]
            song_name = song_name.replace(",", " | ")

        except IndexError:
            run = False
            break
            pass
        try:
            singer = row[j].contents[4].text.replace("\n", "")
            singer = singer.replace(",", " |")
            j = j + 3
        except (IndexError, NameError):
            singer = ""
            j = j + 3
            pass

        if run == True:
            try:
                link_low = row[k].find('a').get('href')
                k=k+3
            except:
                pass
        if run == True:
            try:
                link_high = row[k].find('a').get('href')
                l=l+3
            except:
                pass
        print(movie_name + "," + image + "," + star_cast + ","  + song_name + "," + singer+ "," +link_low + "," + link_high + "\n")
        f.write(movie_name + "," + image + "," + star_cast + ","  + song_name + "," + singer+ "," +link_low + "," + link_high + "\n")



    # brand = container.div.div.a.img["title"]

    # title_container = container.findAll("a", {"class": "item-title"})
    # product_name = title_container[0].text

    # shipping_container = container.findAll("li", {"class": "price-ship"})
    # shipping = shipping_container[0].text.strip()

    # clean the commas from data
    # brand = brand.replace(",", "|")
    # product_name = product_name.replace(",", "|")
    # shipping = shipping.replace(",", "|")

    # print("brand: " + brand)
    # print("product name: " + product_name)
    #print("shipping: " + shipping)



