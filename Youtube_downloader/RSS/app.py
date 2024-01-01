import feedparser
import pandas as pd
import os

def get_last_Videos(url):
    url_parseada=feedparser.parse(url) #parseamos la url que se pasa como parametro
    test= [] #definimos un array donde vamos a guardar cada video
    for item in url_parseada['entries']:
        test.append(item.title) #del feed sacamos cada video y lo metemos al array que vamos a devolver
    
    return test

def get_last_Videos_urls(url):
    url_parseada=feedparser.parse(url) #parseamos la url que se pasa como parametro
    temp= [] #definimos un array donde vamos a guardar cada video
    for item in url_parseada['entries']:
        temp.append(item.link)
    return temp

def main():
    path = os.getcwd()
    path_full_feed=f'{path}//RSS'
    #path_full_feed=r'{}'.format(path_full_feed)

    rss_feed ='https://www.youtube.com/feeds/videos.xml?channel_id=UCDwccNij3DRkqxm1qXJbQzw'
    get_last_Videos(rss_feed)


    #cargamos el fichero que esta en la misma carpeta que este programa Feeds.xlsx
    feeds_file=pd.read_excel(f'{path_full_feed}//Feeds.xls')
    #leemos las urls del excel
    feeds_rss=feeds_file['RSS-Link']

    #cargamos listado de todos los videos actualmente
    videos=[]
    urls=[]

    for url in feeds_rss:
        videos= videos+ get_last_Videos(url)
        urls=urls + get_last_Videos_urls(url)
    
    #comparamos con los que ya bajamos la ultima vez es decir con videos.csv y urls.csv
    #iteramos por todos los videos del listado actual si en la ultima iteracion no ha habido cambios quiere decir que no hay videos nuevos

    #cargamos los videos del dataframe antiguo
    videos_old=pd.read_csv(f'{path_full_feed}//videos.csv')
    urls_old=pd.read_csv(f'{path_full_feed}//urls.csv')

    videos_1 = [video for video in videos_old['0']]
    urls_1 = [url for url in urls_old['0']]

    videos_nuevos=[]
    urls_nuevos=[]


    #comparar videos del rss con los ultimos medidos
    #si hay diferencia meterlos a videos nuevos y generar nuevo csv
    for i in range(0,len(videos)):
        if videos[i] in videos_1:
            print("El video ya estaba en la lista,por lo que no se añade")
        else:
            print('Añadimos video al listado')
            videos_nuevos.append(videos[i])
            urls_nuevos.append(urls[i]) 

    pd.DataFrame(urls_nuevos).to_csv(f'{path_full_feed}//new_videos.csv')

    pd.DataFrame(videos).to_csv(f'{path_full_feed}//videos.csv')
    pd.DataFrame(urls).to_csv(f'{path_full_feed}//urls.csv')

