# coding:utf8
import json
import urllib
import urllib2
# from WeixinUtils import NewsItem
import requests

__author__ = 'Jayvee'


# class MusicUtils:
# @staticmethod
def get_searchlist(name, limit=10):
    data = {"s": name, "type": "1", "limit": limit}
    # s = requests.Session()
    # s.headers.update({'Referer': 'http://music.163.com/'})
    html = requests.post(url='http://music.163.com/api/search/get/web', params=data,
                         headers={'Referer': 'http://music.163.com/'}).text
    # value = urllib.urlencode(data)
    # req = urllib2.Request("http://music.163.com/api/search/get/web")
    # req.add_header("Referer", "http://music.163.com/")
    # html = urllib2.urlopen(req, value).read()
    jsonobj = json.loads(html)
    list = []
    if jsonobj["result"]["songCount"] != 0:
        count = 0
        for obj in jsonobj["result"]["songs"]:
            song_name = obj["name"]
            artistname = obj["artists"][0]["name"]
            albumname = obj["album"]["name"]
            songid = obj["id"]
            details = json.loads(get_songdetails(songid))
            songurl = "http://music.163.com/m/song/%s" % songid
            mp3url = details['songs'][0]['mp3Url']
            songtitle = '%s\n%s-%s' % (song_name, artistname, albumname)
            picurl = details["songs"][0]["album"]["picUrl"]
            # if count == 0:
            #     picurl = details["songs"][0]["album"]["picUrl"] + "?param=250y250"
            # else:
            #     picurl = details["songs"][0]["album"]["picUrl"] + "?param=50y50"
            count += 1
            list.append({'songtitle': songtitle, 'song_name': name, 'artistname': artistname, 'albumname': albumname,
                         'songid': songid,
                         'songurl': songurl, 'mp3url': mp3url, 'picurl': picurl})
        return list
    else:
        return None


# @staticmethod
def get_songdetails(songid):
    url = 'http://music.163.com/api/song/detail/?id=%s&ids=%%5B%s%%5D&csrf_token=Method=GET' % (songid, songid)
    req = urllib2.Request(url)
    req.add_header("Referer", "http://music.163.com/")
    resp = urllib2.urlopen(req)
    return resp.read()


    # ilist = get_searchlist("拥抱", 5)
    # for ii in ilist:
    # print ii.title
    # print ii.url
    # print ii.picurl


if __name__ == '__main__':
    print get_searchlist('秋意浓')
