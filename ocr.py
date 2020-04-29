import os
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
from autocorrect import spell
from IPython.display import display,Image

api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = 'a512a2ed-e139-4d22-9528-7c078fdc0b5b'

def load(folder,imgs):
    for i in os.listdir(folder):
        imgs.append(os.path.join(folder,i))


def teacher_answer_scan():
    folder1="teachersanswer"
    imgs1=[]
    load(folder1,imgs1)
    print("Images containing teachers answer:",imgs1)
    test1=""
    for image1 in range(len(imgs1)):
        try:
            # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
            api_response = api_instance.image_ocr_post(imgs1[image1])
            test1+=api_response._text_result
            test1=test1.replace('\n',' ')+" "
        except ApiException as e:
            print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)
    test1=test1.lstrip(" ")
    test1=test1.rstrip(" ")
    print("TEACHER'S ANSWER:")
    for image1 in range(len(imgs1)):
        display(Image(filename=imgs1[image1]))
    print(test1,"\n")


def student_answer_scan():
    folder2="studentsanswer"
    imgs2=[]
    load(folder2,imgs2)
    print("Images containing students answer:",imgs2)
    test2=""
    for image2 in range(len(imgs2)):
        try:
            # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
            api_response = api_instance.image_ocr_post(imgs2[image2])
            test2+=api_response._text_result
            test2=test2.replace('\n',' ')+" "
        except ApiException as e:
            print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)
    test2=test2.lstrip(" ")
    test2=test2.rstrip(" ")
    test2=test2.replace('\n',' ')
    test3=test2
    print("STUDENT'S ANSWER:")
    for image2 in range(len(imgs2)):
        display(Image(filename=imgs2[image2]))
    print(test2,"\n")
    list1=test2.split(".")
    print(list1)

