import time
import threading

def caculate_time(func):
    
    def wrapper_func(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        finish = time.perf_counter()
        print(finish - start)
        return func.__name__
    
    return wrapper_func

@caculate_time
def test(sec=0, *args, **kwargs):
    sleep_time = kwargs.get('sleep_time', 1)
    my_id = threading.current_thread()
    if sec != 0:
        sleep_time = sec
    print("{} - START".format(my_id))
    time.sleep(sleep_time)
    print("{} - FINISTH".format(my_id))

# start = time.perf_counter()

# 현재 이 스크립트 파일을 동작시키는건 main_thread
main_thread = threading.main_thread()
print("MAIN THREAD : ", threading.current_thread())
assert main_thread is threading.current_thread()

# make thread
t1 = threading.Thread(target=test)
t2 = threading.Thread(target=test)

#run thread
t1.start()
t2.start()

#wait target function. 지금 예시는 test func
t1.join()
t2.join()

# finish = time.perf_counter()

# print( finish - start )
print("=" * 50)

start = time.perf_counter()
threads = []
for i in range(10):
    t = threading.Thread(target=test, kwargs={'sleep_time' : 0.5})
    t.start()
    threads.append(t)
    # t.join()

for thread in threads:
    thread.join()

finish = time.perf_counter()

print( finish - start )
print("=" * 50)

import concurrent.futures

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(test, sleep_time=0.5)
    f2 = executor.submit(test)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(finish - start)
print("=" * 50)


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(test, sleep_time=0.5) for _ in range(10)]

#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    time_list = [0.5]*10
    # results = executor.map(test, time_list) # 해당 functino 의 return 값이 이미 들어가 있음.

    # map 을 사용하는데 kwargs 를 보내고 싶을 때, lambda 식을 쓸 수 있다.
    results = executor.map(lambda x: test(sleep_time=x), time_list)

    for result in results:
        print(result)

# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Threading/download-images.py
import requests
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c'
]

# start = time.perf_counter()
# for img_url in img_urls:
#     img_bytes = requests.get(img_url).content
#     img_name = img_url.split('/')[3]
#     img_name = f'{img_name}.jpg'
#     with open(img_name, 'wb') as img_file:
#         img_file.write(img_bytes)
#         print("downloading")
# finish = time.perf_counter()
# print(finish - start)

@caculate_time
def download_image(**kwargs):
    img_url = kwargs.get('img_url', None)
    if img_url == None:
        return None
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(lambda x: download_image(img_url=x), img_urls)
