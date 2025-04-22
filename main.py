from controllers.trip_controller import TripController
from views.ui import run_ui

def main():
    run_ui(TripController())

if __name__ == "__main__":
    main()
