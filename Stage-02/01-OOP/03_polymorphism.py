class Manager:
    def work(self):
        print("Manage teams")

class Developer:
    def work(self):
        print("Write codes")

class Designer:
    def work(self):
        print("Create Design")

d1 = Developer()
d2 = Manager()
d3 = Designer()

employees = [d1,d2,d3]

for emp in employees:
    emp.work()