import re

from IdolAbstract import IdolAbstract
from Idol import Idol
from IdolGenerator import IdolGenerator

class IdolManager(IdolAbstract):
    def __init__(self):
        self.idols = [
            Idol("I001", "Alice", 12, "tiktoker", False, 5000),
            Idol("I002", "Bob", 22, "music", True, 8000),
            Idol("I003", "Charlie", 19, "mukbang", False, 3000),
            Idol("I004", "Diana", 25, "tiktoker", True, 12000),
            Idol("I005", "Eve", 21, "music", False, 7000),
        ]
        
    # validates
    def input_code(self, label="Enter the idol code: ", is_required=True, checkExist=True):
        pattern = re.compile(r"^I\d{3}$")
        
        while True:
            code = input(label)
            
            if not is_required and len(code) == 0:
                return None
            
            if not code.strip():
                print("Idol Code must be required.\n")
            elif not pattern.match(code):
                print("Idol Code must be matched with format: Ixxx.\n")
            elif checkExist and self.find_idol_by_code(code):
                print("Idol Code already existed.\n")
            else:
                return code
            
    def find_idol_by_code(self, code):
        for idol in self.idols:
            if idol.code == code:
                return idol
            
        return None
    
    def input_name(self, is_required=True):
        while True:
            name = input("Enter the idol name: ")
            
            if not is_required and len(name) == 0:
                return None
            
            if not name.strip():
                print("Idol Name must be required.\n")
            elif len(name) < 2 or len(name) > 10:
                print("Length of idol name must be between 2 to 10 characters.\n")
            else:
                return name
    
    def input_age(self, is_required=True):
        while True:
            age = input("Enter the idol age: ")
            
            if not is_required and len(age) == 0:
                return None
            
            if not age.isdigit():
                print("Idol Age must be a integer number.\n")
            elif int(age) < 14 or int(age) > 30:
                print("Idol Age must be between 14 to 30 years old.\n")
            else:
                return int(age)
    
    def input_skill(self, is_required=True):
        while True:
            skill = input("Enter the idol skill ('Tiktoker', 'Music', 'Mukbang'): ")
            
            if not is_required and len(skill) == 0:
                return None
            
            if not skill.strip():
                print("Idol skill must be required.\n")
            elif skill.lower() not in ['tiktoker', 'music', 'mukbang']:
                print("Idol Skill must be in ['Tiktoker', 'Music', 'Mukbang'].\n")
            else:
                return skill.capitalize()
    
    def input_follower(self, is_required=True):
        while True:
            follower = input("Enter the idol follower: ")
            
            if not is_required and len(follower) == 0:
                return None
            
            if not follower.isdigit():
                print("Idol Follower must be a integer number.\n")
            elif int(follower) < 0:
                print("Idol Follower must be greater than 0 follower.\n")
            else:
                return int(follower)
    
    # functions
        def show_all_idols(self):
            pass
    
    def input_year(self, is_required=True):
        while True:
            year = input("Enter the year when store: ")
            if not is_required and len(year) == 0:
                return 0
            year = int(year)
            if 10 <= year:
                return year
            else:
                print("Year must be at least 10.\n")
    
    # functions
    def show_all_idols(self):
        for idol in self.idols:
            print(idol)
    
    def create_idol(self):
        code = self.input_code()
        name = self.input_name()
        age = self.input_age()
        skill = self.input_skill()
        follower = self.input_follower()
        
        new_idol = Idol(code, name, age, skill, False, follower, "", 0)
        self.idols.append(new_idol)
        
        print("✅ Created new idol successfully\n")
    
    def update_idol(self):
        if not self.idols:
            print("Sorry... The idol list is actually empty.\n")
            return
        
        code = self.input_code("Enter the student code to update: ", checkExist=False)
        idol = self.find_idol_by_code(code)
        
        if idol:
            print("Enter the new idol details (leave blank to keep current value: )")

            name = self.input_name(is_required=False)
            age = self.input_age(is_required=False)
            skill = self.input_skill(is_required=False)
            follower = self.input_follower(is_required=False)
            
            if name:
                idol.name = name
            if age:
                idol.age = int(age)
            if skill:
                idol.skill = skill
            if follower:
                idol.follower = int(follower)
                
            print("✅ Updated idol successfully")
            
        else:
            print(f"No idol found with code {code}.\n")
    
    def delete_idol(self):
        if not self.idols:
            print("Sorry... The idol list is actually empty.\n")
            return
        
        code = self.input_code("Enter the student code to delete: ", checkExist=False)
        idol = self.find_idol_by_code(code)
        
        if idol:
            self.idols.remove(idol)
            print("✅ Deleted idol successfully")
            
        else:
            print(f"No idol found with code {code}.\n")    
    
    def show_all_good_idols(self):
        if not self.idols:
            print("Sorry... The idol list is actually empty.\n")
            return
        
        good_idols = []
        
        for idol in self.idols:
            if not idol.is_stored:
                good_idols.append(idol)
            
        if len(good_idols) > 0:
            for idol in IdolGenerator(good_idols):
                print(idol)
        else:
            print("No good idol found...\n")
    
    def store_idol_by_code(self):
        if not self.idols:
            print("Sorry... The idol list is actually empty.\n")
            return
        
        code = self.input_code("Enter the student code to store: ", checkExist=False)
        idol = self.find_idol_by_code(code)
        
        if idol:
            if idol.age < 18:
                print(f"Idol with code {code} is under 18 years old and cannot be stored.\n")
            elif not idol.is_stored:
                idol.is_stored = True
                idol.year = self.input_year()
                idol.reason = input("Enter the reason when store: ").strip()
            else: 
                print(f"Idol with code {code} is already stored.\n")
        else:
            print(f"No idol found with code {code}.\n")
    
    def sort_all_idols_available_by_follower(self, option):
        good_idols_sorted = []
        
        for idol in self.idols:
            if not idol.is_stored:
                good_idols_sorted.append(idol)
                
        good_idols_sorted.sort(key=lambda x: x.follower, reverse=option)
        
        for idol in good_idols_sorted:
            print(idol)