import sys, re
page, img, caption, heading, mode, ref = sys.argv[1:7]

m = re.search(r'<figure class="([^"]+)"', open(ref).read())
cls = m.group(1) if m else "archive-figure"

html = open(page).read()
if img in html:
    sys.exit("Already has " + img)
if heading not in html:
    sys.exit("Heading not found: " + heading)

fig = (f'<figure class="{cls}">\n'
       f'<img src="{img}" alt="{caption}" loading="lazy">\n'
       f'<figcaption>{caption}</figcaption>\n</figure>\n\n')

i = html.index(heading)
if mode == "before":
    j = html.rfind("<h2", 0, i)
    html = html[:j] + fig + html[j:]
else:
    j = html.index("</p>", i) + 4
    html = html[:j] + "\n\n" + fig + html[j:]

open(page, "w").write(html)
print("Done:", img)
