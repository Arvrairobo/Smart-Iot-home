# import requests
# url = "http://118.102.206.26/face_detect/media/user/1487913160newpic.jpg"
# response = requests.get(url)
# if response.status_code == 200:
#     with open("/home/kush/Desktop/FaceTrack/boy.png", 'w') as f:
#         f.write(response.content)


import urllib, urllib2, sys, os
import base64
# import os.path
# import ConfigParser
from emp import Ui_MainWindow
global config
from PyQt4.QtGui import QApplication, QMainWindow
import csv
import json

# config = ConfigParser.RawConfigParser()
if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        f = QMainWindow()
        form = Ui_MainWindow()
        form.setupUi(f)
        f.show()
        app.exec_()
        page = 'http://118.102.206.26/face_detect/web/index.php?'
        cfg_path = '/home/kush/Desktop/FaceTrack/FaceTrace.cfg'
        check = os.path.exists(cfg_path)
        if check == True:
            config.read(cfg_path)
            url = config.get('Settings', page)
        dict = form.getparams()
        raw_params = dict
        params = urllib.urlencode(raw_params)
        request = urllib2.Request(page, params)
        request.add_header("Content-type", "application/x-www-form-urlencoded; charset=UTF-8")
        page = urllib2.urlopen(request)
        info = page.info()
        print info
    except ValueError as er:
        print "There is value error", er
    except:
        print "no error"


# import requests
# url = 'http://118.102.206.26/jewellery/webservices/index.php?'
# files = {'mode': 'upload_image','imgg': open('/home/kush/Desktop/img.jpg', 'rb')}
# r = requests.post(url, files=files)
# print r.text, r.content