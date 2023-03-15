from input_url import url

def create_name_page():
    #index volume in url
    index_v_start_in_url = url.find('v', 20)
    index_v_end_in_url = url.find('/c', 20)
    value_v = url[index_v_start_in_url : index_v_end_in_url]

    #index chapter in url
    index_c_start_in_url = url.find('c', 20)
    index_c_end_in_url = url.find('?', 20)
    value_c = url[index_c_start_in_url : index_c_end_in_url]

    name_page = value_v + ' ' + value_c + ' page '

    return name_page
