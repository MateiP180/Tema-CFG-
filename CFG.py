import random

def Representation() :
    non_terminals = ["S"]
    start = "S"
    terminals = ["a", "b"]
    productions = {"S" : ["aSb", "~"]} # "~" = elementul vid

    cfg = {
        "Non_terminals": non_terminals,
        "Terminals": terminals,
        "Start_symbol": start,
        "Productions": productions
    }
    
    return cfg


def stringGenerator():
    strings = []
    
    for _ in range(10): 
        cur_string = "S"

        while "S" in cur_string and len(cur_string) < 10:
            k = cur_string.index("S")
            rand = random.randint(0, 2) # am luat pana la 2 ca sa fie probabilitatea mai mica sa imi dea epsilon repede

            if rand == 0:
                cur_string = cur_string[:k] + cur_string[k+1:]
            else:
                cur_string = cur_string[:k] + "aSb" + cur_string[k+1:]

        cur_string = cur_string.replace("S", "")

        strings.append(cur_string)

    return strings

stack = []

def Member(cfg, target, current_string, depth = 0):
    if depth > 12:
        return False
    if current_string == target:
        return True
    
    for i in range(len(current_string)):
        symbol = current_string[i]
        if symbol in cfg["Non_terminals"]:
            for prod in cfg["Productions"][symbol]:

                if prod == "~":
                    new_string = current_string[:i] + current_string[i+1:]
                else:
                    new_string = current_string[:i] + prod + current_string[i+1:]
                
                
                if Member(cfg, target, new_string, depth + 1):
                    return True
    return False 

def Derive(cfg, target, current_string, depth):
    if depth > 15:
        return None 
    
    if current_string == target:
        for c in current_string:
            if c in cfg["Non_terminals"]:
                return None
        return [current_string]
    
    for i in range(len(current_string)):
        symbol = current_string[i]
        if symbol in cfg["Non_terminals"]: 
            for production in cfg["Productions"][symbol]:
                if production == '~':
                    production = ''
                new_string = current_string[:i] + production + current_string[i+1:]
                result = Derive(cfg, target, new_string, depth + 1)
                if result is not None:
                    return [current_string] + result 

cfg = Representation()
strings = stringGenerator()

target = "ab"
path = Derive(cfg, target, cfg["Start_symbol"], 0)
if path is None:
    print("Eroare")
else:
    n = len(path)
    for i in range(n - 1):
        print(path[i], end= " -> ")
    print(path[-1])

print(Member(cfg, target, cfg["Start_symbol"], 0))

