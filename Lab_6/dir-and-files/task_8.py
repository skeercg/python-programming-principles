import os

path = '/Users/khas/Downloads/Пролетая над гнездом кукушки.epub'

if (os.access(path, os.F_OK)):
    os.remove(path)
