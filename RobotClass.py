from Location import Location
from time import sleep


class Robot:
    # Para conhecimento:
    # (0,1) -> Lugar A/B
    # (0,1) -> Ocioso/Limpando
    # Action (0, 1, 2) -> Parado, mover para a esquerda, mover para a direita

    def __init__(self, state_location, state_execute, action):
        self.state_location = state_location
        self.state_execute = state_execute
        self.action = action

    def execute(self, location: list[Location]):

        if self.state_location == "B":
            location = location[::-1]

        cleaning_place_task = location[:]

        for loc in location:
            if loc.name == self.state_location:
                cleaning_place_task.remove(loc)
                self.state_execute = 1
                print("Limpando")
                sleep(2)

                print("limpo")

                if loc.name == "A":
                    if len(cleaning_place_task) == 0:
                        print("Trabalho finalizado")

                    else:
                        print("Movendo para a direita")
                    self.action = 2
                    self.state_location = "B"
                    self.state_execute = 0
                    self.state_execute = 0
                    self.action = 0

                else:
                    if len(cleaning_place_task) == 0:
                        print("Trabalho finalizado")

                    else:
                        print("Movendo para a Esquerda")
                    self.action = 1
                    self.state_location = "A"
                    self.state_execute = 0
                    self.state_execute = 0
                    self.action = 0