class ControllerShurima:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_reservation(self, name, date, time, type):
        self.model.add_reservation(name, date, time, type)

    def get_reservations(self):
        return self.model.get_reservations()

    def update_view(self):
        reservations = self.get_reservations()
        self.view.display(reservations)
