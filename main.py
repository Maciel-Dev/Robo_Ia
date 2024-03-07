import Location
import RobotClass
import sys


def main():

    start_place = input("Digite 'A' ou 'B' para o robo iniciar: ").upper()

    if start_place == "A" or start_place == "B":
        location_obj = [Location.Location(name="A", status=0), Location.Location(name="B", status=0)]
        robo = RobotClass.Robot(state_location="B", state_execute=0, action=0)
        RobotClass.Robot.execute(robo, location_obj)

    else:
        print("Favor, selecionar lugares entre A e B")
        print("Robo bugou, reinicie a chamada do programa...")
        sys.exit()


if __name__ == "__main__":
    main()
