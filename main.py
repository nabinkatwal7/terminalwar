from "/class/Character.py" import Character as Character

if __name__ == "__main__":
    luffy = Character("luffy", 100, 10, 10)
    kaido = Character("kaido", 100, 10, 10)
    
    luffy.attack(kaido)
    
    print(luffy)
    print(kaido)