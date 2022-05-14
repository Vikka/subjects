from importlib import import_module

from pytest import fixture


@fixture
def module(request):
    """
    Fixture for module
    """
    path = request.node.path.parent.resolve()
    local_fill_me = path/'_fill_me.py'
    if local_fill_me.exists():
        print(f'Importing module: exercises.{path.name}._fill_me')
        return import_module(f'exercises.{path.name}._fill_me')

    print(f'Importing module: exercises.{path.name}.fill_me')
    return import_module(f'exercises.{path.name}.fill_me')
