import json, requests, sys
from emp1 import Ui_MainWindow
from PyQt4.QtGui import QApplication, QMainWindow, QPixmap
from PyQt4.QtCore import QString
import csv
app = QApplication(sys.argv)
f = QMainWindow()
form = Ui_MainWindow()
form.setupUi(f)
f.show()
app.exec_()
url = 'http://118.102.206.26/face_detect/web/index.php?'
dict = form.getparams()
params = {'mode' : str(dict.get('mode')), 'user_type' : str(dict.get('user_type')), 'employee_id' : str(dict.get('employee_id'))}
print params
resp = requests.get(url=url, params=params)
data = json.loads(resp.content)
print data
with open('/home/kush/Desktop/FaceTrack/data/names.csv', 'w+') as csvfile:
    fieldnames = ['name', 'empolyee_id', 'department', 'image', 'time_in', 'time_out']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0, len(data['data']) - 1, 1):
        writer.writerow(
            {'name': str(data['data'][i].get('name')), 'empolyee_id': str(data['data'][i].get('employee_id')),
             'department': str(data['data'][i].get('department')),
             'image': str(data['data'][i].get('image')), 'time_in': str(data['data'][i].get('time_in')),
             'time_out': str(data['data'][i].get('time_out'))})