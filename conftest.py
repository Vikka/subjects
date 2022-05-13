from importlib import import_module

from pytest import fixture


@fixture
def module(request):
    """
    Fixture for module
    """
    path = request.node.path.parent.resolve()
    for p in path.iterdir():
        if p.suffix == '.py' and not p.name.startswith('test_'):
            print(f'Importing module: {path.name}.{p.stem}')
            return import_module(f'{path.name}.{p.stem}')
    raise Exception('No module found in {}'.format(path))
