class Program():

    def __init__(self, *args, **kwargs):
        self.lang = input("what language? ")
        self.version = float(input("Version? "))
        self.skill = input("What skill level? ")

    def upgrade(self):
        new_version = input("What version? ")
        print("We have updated the version, ", self.lang)
        self.version = new_version

p1 = Program()
p2 = Program()
