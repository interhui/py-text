# coding=utf-8

import types

def is_blank(string):
    return True if string == None else False

def is_empty(string):
    if string == None:
        return True
    string = str(string)
    if string == '':
        return True
    string = string.strip()
    if string == '':
        return True
    return False

def is_not_blank(string):
    return not is_blank(string)

def is_not_empty(string):
    return not is_empty(string)

def is_numeric(string):
    if is_blank(string):
        return False
    return to_string(string).isdigit()

def is_bool(string):
    if is_blank(string):
        return False
    string = str(string).lower()
    if string == 'true' or string == 'false':
        return True
    else:
        return False

def index_of(string, search_str):
    if is_blank(string) or is_blank(search_str):
        return -1
    
    string = str(string)
    search_str = str(search_str)
    
    if search_str in string:
        return str(string).index(str(search_str))
    else:
        return -1

def index_of_any(string, search_strs):
    if is_blank(string):
        return -1
    string = str(string)
    if search_strs != None and type(search_strs) == types.ListType:
        for search_str in search_strs:
            if is_blank(search_str):
                continue
            if str(search_str) in string:
                return string.index(search_str)
    return -1

def index_of_ignore_case(string, search_str):
    if is_blank(string) or is_blank(search_str):
        return -1
    string = str(string).lower()
    search_str = str(search_str).lower()
    if search_str in string:
        return string.index(search_str)
    return -1


def last_index_of(string, search_str):
    if is_blank(string) or is_blank(search_str):
        return -1
    string = str(string)
    search_str = str(search_str)
    if search_str in string:
        return string.rindex(search_str)
    else:
        return -1

def left(string, length):
    if is_numeric(length):
        if is_blank(string): 
            return None
        string = str(string)
        if len(string) <= length:
            return string
        return string[: length]
    return string

def right(string, length):
    if is_numeric(length):
        if is_blank(string): 
            return None
        string = str(string)
        if len(string) <= length:
            return string
        return string[len(string) - length: ]
    return string

def mid(string, start, length):
    if is_numeric(start) and is_numeric(length):
        if is_blank(string): 
            return None
        string = str(string)
        if len(string) <= start:
            return string
        end_pos = start + length
        if len(string) < end_pos:
            end_pos = len(string)
        return string[start: end_pos]
    return string

def left_pad(string, length, pad = '*'):
    if is_blank(string):
        string = ''
    repeat_str = repeat(pad, length)
    return repeat_str + string

def right_pad(string, length, pad = '*'):
    if is_blank(string):
        string = ''
    repeat_str = repeat(pad, length)
    return string + repeat_str

def repeat(string, repeat_count):
    if is_blank(string):
        string = '*'
    if repeat_count < 0:
        repeat_count = 0
    return ''.join([string for _ in range(repeat_count)])

def abbreviate(string, offset, max_width, pad = '*'):
    if is_blank(string):
        return None
    string = str(string)
    if len(string) <= offset:
        return string
    if len(string) - offset < max_width:
        max_width = len(string) - offset
    return string[:offset] + repeat(pad, max_width)

def count_matches(string, search_str):
    if is_blank(string) or is_blank(search_str):
        return 0
    string = str(string)
    search_str = str(search_str)
    return string.count(search_str)

def remove_pattern(string, regex):
    pass

def remove_end(string, search_str):
    if is_blank(string):
        return None
    string = str(string)
    if is_blank(search_str):
        return string
    
    string = str(string)
    search_str = str(search_str)
    index = last_index_of(string, search_str)
    
    return string[ :index] + string[index + len(search_str):] if index != -1 else string

def remove_start(string, search_str):
    if is_blank(string):
        return None
    string = str(string)
    if is_blank(search_str):
        return string
    
    string = str(string)
    search_str = str(search_str)
    index = index_of(string, search_str)
    
    return string[ :index] + string[index + len(search_str):] if index != -1 else string

def split(string, separator):
    if is_blank(string):
        return None
    
    result = []
    split_list = str(string).split(separator)
    for item in split_list:
        if is_not_empty(item):
            result.append(item.strip())
    return result

def strip_all(strings):
    if strings == None or type(strings) != types.ListType:
        return None
    
    result = []
    for string in strings:
        if is_not_blank(string):
            result.append(str(string).strip())
        else:
            result.append(None)
    return result

def substring_after(string, tag):
    if is_blank(string):
        return None
    string = str(string)
    if is_blank(tag):
        return string
    index = index_of(string, tag)
    if index != -1:
        return string[index + len(tag):]
    else:
        return string

def substring_after_last(string, tag):
    if is_blank(string):
        return None
    string = str(string)
    if is_blank(tag):
        return string
    index = last_index_of(string, tag)
    if index != -1:
        return string[index + len(tag):]
    else:
        return string
    
def substring_before(string, tag):
    if is_blank(string):
        return None
    string = str(string)
    if is_blank(tag):
        return string
    index = index_of(string, tag)
    if index != -1:
        return string[:index]
    else:
        return string

def substring_before_last(string, tag):
    if is_blank(string):
        return None
    string = str(string)
    if is_blank(tag):
        return string
    index = last_index_of(string, tag)
    if index != -1:
        return string[:index]
    else:
        return string

def substring_between(string, open_tag, close_tag):
    if is_blank(string):
        return string
    
    open_tag_index = index_of(string, open_tag)
    close_tag_index = index_of(string, close_tag)
    
    open_tag_index = 0 if open_tag_index == -1 else open_tag_index + len(open_tag)
    close_tag_index = len(string) if close_tag_index == -1 else close_tag_index

    return string[open_tag_index : close_tag_index]

def startswith(string, prefix):
    if is_not_blank(string) and is_not_blank(prefix):
        return string.startswith(prefix)
    return False

def startswith_any(string, prefixs):
    if prefixs != None and type(prefixs) == types.ListType:
        for prefix in prefixs:
            if startswith(string, prefix):
                return True
    return False

def endswith(string, suffix):
    if is_not_blank(string) and is_not_blank(suffix):
        return string.endswith(suffix)
    return False

def endswith_any(string, suffixs):
    if suffixs != None and type(suffixs) == types.ListType:
        for suffix in suffixs:
            if endswith(string, suffix):
                return True
    return False
def contains_any(string, search_strs):
    if is_blank(string):
        return False
    if type(search_strs) == types.ListType:
        for search_str in search_strs:
            result = contains(string, search_str)
            if result:
                return result
    else:
        return contains(string, str(search_strs))
    return False

def contains(string, search_str):
    if is_not_blank(string) and is_not_blank(search_str):
        return search_str in string
    return False

def to_string(string):
    if is_blank(string):
        return None
    return str(string)

def reverse(string):
    char_list = str(string).split()
    char_list = char_list.reverse()
    return ''.join(char_list)

def replace_all(string, search_str, replacement):
    if is_blank(string):
        return None
    
    string = str(string)
    if is_blank(search_str) or is_blank(replacement):
        return string
    
    search_str = str(search_str)
    replacement = str(replacement)
    
    return string.replace(search_str, replacement)
    

def replace_each(string, search_list, replacement_list):
    if is_blank(string):
        return None
    string = str(string)
    
    if search_list == None or replacement_list == None:
        return string
    
    if type(search_list) == types.ListType and \
        type(replacement_list) == types.ListType and \
        len(search_list) == len(replacement_list):
        
        for i in range(len(search_list)):
            search_str = search_list[i]
            replacement = replacement_list[i]
            
            if is_blank(search_str) or is_blank(replacement):
                continue
            
            search_str = str(search_str)
            replacement = str(replacement)
            
            string = string.replace(search_str, replacement)
            
    return string
        