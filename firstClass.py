


class Temp:

    f = 0
    c = 0

    def __init__(self, given_f, given_c):
        self.f = given_f
        self.c = given_c

    def convertC(self, c_temp):
        self.c = (c_temp - 32) * 5/9

    def convertF(self, f_temp):
        self.f = (f_temp * 9/5) + 32

    def getTemp(self):
        print(f'Fahrenheit: {self.f}')
        print(f'Celsius: {self.c}')



today = Temp(58, 12)

tomorrow = Temp(60, 14)

print("Today") 
today.getTemp()
print("Tomorrow")
tomorrow.getTemp()