import os

list_photos = os.listdir("new photos")

    for idx, picture in enumerate (list_photos):
        fd=open (f"website/{idx}.html", "w")
        fd.write ('<!DOCTYPE html>\n')
        fd.write ('<html lang="en">')
        fd.write ('<head>')
        fd.write ('<meta charset="UTF-8">')
        fd.write ('<title>Images</title>')
        fd.write ('</head>')
        fd.write ('<body>')
        fd.write (f'img src')
        fd.write ('')
        fd.write ('')

html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Images</title>
</head>
<body>
    <!-- -->
    <img src="cat_pic.jpeg" alt ="picture of a cat" width="600">


</body>
</html>