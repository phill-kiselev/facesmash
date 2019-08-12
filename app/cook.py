import os, random
PATH_GIRLS = os.getcwd() + '/app/static/img/girls'

def get_impath(index):
    return os.listdir(PATH_GIRLS)[index]

def list_to_str(l):
    s = '_'.join(str(x) for x in l)
    return s
    
def str_to_list(s):
    l = s.split('_')
    l = list(map(int, l))
    return l

def generate_sequence():
    files = os.listdir(PATH_GIRLS)
    LEN = len(files)
    indexes = list(range(LEN))
    random.shuffle(indexes)
    indexes.append(0)
    return list_to_str(indexes)
    
def get_next_images(cooka):
    lcoo = str_to_list(cooka)
    cur_index = lcoo.pop()
    if cur_index <= len(lcoo)-2:
        im1, im2 = get_impath(lcoo[cur_index]), get_impath(lcoo[cur_index+1])
        lcoo.append(cur_index+2)
        strcoo = list_to_str(lcoo)
        return (im1, im2), strcoo
    else:
        cooka = generate_sequence()
        return get_next_images(cooka)
