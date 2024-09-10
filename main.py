import time 
from tqdm import tqdm

#Creating todolist for mistake
class mistakes:
    def __init__(self):
        self.mistakes = []
    def add_mistake(self, mistake):
        self.mistakes.append(mistake)
        with open("mistakes.txt", "a") as f:
                f.write(f"{mistake} at {time.ctime()}\n")

if __name__ == "__main__":
    for i in tqdm(range(100), desc="Loading...", ascii=False, ncols=75):
        time.sleep(0.01)
    print("Welcome to Mistake Tracker")
    mistakes = mistakes()
    while True:
        your_mistake = input("Enter your mistake: ")
        if(your_mistake == "exit"):
            break
        mistakes.add_mistake(f"mistake : {your_mistake}")
    
