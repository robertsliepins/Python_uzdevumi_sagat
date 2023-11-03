""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.
1)Rss?
2( plusmu no googlelv? google ir vietne bet nav satura raditaja, google izmanot rss,
"""
import feedparser
# URL uz RSS plusmu

rss_url='https://www.liepajniekiem.lv'

#iegusim rss plusmas darusn
kkk=feedparser.parse(rss_url)

#noformesana
for entry in kkk.entries:
    print("Virsrakts: ", entry.title)
    print("Saite:", entry.link )
    print("Publicesanas datuns: ", entry.published)
    print("\n")