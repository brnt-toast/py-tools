from ..utils.html import html 

thing = html.html()

def write_file(name, content):

    with open(name, 'w', encoding='utf-8') as f:
        f.write(content)
        f.close()

test = "test.html"
print(thing)