class laptop:
    storage_type ="ssd"

    def _init_(self , RAM ,storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(itself):#insstance method
        print(f"laptop has {self.RAM} RAM  & {self.storage} {self.storage_type}")


L1 = laptop("16gb" ,"512gb" )
L2 = laptop("8gb", "256gb")

L1.get_info()