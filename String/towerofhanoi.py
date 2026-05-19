# Tower of Hanoi
import time

class Tower:

    def __init__(self):

        print("WELCOME TO TOWER OF HANOI GAME")
        print()

        print("Given Problem    A= [3,2,1]     B= []     C= []")
        print()

        print("Expected Output  A= []          B= []     C= [3,2,1]")
        print()

        self.A = []
        self.B = []
        self.C = []

    # inserting disks into Tower A
    def tower(self, item):

        self.A.append(item)

        time.sleep(2)

        print("A:", self.A)
        print("Items in Tower A\n")

    # display all towers
    def display(self):

        print("A =", self.A)
        print("B =", self.B)
        print("C =", self.C)
        print("-" * 30)

    # recursive logic
    def solve(self, n, source, auxiliary, destination,
              source_name, auxiliary_name, destination_name):

        if n == 1:

            disk = source.pop()
            destination.append(disk)

            print(f"Move Disk {disk} from {source_name} to {destination_name}")

            self.display()

            time.sleep(2)

            return

        # step 1
        self.solve(n-1,
                   source,
                   destination,
                   auxiliary,
                   source_name,
                   destination_name,
                   auxiliary_name)

        # step 2
        disk = source.pop()
        destination.append(disk)

        print(f"Move Disk {disk} from {source_name} to {destination_name}")

        self.display()

        time.sleep(2)

        self.solve(n-1,
                   auxiliary,
                   source,
                   destination,
                   auxiliary_name,
                   source_name,
                   destination_name)




obj = Tower()

obj.tower(3)
obj.tower(2)
obj.tower(1)

print("Initial Towers")
obj.display()

time.sleep(2)


obj.solve(3,
          obj.A,
          obj.B,
          obj.C,
          "A",
          "B",
          "C")

print("FINAL OUTPUT")
obj.display()