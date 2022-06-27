import eel
from Search_Process import Search_process
from search import search
import json

eel.init('web')
process = search()


@eel.expose
def resp(r):
    process.__int__(r)
    return process.responce


eel.start('mainpage.html')
