def create_html(filename, data):
    f = open(filename + '.html', 'w')

    header = """<html>
<head></head>
<body>
"""
    body = ''
    for p in data:
        body += """<p>""" + p[0] + """<br />""" + p[1] + """</p>"""

    footer = """
</body>
</html>
"""
    f.write(header + body + footer)
    f.close()
    return
