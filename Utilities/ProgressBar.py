# This is a progress bar solution made by ChesterChowWOV.
# https://gist.github.com/ChesterChowWOV/2b35c551b339adbf459363322aac5b4b
import sys

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("{}[{}{}] {}%/{}%\r".format(prefix, "█"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()