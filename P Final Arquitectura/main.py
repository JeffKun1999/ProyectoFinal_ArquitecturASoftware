# main.py
from models.model_shurima import ModelShurima
from views.view_shurima import ViewShurima
from controllers.controller_shurima import ControllerShurima

def main():
    model = ModelShurima()
    view = ViewShurima()
    controller = ControllerShurima(model, view)

    controller.update_view()

if __name__ == "__main__":
    main()
