import json
from watson_developer_cloud import VisualRecognitionV3

#API Setup
visual_recognition = VisualRecognitionV3('2016-05-20', api_key='48bb0bb1b8ed256d63982f767aeb6874f251e712')

#classify an image By URL
results = visual_recognition.classify(images_url="http://i.imgur.com/EmSTlTc.jpg")
print(json.dumps(results))


#Detect faces via URL
faceResults = visual_recognition.detect_faces(images_url='http://i.imgur.com/UoO6jjl.jpg')
print(json.dumps(faceResults))


#Recognize Text in the image by URL
textResults = visual_recognition.recognize_text(images_url='http://i.imgur.com/BTT8zsO.jpg')
print(json.dumps(textResults))
