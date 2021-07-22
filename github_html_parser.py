from bs4 import BeautifulSoup
from urllib.parse import unquote
import re
import os
import markdown
import shutil

full_list = ['media', 'presentations', 'publications']

simssa_root_folder = './'
export_folder = 'zotero_export/'

for type in full_list:

    html_file_name = f'SIMSSA_{type}.html'
    citation_folder = f'_{type}'

    with open(export_folder + html_file_name) as f:
        html_soup = BeautifulSoup(f, 'html.parser')

    # Save html (div) and ascii title [ [<div></div>, "Example Title"]]

    shutil.rmtree(citation_folder)
    os.makedirs(citation_folder)

    html_array = []

    for html_tag in html_soup.findAll('div', {'class': 'csl-entry'}):
        # print(tag.find_next('span'))
        # if html_tag.find('a'):
        #     continue
        parse_attr = html_tag.find_next('span')['title']
        year = 'n.d.'
        author = 'no_author'
        title = ')no_title'
        a_title = ')no_a_title'
        b_title = ')no_b_title'
        if 'rft.date' in parse_attr:
            year = parse_attr.split('rft.date=')[1].split('-')[0].split('&')[0]
        if 'rft.aulast' in parse_attr:
            author = unquote(parse_attr.split('rft.aulast=')[1].split('&')[0])
        if 'rft.title' in parse_attr:
            title = unquote(parse_attr.split('rft.title=')[1].split('&')[0])
        if 'rft.atitle' in parse_attr:
            a_title = unquote(parse_attr.split('rft.atitle=')[1].split('&')[0])
        if 'rft.btitle' in parse_attr:
            b_title = unquote(parse_attr.split('rft.btitle=')[1].split('&')[0])

        final_title = ''
        for t in [title, a_title, b_title]:
            if t.split('_')[0] != ')no':
                final_title = t
                break
        file_name = author + '_' + final_title.replace(' ', '_') + '_' + year + '.md'

        if not os.path.exists(simssa_root_folder + citation_folder + '/' + year):
            os.makedirs(simssa_root_folder + citation_folder + '/' + year)
        with open(simssa_root_folder + citation_folder + '/' + year + '/' + file_name, 'w') as f:
            f.write(f'---\npresentation_year: {year}\nyear: {year}\n---\n\n{html_tag.decode_contents()}')

        print(html_tag.decode_contents(), '\n')
        print(parse_attr, '\n')
        print('T', final_title, '\n\n')

    # print("unsorted")
    # for x in html_array: print(x[0], x[1])
    html_array = sorted(html_array, key = lambda x: (x[0], x[1]))
    # print("\nsorted")
    # for x in html_array: print(x[0], x[1], x[2], "\n")
