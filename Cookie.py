class Cookie: # like cookie cutter 
    def __init__(self, color):
        self.color = color # creating a data type called Cookie and passing parameter of color

    def get_color(self): # creating a function to tell its color 
        return self.color

    def set_color(self, color): #sets or changes the color of the cookie, its a function 
        self.color = color


#creating our cookies, the cookieone and cookietwo are new variables
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())

# variables in class
class LinkedList:
    def __init__(self, value):
    
    def append(self,value) #attace to the end of the list 
    
    def pop(self): #pop off the end of the list 

    def prepend(self,value): # put it in the beginning

    def insert(self, index, value): #to insert in the middle of the list 

    def remove(self,value): #remove in the list 
        pass