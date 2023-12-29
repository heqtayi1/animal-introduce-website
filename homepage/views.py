from django.shortcuts import render
from django_test.settings import STATICFILES_DIRS
from django.http import JsonResponse
import os
import io
import base64
import cv2
import matplotlib.pyplot as plt

def homepage(request):

    return render(request, 'homepage.html')
def animal_audiograph_creat():
    #创建一段连续的音频波形图
    import requests
    import matplotlib.pyplot as plt
    import numpy as np
    import base64
    from io import BytesIO
    str=["sheep","giraffe","cow","crow","penguin","rattlesnake"]
    #img_str = []
    for i in str:
        url = "https://www.google.com/logos/fnbx/animal_sounds/"+i+".mp3"
        des_url= os.path.join(STATICFILES_DIRS[0], 'audios_img')
        response = requests.get(url)
        audio_content = response.content

        # 确保 audio_content 的长度是 np.int16 元素大小的倍数
        remainder = len(audio_content) % 2  # np.int16 是 2 字节
        if remainder:
            audio_content += b'\x00'  # 添加一个空字节来使其成为 2 的倍数
    
        audio_data = np.frombuffer(audio_content, dtype=np.int16)

        # 创建一个时间向量，用于绘制波形图
        time = np.linspace(0., len(audio_data) / 44100., len(audio_data))
        plt.figure(figsize=(10,4))
        plt.plot(time, audio_data, color='blue')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.title('Waveform of Audio')
        plt.grid(True)
        #
        #buffer = BytesIO()
        #print(des_url+i)
        plt.savefig(des_url+i + '.png',format='png')
        #buffer.seek(0)
        # 将图像数据转换为Base64编码的字符串
        #img_str.append(base64.b64encode(buffer.read()).decode('utf-8'))
        plt.close()
    
    

def animal_page(request):
    str=["sheep","giraffe","cow","crow","penguin","rattlesnake"]
    for i in str:
        des_url= os.path.join(STATICFILES_DIRS[0], 'audios_img')
        if not os.path.exists(des_url+i+'.png'):
            animal_audiograph_creat()
        
    return render(request,'animal.html')

def image_list_page(request):
    image_path = os.path.join(STATICFILES_DIRS[0], 'images')
    image_dir = os.listdir(image_path)
    image_arr = []
    for item in image_dir:
        image_arr.append(os.path.join('/images', item))
    return render(request, 'image_list.html', {'image_arr': image_arr})

def video_list_page(request):
    video_path = os.path.join(STATICFILES_DIRS[0], 'videos')
    video_dir = os.listdir(video_path)
    video_arr = []
    for item in video_dir:
        video_arr.append(os.path.join('/videos', item))
    return render(request, 'video_list.html', {'video_arr': video_arr})

def upload(request):
    return render(request, 'upload.html')

def upload_image(request):
    upload_success = False
    if(request.method == 'POST'):
        image_content = request.FILES['image']
        image_name = image_content.name
        file_path = os.path.join(STATICFILES_DIRS[0], 'images', image_name)

        with open(file_path, 'wb+') as destination:
            for chunk in image_content.chunks():
                destination.write(chunk)
        upload_success = True
    return render(request, 'upload.html', {'image_name': image_name, 'upload_success': upload_success})


def upload_video(request):
    upload_success1 = False
    if (request.method == 'POST'):
        video_content = request.FILES['video']
        video_name = video_content.name
        file_path = os.path.join(STATICFILES_DIRS[0], 'videos', video_name)

        with open(file_path, 'wb+') as destination:
            for chunk in video_content.chunks():
                destination.write(chunk)
        upload_success1 = True
    return render(request, 'upload.html', {'video_name': video_name, 'upload_success1': upload_success1})


def search_image(request):
    if request.method == 'POST':
        search_content = request.POST.get('search_name')
        image_path = os.path.join(STATICFILES_DIRS[0], 'images')
        image_dir = os.listdir(image_path)
        image_arr = []
        for item in image_dir:
            if item == search_content or search_content == '':
                image_arr.append(os.path.join('/images', item))
    return render(request, 'image_list.html', {'search_content': search_content, 'image_arr': image_arr})


def imageProcessing(request):
    return render(request, 'image_process.html')

def load_image(request):
    # 在这里实现加载图像的逻辑
    image_url = 'static/images/7.jpg'
    return JsonResponse({'image_url': image_url})

def grayscale_image(request):
    url = request.GET.get('key1')
    src_path = url.split('/')[-1]
    image_path = os.path.join(STATICFILES_DIRS[0], 'images', src_path)
    des_path = os.path.join(STATICFILES_DIRS[0], 'images_result', src_path)

    if not os.path.exists(des_path):
        color_image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(des_path, gray_image)

    grayscale_image_url = 'static/images_result/' + src_path
    return JsonResponse({'grayscale_image_url': grayscale_image_url})

def imageRecognition(request):
    return render(request, 'image_recognition.html')

def Recognize(request):
    url = request.GET.get('key1')
    src_path = url.split('/')[-1]
    image_path = os.path.join(STATICFILES_DIRS[0], 'images', src_path)

    label = 'this image is tank'
    return JsonResponse({'label': label})


def chartDisplay(request):
    #图表数据可以读取static目录下的数据文件
    data = {'labels': ['A', 'B', 'C', 'D', 'E'],
            'values': [5, 9, 3, 7, 2]}
    plt.bar(data['labels'], data['values'])
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()
    return render(request, 'chart_display.html', {'image_base64': image_base64})