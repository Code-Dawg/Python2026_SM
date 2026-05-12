class Person:
    name=""
    def __init__(self,name,age,addr):

        self.name=_name
        self.age=_age
        self.addr=_addr

    def get_name(self):
        return "self_name"

    def can_vote(self):
        if self.age>=18:
            return f("Yes (self.name) can vote and age is (self.age)")
        return"No They cannot Vote"


a=Person("darshan",20,"Pokhara")
print(a.name,a.age,a.addr)



