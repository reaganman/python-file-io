import re

with open('origin.txt','r') as orgin:
    to_search = orgin.read()
    pattern = re.compile(r'\w*herit\w*', re.IGNORECASE)
    found = re.finditer(pattern, to_search)
    with open('origin_out.txt','w') as outfile:
        for i in found:
            line_found = to_search.count('\n', 0, i.start()) + 1
            to_write = f"{line_found}\t{i.group(0)}\n"
            outfile.write(to_write)
