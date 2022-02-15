from urllib import request
from project import Project

import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_content = toml.loads(content)["tool"]["poetry"]

        name = parsed_content["name"]
        description = parsed_content["description"] if parsed_content["description"] else "-"
        dependencies = list(parsed_content["dependencies"].keys())
        dev_dependencies = list(parsed_content["dev-dependencies"].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
