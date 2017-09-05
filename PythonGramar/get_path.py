#coding:utf-8

from lxml import etree

s = """
<html>
    <body>
        <a href="/1234.html">TEXT A</a>
        <a href="/3243.html">TEXT B</a>
        <a href="/7445.html">TEXT C</a>
    </body>
</html>
"""


html = etree.fromstring(s)


ele_a = html.xpath('.//*[text()="TEXT B"]')

if ele_a:
    ele = ele_a[0]
    abs_path = ele.getroottree().getpath(ele)
    print abs_path
