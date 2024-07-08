class ControllerShurima:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_view(self):
        data = self.model.get_data()
        self.view.display(data)