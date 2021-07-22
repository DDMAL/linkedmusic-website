from pybtex.database.input import bibtex

parser = bibtex.Parser()
bib_data = parser.parse_file('zotero_export/SIMSSAPublications.bib')
for e in bib_data.entries:
    if 'year' not in bib_data.entries[e].fields:
        print('ok')
        continue
    else:
        print('---')
        print('title:', e)
        # print(bib_data.entries[e])
        print('_template: publication')
        # print('conference:', bib_data.entries[e].fields['jou'])
        print('---')
