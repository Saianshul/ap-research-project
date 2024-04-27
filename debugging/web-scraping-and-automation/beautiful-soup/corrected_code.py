from bs4 import BeautifulSoup
from bs4 import Comment

html_1 = """
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>Website</title>
        <link rel="stylesheet" type="text/css"/>
    </head>

    <body>
        <div class="links">
            <a href="https://youtube.com/">Link 2</a>
            <a href="https://google.com/">Link 2</a>
            <a href="https://amazon.com/">Link 3</a>
            <a href="https://netflix.com/">Link 4</a>
        </div>

        <div class="img">
            <img src="img1.jpg" width="100%" height="400px"/>
            <p>Image Description</p>
        </div>

        <div class="lists">
            <div id="list-1">
                <p>
                    <ol>
                        <li>Item 4</li>
                        <li>Item 11</li>
                        <li>Item 8</li>
                    </ol>
                </p>
            </div>

            <div id="list-2">
                <p>
                    <ul>
                        <li>Item 2</li>
                        <li>Item 5</li>
                    </ul>
                </p>
            </div>
        </div>

        <div id="descriptions">
            <div class="description-1">
                <center>
                    <a href="https://gmail.com/">
                        <img src="img2.png" width="200px" height="200px"/>
                    </a>
                    <h3>Gmail</h3>
                </center>
                <p>Description 1</p>
            </div>

            <div class="description-2">
                <p>Description 2</p>
            </div>
        </div>
    </body>
</html>
"""

soup_1 = BeautifulSoup(html_1, 'html.parser')

html_tag = soup_1.find('html')
html_tag['lang'] = 'en'

link_tag = soup_1.find('link')
link_tag['href'] = 'style.css'

first_a_tag = soup_1.find('a')
first_a_tag.string = 'Link 1'
links_div_tag = soup_1.find('div', {'class': 'links'})
for i, a in enumerate(links_div_tag.find_all('a')):
    a['id'] = f'link-{i + 1}'

first_p_tag = soup_1.find('p')
new_b_tag = soup_1.new_tag('b')
new_a_tag = soup_1.new_tag('a', href='image.com')
new_a_tag.string = 'Image Description'
new_b_tag.append(new_a_tag)
first_p_tag.replace_with(new_b_tag)

section_1_div_tag = soup_1.new_tag('div', attrs={'id': 'section-1'})
img_div = soup_1.find('div', {'class': 'img'})
section_1_div_tags = []
section_1_div_tags.append(links_div_tag)
section_1_div_tags.append(img_div)
for div_tag in section_1_div_tags:
    section_1_div_tag.append(div_tag.extract())
body_tag = soup_1.find('body')
body_tag.insert(section_1_div_tag)
# body_tag.insert(0, section_1_div_tag)

lists_div_tag = soup_1.find('div', {'class': 'lists'})
for list_div_tag in lists_div_tag.find_all('div'):
    for li_tag in list_div_tag.find_all('li'):
        item_num = int(li_tag.text.split(' ')[1])
        if item_num % 2 != 0:
            i_tag = soup_1.new_tag('i')
            # i_tag.string = li_tag.string
            li_tag.string.replace_with(i_tag)

center_tag = soup_1.find('center')
center_tag.replace_with(center_tag.contents)
# center_tag.replace_with(*center_tag.contents)

description_2_div = soup_1.find('div', {'class': 'description-2'})
description_2_p_tag = description_2_div.find('p')
comment = Comment('Description 3')
description_2_p_tag.append(comment)

section_2_div_tag = soup_1.new_tag('div', attrs={'id': 'section-2'})
lists_div_tag.wrap(section_2_div_tag)

html_2 = """
<html lang="en">
    <head>
        <meta charset="UTF-8"/>
        <title>Website</title>
        <link rel="stylesheet" type="text/css" href="style.css"/>
    </head>

    <body>
        <div id="section-1">
            <div class="links">
                <a id="link-1" href="https://youtube.com/">Link 1</a>
                <a id="link-2" href="https://google.com/">Link 2</a>
                <a id="link-3" href="https://amazon.com/">Link 3</a>
                <a id="link-4" href="https://netflix.com/">Link 4</a>
            </div>

            <div class="img">
                <img src="img1.jpg" width="100%" height="400px"/>
                <b><a href="image.com">Image Description</a></b>
            </div>
        </div>

        <div id="section-2">
            <div class="lists">
                <div id="list-1">
                    <p>
                        <ol>
                            <li>Item 4</li>
                            <li><i>Item 11</i></li>
                            <li>Item 8</li>
                        </ol>
                    </p>
                </div>

                <div id="list-2">
                    <p>
                        <ul>
                            <li>Item 2</li>
                            <li><i>Item 5</i></li>
                        </ul>
                    </p>
                </div>
            </div>
        </div>

        <div id="descriptions">
            <div class="description-1">
                <a href="https://gmail.com/">
                    <img src="img2.png" width="200px" height="200px"/>
                </a>
                <h3>Gmail</h3>
                <p>Description 1</p>
            </div>

            <div class="description-2">
                <p>Description 2<!--Description 3--></p>
            </div>
        </div>
    </body>
</html>
"""

soup_2 = BeautifulSoup(html_2, 'html.parser')

print(soup_1.prettify() == soup_2.prettify())