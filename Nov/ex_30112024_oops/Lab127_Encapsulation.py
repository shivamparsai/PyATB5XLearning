class car:
    def __init__(self, o_name, o_power, o_model):
        self.name = o_name
        self.power = o_power
        self.model = o_model

    def start_engin(self):
        print("starting a car with the name "+ self.name)
        print("starting a car with the power "+ self.power)
        print("starting a car with the model "+ self.model)

lambo = car("lambo", "1.5 turbo", "2023")
lambo.start_engin()

print("=============================")

MG = car("Hector", "1.5", "2025")
MG.start_engin()