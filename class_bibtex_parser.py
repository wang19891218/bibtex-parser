import os
import re


def function_parse_bib(str_file_name):
    list_str_line_content = []
    with open(str_file_name) as file_handle:
        for str_line_content in file_handle:
            list_str_line_content.append(str_line_content)

    dict_key_to_title = {}
    for i_line in range(len(list_str_line_content)):
        str_line_content = list_str_line_content[i_line]
        if str_line_content[0] == '@':
            temp_key = re.findall('{.*,', str_line_content)[0][1:-1]
            temp_str_title = ''
            for i_line_shift in range(20):
                str_line_content_shift = list_str_line_content[i_line + i_line_shift]
                if len(re.findall('title = {', str_line_content_shift)) > 0:
                    temp_str_title = re.findall('{.*}', str_line_content_shift)[0][1:-1]
                    break
            if temp_str_title == '':
                print('error for ', i_line, temp_key)
            temp_str_title = temp_str_title.replace('{', '')
            temp_str_title = temp_str_title.replace('}', '')
            dict_key_to_title[temp_key] = temp_str_title

    return dict_key_to_title
