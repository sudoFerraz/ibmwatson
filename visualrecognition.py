from watson_developer_cloud import VisualRecognitionV3 as vr
import json


instance = vr(api_key='48bb0bb1b8ed256d63982f767aeb6874f251e712', version='2016-05-20')

img = instance.classify(images_url='https://amenteemaravilhosa.com.br/wp-content/uploads/2015/06/Solid%C3%A3o-.jpg')

img['images'][0]['classifiers'][0]['classes']

print json.dumps(img)
