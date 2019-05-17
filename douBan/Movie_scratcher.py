import requests
import re
import base64
import time


class MovieScrathcer(object):
    @classmethod
    def is_header(cls, header):
        if not header:
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
            }
        return header

    @classmethod
    def movie_watch_on_url(cls, url):
        source_url = url
        movie_url = 'http://jx.aeidu.cn/index.php?url={}'.format(source_url)
        return movie_url

    @classmethod
    def movie_download_on_url(cls, url, header=None):
        try:
            header = cls.is_header(header)
            source_url = url
            response = requests.get(url='http://jiexi.a0296.cn/?url=' + source_url, headers=header)
            text = re.findall(r'\$\.post\("api\.php",{([\s\S]*)},function', response.text, )[0].strip().split('\n')
            referer = text[1].split(':')[-1].strip(',').strip("'")
            key = text[-1].split(':')[-1].strip("'")

            base64_url = base64.b64encode(source_url.encode())
            formdata = {
                'url': source_url,
                'referer': referer,
                'ref': 0,
                'time': int(time.time()),
                'type': "",
                'other': base64_url,
                'key': key
            }
            data = requests.post(url='http://jiexi.a0296.cn/api.php', data=formdata, headers=header).json()
            if data.get('title'):
                return data['url']
            else:
                return None
        except Exception as e:
            print('================================================================错误：',e)
            return None



if __name__ == "__main__":
    url = MovieScrathcer.movie_watch_on_url('https://www.iqiyi.com/v_19rsiwm8tk.html#vfrm=19-9-0-1')
    print(url)

    download_url = MovieScrathcer.movie_download_on_url('https://www.iqiyi.com/v_19rsiwm8tk.html#vfrm=19-9-0-1')
    print(download_url)
