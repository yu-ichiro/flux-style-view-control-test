# data -> view -> action -> data
from ui import View

class ViewController:
    _view: View

    def __init__(self):
        self._view = View()

    def render(data):
        raise NotImplementedError

    @property
    def view(self):
        return self._view
