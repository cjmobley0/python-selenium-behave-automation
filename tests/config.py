import yaml, os, time


class Loader(yaml.Loader):

    def __init__(self, stream):

        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):

        filename = os.path.join(self._root, self.construct_scalar(node))

        with open(filename, 'r') as f:
            return yaml.load(f, Loader)

Loader.add_constructor('!include', Loader.include)

with open(os.path.join(os.path.dirname(__file__), 'resource', 'config.yml'), 'rU') as path_config_file:
    try:
        config = yaml.load(path_config_file, Loader)
    except yaml.YAMLError as exc:
        print(exc)
