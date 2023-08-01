from bs4 import BeautifulSoup
import json

print('References (r, R), or all (a,A)?\n')
choice = str(input()).lower()

input_list = ['r', 'a']
full_list = ['references']
parse_list = []

if choice not in input_list:
    print('\nTry again, the input was not valid.\n\n')
    exit()
if choice == 'a':
    parse_list = full_list
else:
    parse_list = [full_list[input_list.index(choice)]]

root_folder = './'
export_folder = 'zotero_export/'

for type in parse_list:

    html_file_name = f'LinkedMusic_{type}.html'
    path = f'{type}/content.json'

    with open(export_folder + html_file_name) as f:
        html_soup = BeautifulSoup(f, 'html.parser')

    content_array = []

    for html_tag in html_soup.findAll('div', {'class': 'csl-entry'}):
        content_array.append(str(html_tag))

    # sort alphabetically by author
    print(content_array)
    content_array.sort()

    with open(path, 'w') as f:
        json.dump(content_array, f, indent=4)
