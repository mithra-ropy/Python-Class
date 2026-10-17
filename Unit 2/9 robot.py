 r1 = {"name": "Alpha", "battery": 100}
 r2 = {"name": "Beta", "battery": 60}


# def drain(robot, amount):
#     robot["battery"] = max(0, robot["battery"] - amount)


# def status(robot):
#     return f'{robot["name"]}:{robot["battery"]}%'


# drain(r1, 35)
# print(status(r1))
# print(status(r2))
#------------------------------------------------------------
class Robot:
    """A mobile robot with a battery ."""
    def _init_(self,name,battery=100):
        self.name=name
        self.battery=battery

    def drain(self,amount):
        self.battery=max(0,self.battery-amount)

    def status(self):
        return f"{self.name}:{self.battery}%"

r1=Robot("Alpha")
r2=Robot("Beta",60)
r1.drain(35)
print(r1.status())
print(r2.status())
#-------------------------------------------------------------------------------
# class Robot:
#     def _init_(self,name,battery=100):
#         self.name=name
#         self.battery=battery

#     def drain(self,amount):
#         self.battery=max(0,self.battery-amount)

#     def status(self):
#         return f"{self.name}:{self.battery}%"

# fleet=[Robot("Alpha",100),Robot("Beta",60),Robot("Gamma",30)]
# for r in fleet:
#         r.drain(20)

# for r in fleet:
#         print(r.status())

# print("objects created:",len(fleet))
#-------------------------------------------------------------
# create a class with name student which has two instances attributes name and srn and a display() method nthen cfreate 3 objects and print al, three

# class student:
#     def _init_(self,name,srn):
#         self.name=name
#         self.srn=srn   
#     def display(self):
#         print(f"Name: {self.name}, SRN: {self.srn}") 

# std1=student("john","R25EV007")
# std2=student("lingraj","R25EV060")
# std3=student("vasanth","R25EV040")

# std1.display()
# std2.display()
# std3.display()
#-----------------------------------------------------------------------
# class Robot:
#      def _init_(self, name):  #self is the linkage b/w classes and objrcts 
#          self.name = name

#      def status(self):
#          return f"{self.name}:ready"

# r=Robot("Alpha")
# print(r.status())    #the normal way
# print(Robot.status(r))   # exactlywhat python does underneath
# #if self is not used it shows attribute error because python does not know which object to use
# #---------------------------------------------------------------------------------------------------------
# class Robot:
#         def _init_(self, name,battery=100,speed=0.5):
#             self.name = name
#             self.battery = battery
#             self.speed = speed

        
#         def status(self):
#             return f"{self.name}:{self.battery}% at {self.speed} "
# print(Robot("alpha").status())
# print(Robot("beta", 60).status())
# print(Robot("gamma", 25, 1.2).status())

# #----------------------------------------------------------------------------
# class Robot:
#      wheels=4
#      fleet_size=0
#      def _init_(self, name):
#             self.name = name
#             Robot.fleet_size += 1   
# a=Robot("alpha")
# b=Robot("beta")
# print("names:",a.name,b.name)
# print("wheels :",a.wheels,b.wheels)
# print("fleet size:",Robot.fleet_size)
# Robot.wheels=6
# print("after change :",a.wheels,b.wheels)

#------------------------------------------------------------
class Robot:
      log=[]
      def _init_(self, name):
         self.name = name
        self.log =[]

      def record(self,event):
       self.log.append(event)

 a=Robot("Alpha")
 b=Robot("Beta")
 a.record("Alpha started")
 b.record("Beta started")
 print("Alpha Log:", a.log)
 print("Beta log:",b.log)
     