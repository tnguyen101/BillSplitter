import copy
import os
from datetime import datetime

class Item:
    #Constructor
    def __init__(self, name, total, people):
        self.name = name
        self.total = float(total)
        self.people = people
    #This function returns the people involved
    def getpeople(self):
        return self.people
    #This function rewrites the whole item with the given list ['Name','Price', People...]
    def setitem(self, lst):
        if len(lst > 2):
            self.name = lst[0]
            self.total = float(lst[1])
            self.people = lst[2:]
    #This function prints "{Item}   {total} {person1 person2 ...}"
    def print(self):
        print(f"{self.name}\t{self.total:.2f} {' '.join(self.people)}")   
    #This function returns an array [name, total, person1, perosn 2, ...]
    def get_arr_info(self):
        arr = []
        arr.append(self.name)
        arr.append(self.total)
        for person in self.people:
            arr.append(person)
        return arr


#MAIN CLASS TO IMPORT
class Receipt:
#------------------------------BASIC FUNCTIONS----------------------------------------
    #Constructor: empty list of items
    def __init__(self, name = None, date = None):
        self.name = name
        self.date = date
        self.items = []
        self.filename = None
        self.filetime = None
   
    #This function adds an item to the receipt
    def add(self,item):
        self.items.append(item) 

    #This RETURN function returns the total of the receipt
    def gettotal(self):
        total = 0.0
        for item in self.items:
            total+=item.total
        return total
   
    #This function prints the info the receipt in the terminal
    def printf(self):
        #print Receipt info
        items_formated = self.get_string_output_data()
        print(f'\n{self.name} {self.date.strftime("%m/%d/%Y")} {self.filetime.strftime("%Y_%m_%d_%H_%M_%S")}\n')
        for item in items_formated:
            print(f'{item[0]:^13} {item[1]:^6} {"".join([f"{person:^8}" for person in item[2:]])}')
        people_dict = self.get_summary()
        #print dictionary
        for key,value in people_dict.items():
            print(f'{key} : {value:.2f}')
        #checks total
        total = self.gettotal()
        d_total =0 
        for value in people_dict.values():
            d_total += value
        #done checking total
        #for recheck in case array has fake valeus that causes len to be higher
        if (total == d_total):
            pass
        else:
            print(f'Total amount from receipt: {total:.2f}')
            print(f'Total amount from adding dictionalry {d_total:.2f}\nThe offset is: {total-d_total:.2f}')
#------------------------------DATA OUTPUT----------------------------------------
 
    def get_header_info(self):
        return (self.date, self.name, self.gettotal(), self.filetime)
    
    #This RETURN function returns a dictionary summary of the receipt. The first parameter puts receipt info in the dictionary
    def get_summary(self, header = False):
        items_formated = self.get_string_output_data()
        #cretes a dictionary with person and values
        people_dict = {}
        if header:
            people_dict.update({self.name:self.date.strftime("%Y/%m/%d")})
        for person in items_formated[0][2:]:
            price = 0.0
            for item in self.items:
                for name in item.people:
                    if person == name:
                        price += item.total/len(item.people)
                        price = round(price,2)
            people_dict.update({person: price})
        return people_dict
    
    #This RETURN function returns the data of the object as a 2dlist :[line[item_data[]] where [0][] = R_name, R_date
    def get_obj_data(self):
        needed_names = set()
        for item in self.items:
            people_lst = item.getpeople()
            for person in people_lst:
                    needed_names.add(person)
        header = ["Name", "Price"] 
        for names in needed_names:
            header.append(names)
        #format people in item
        formated_2d = []
        formated_2d.append(header)
        for item in self.items:
            names = item.getpeople()
            name_format = [str(item.name) , float(item.total)]
            for person in names:
                name_format.append(person)    
            formated_2d.append(name_format)
        return copy.deepcopy(formated_2d)          
    
    #This RETURN function returns the receipt data into a 2d output string list : [line[string list[]]
    def get_string_output_data(self):
        data = self.get_obj_data()
        #format people in item
        formated_2d = []
        formated_2d.append(data[0])
        for item in self.items:
            names = item.getpeople()
            name_format = [str(item.name) , str(item.total)]
            for h_name in data[0][2:]:
                found = False
                for name in names:
                     if h_name == name:
                        name_format.append('x')
                        found = True
                        break
                if found==False:
                    name_format.append("-")    
            formated_2d.append(name_format) 
        return formated_2d  
         
    #This function writes the receipt summary
    def write_to_file_summary(self, file_name):
        pass#WRITE TO JSON FILE
                    
    #This function RETURNS the current time when called and saves.
    def get_date_time(self):
        if self.filetime == None:
            self.filetime = datetime.now().replace(microsecond=0)
            self.filename = f'{self.name}-{self.filetime.strftime("%Y_%m_%d_%H_%M_%S")}.txt'
        return self.filetime
    
    def get_file_name(self):
        self.get_date_time()
        return self.filename
#------------------------------DATA INPUT----------------------------------------
    def scan_list_data(self, data):
        name_date = data[1][0].split(':')
        self.name = name_date[0]
        print(name_date[1])
        receipt_date = name_date[1].split('/')
        self.date = datetime(year=int(receipt_date[0]), month=int(receipt_date[1]), day=int(receipt_date[2]))
        #initialize date of creation
        date = data[0][0].split('-')
        date = date[1].split('.')
        date = date[0].split('_')
        date = datetime(year=int(date[0]), month=int(date[1]), day=int(date[2]), hour=int(date[3]), minute=int(date[4]), second=int(date[5]))
        self.filetime = date
        self.filename = f'{self.name}{self.filetime.strftime("%Y_%m_%d_%H_%M_%S")}.txt'
        for line in data[3:]:
            name = line[0]
            amount = float(line[1])
            people = []
            for person in line[2:]:
                people.append(str(person))
            self.add(Item(name,amount,people))

                
    #This function reads data from a txt file in a given location into the object
    def read_from_file(self, file_name):
        raw_data = []
        with open(file_name, 'r') as file:
            for line in file:   
                if line.strip() == "":
                    #the line is empty
                    pass
                else:
                    line = line.strip()
                    line = line.split('\31')
                    raw_data.append(line)
        self.scan_list_data(raw_data)