class employee: 
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print("starting executing attributes/data")
        self.id = 123
        self.salary = 120000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    def travel(self, designation):
        print("This travel function was called manually")
        print(f"Employee is now travelling to {designation}")


#create an obj/instance of the class
sam = employee()

#printing the attributes
# print(sam.id)

# calling a method
sam.travel("Denmark")
