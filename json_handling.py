import json

# JSON FILES
# JSON is also a format which is used to store the data and used by APIs to communicate
# it is similar to Dictionary files

#student = {"name":"Hari","Id":101,"age":24}

#with open("student.json","w") as file:
#    json.dump(student,file,indent=4)
    
    
    
player = [{"id": 1, "name": "Virat Kohli", "sport": "Cricket", "team": "India", "runs": 13000, "age": 35},
{"id": 2, "name": "Lionel Messi", "sport": "Football", "team": "Argentina", "goals": 820, "age": 36},
{"id": 3, "name": "LeBron James", "sport": "Basketball", "team": "Lakers", "points": 39000, "age": 39},
{"id": 4, "name": "Rohit Sharma", "sport": "Cricket", "team": "India", "runs": 10000, "age": 36},
{"id": 5, "name": "Cristiano Ronaldo", "sport": "Football", "team": "Portugal", "goals": 850, "age": 39},
{"id": 6, "name": "Stephen Curry", "sport": "Basketball", "team": "Warriors", "points": 22000, "age": 35},
{"id": 7, "name": "MS Dhoni", "sport": "Cricket", "team": "India", "runs": 10500, "age": 42},
{"id": 8, "name": "Neymar Jr", "sport": "Football", "team": "Brazil", "goals": 450, "age": 32},
{"id": 9, "name": "Kevin Durant", "sport": "Basketball", "team": "Suns", "points": 27000, "age": 35},
{"id": 10, "name": "Hardik Pandya", "sport": "Cricket", "team": "India", "runs": 4000, "age": 31}
]
with open("Player.json","w") as file2: # writing the data into Player.json file
    json.dump(player,file2,indent = 4) # dumping the data 
    
with open("Player.json","r") as file3: #Reading the data using "r" mode
    reader = json.load(file3)          #assaigning the loaded files to reader
    for i in reader:                   #printing every row using for loop
        if i["age"] > 30 : 
            print(i["name"])
            
                      
# print the player details if he plays cricket        
with open("Player.json") as file4:
    reader = json.load(file4)
    for i in reader:
        if i["sport"] == "Cricket":
            print(i)
            
#JSON is better than plain text, beacuse json files gives the clear details about the data
#the data is stored in Key-value pairs, suitable for complex real-world applications.