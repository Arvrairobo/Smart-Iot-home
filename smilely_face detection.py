import cv2
import ipywidgets as widgets
from IPython.display import display, clear_output
from pylab import *
from sklearn import datasets
import json
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem
from sklearn import metrics

def train_and_evaluate(clf, X_train, X_test, y_train, y_test):
    clf.fit(X_train, y_train)

    print ("Accuracy on training set:")
    print (clf.score(X_train, y_train))
    print ("Accuracy on testing set:")
    print (clf.score(X_test, y_test))

    y_pred = clf.predict(X_test)

    print ("Classification Report:")
    print (metrics.classification_report(y_test, y_pred))
    print ("Confusion Matrix:")
    print (metrics.confusion_matrix(y_test, y_pred))


def evaluate_cross_validation(clf, X, y, K):
    # create a k-fold cross validation iterator
    cv = KFold(len(y), K, shuffle=True, random_state=0)
    # by default the score used is the one returned by score method of the estimator (accuracy)
    scores = cross_val_score(clf, X, y, cv=cv)
    print (scores)
    print ("Mean score: {0:.3f} (+/-{1:.3f})".format(
        np.mean(scores), sem(scores)))


svc_1 = SVC(kernel='linear')
faces = datasets.fetch_olivetti_faces()
faces.keys()
for i in range(10):
    face = faces.images[i]
    subplot(1, 10, i + 1)
    imshow(face.reshape((64, 64)), cmap='gray')
    axis('off')


def detect_face(frame):
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detected_faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=6,
            minSize=(100, 100),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
    return gray, detected_faces

random_image_button = widgets.Button(description="New image!")

def display_face_and_prediction(b):
    index = randint(0, 400)
    face = faces.images[index]
    display_face(face)
    print("this person is smiling: {0}".format(svc_1.predict(faces.data[index, :])==1))

random_image_button.on_click(display_face_and_prediction)
display(random_image_button)
display_face_and_prediction(0)



class Trainer:
    def __init__(self):
        self.results = {}
        self.imgs = faces.images
        self.index = 0

    def increment_face(self):
        if self.index + 1 >= len(self.imgs):
            return self.index
        else:
            while str(self.index) in self.results:
                print self.index
                self.index += 1
            return self.index

    def record_result(self, smile=True):
        self.results[str(self.index)] = smile


def display_face(face):
    clear_output()
    imshow(face, cmap='gray')
    axis('off')


def update_smile(b):
    trainer.record_result(smile=True)
    trainer.increment_face()
    display_face(trainer.imgs[trainer.index])

def update_no_smile(b):
    trainer.record_result(smile=False)
    trainer.increment_face()
    display_face(trainer.imgs[trainer.index])

if __name__ == '__main__':
    trainer = Trainer()
    button_smile = widgets.Button(description='smile')
    button_no_smile = widgets.Button(description='sad face')

    button_no_smile.on_click(update_no_smile)
    button_smile.on_click(update_smile)

    display(button_smile)
    display(button_no_smile)
    display_face(trainer.imgs[trainer.index])
    yes, no = (sum([trainer.results[x] == True for x in trainer.results]),
               sum([trainer.results[x] == False for x in trainer.results]))
    results = json.load(open('results.xml'))
    trainer.results = results
    bar([0, 1], [no, yes])
    ylim(0, max(yes, no))
    xticks([0.4, 1.4], ['no smile', 'smile']);

    smiling_indices = [int(i) for i in results if results[i] == True]

    fig = plt.figure(figsize=(12, 12))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
    for i in range(len(smiling_indices)):
        # plot the images in a matrix of 20x20
        p = fig.add_subplot(20, 20, i + 1)
        p.imshow(faces.images[smiling_indices[i]], cmap=plt.bone)

        # label the image with the target value
        p.text(0, 14, "smiling")
        p.text(0, 60, str(i))
        p.axis('off')
    indices = [i for i in trainer.results]
    data = faces.data[indices, :]
    target = [trainer.results[i] for i in trainer.results]
    target = array(target).astype(int32)
    X_train, X_test, y_train, y_test = train_test_split(
        data, target, test_size=0.25, random_state=0)
    evaluate_cross_validation(svc_1, X_train, y_train, 5)
    train_and_evaluate(svc_1, X_train, X_test, y_train, y_test)




