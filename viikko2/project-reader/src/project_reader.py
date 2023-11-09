from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = toml.loads(request.urlopen(self._url).read().decode("utf-8"))
        # print(toml.loads(content))
        poetry = content['tool']['poetry']
        # deserialisoi TOML]-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        
        return Project(poetry['name'], poetry['description'], poetry['license'],
                       poetry['authors'], poetry['dependencies'], 
                       poetry['group']['dev']['dependencies'])
