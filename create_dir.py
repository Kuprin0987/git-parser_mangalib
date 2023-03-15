import os
from input_url import url

def create_name_dir():
    # to find index chapter and indexes for name manga
    index_c_in_url = url.find('/c', 20)   #20 что бы не найти "c" в названиии
    index_question_in_url = url.find('?', 20)
    
    index_start_name_manga = url.find('mangalib.me/') + len('mangalib.me/')
    index_end_name_manga = url.find('/v', 20)

    # name manga
    name_manga = url[index_start_name_manga : index_end_name_manga]
    
    # name dir
    name_dir = name_manga + ' chapter ' + url[index_c_in_url+2 : index_question_in_url]
    
    return name_dir

def create_dir():
    name_dir = create_name_dir()

    # create or replacement dir
    if name_dir in os.listdir():
        print(f'У вас уже есть директрория {name_dir}(можете удалить директрорию и запустить программу заново)')
    else:
        os.mkdir(name_dir)
        return True
        
