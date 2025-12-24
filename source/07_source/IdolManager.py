import re
from Idol import Idol
from IdolAbstract import IdolAbstract
from IdolGenerator import IdolGenerator


class IdolManager(IdolAbstract):
    def __init__(self):
        self.idols = [
            #  self, code, name, age, skill, store=False, follower=0, note="", year=0
            Idol("I001", "Alice", 12, "tiktoker", False, 5000),
            Idol("I002", "Bob", 22, "music", True, 8000),
            Idol("I003", "Charlie", 19, "mukbang", False, 3000),
            Idol("I004", "Diana", 25, "tiktoker", True, 12000),
            Idol("I005", "Eve", 21, "music", False, 7000),
        ]

    def view_all(self):
        for idol in self.idols:
            print(idol)

    def input_code(self, isRequired=True, checkExist=True):
        # r => raw string
        pattern = re.compile(r"^I[0-9]{3}$")
        while 1:
            code = input("Nhập mã (IXXX): ")

            if not isRequired and len(code) == 0:
                return None

            if not pattern.match(code):
                print("Mã idol không hợp lệ. Phải có ở dạng IXXX. VD: I001\n")
            elif checkExist and self.findIdolByCode(code):
                print("Mã số idol đã tồn tại từ trước!")
            else:
                return code

    def findIdolByCode(self, code):
        for idol in self.idols:
            if idol.code == code:
                return idol
        return None

    def input_name(self, isRequired=True):
        while True:
            name = input("Enter the name: ").strip()
            if not isRequired and len(name) == 0:
                return None

            if 2 <= len(name) <= 10:
                return name
            print("Name must be between 2 and 10 characters.\n")

    def input_age(self, isRequired=True):
        while True:
            age = input("Enter the age: ")
            if not isRequired and len(age) == 0:
                return 0
            age = int(age)
            if 14 <= age <= 30:
                return age
            else:
                print("Age must be between 14 and 30.\n")

    def input_follower(self, isRequired=True):
        while True:
            follower = input("Enter the follower count: ")
            if not isRequired and len(follower) == 0:
                return 0
            follower = int(follower)
            if 0 <= follower:
                return follower
            else:
                print("Follower count must be a non-negative integer.\n")

    def input_year(self, isRequired=True):
        while True:
            year = input("Enter the year: ")
            if not isRequired and len(year) == 0:
                return 0
            year = int(year)
            if 10 <= year:
                return year
            else:
                print("Year must be at least 10.\n")

    def input_skill(self, isRequired=True):
        while True:
            skill = input("Enter the skill: ").strip()
            if not isRequired and len(skill) == 0:
                return None

            if skill in ["tiktoker", "music", "mukbang"]:
                return skill
            print("Skill must be one of the following: Tiktoker, Music, Mukbang.\n")

    def create_idol(self):
        code = self.input_code()
        name = self.input_name()
        age = self.input_age()
        skill = self.input_skill()
        follower = self.input_follower()

        #  self, code, name, age, skill, store=False, follower=0, note="", year=0
        newStudent = Idol(code, name, age, skill, False, follower, "", 0)
        self.idols.append(newStudent)
        print("Created new idol succeed")

    def store_idol_by_code(self):
        code = input("Enter the idol code to store: ").strip()
        idol = self.findIdolByCode(code)
        if idol:
            # >= 18 tuôi
            if idol.age < 18:
                print(
                    f"Idol with code {code} is under 18 years old and cannot be stored."
                )

            elif not idol.store:
                idol.store = True
                idol.year = self.input_year()
                idol.note = input("Enter note: ").strip()
                print(f"Idol with code {code} has been stored.")
            else:
                print(f"Idol with code {code} is already stored.")
        else:
            print(f"No idol found with code {code}.")

    def update_idol(self):
        code = input("Enter the idol code to update: ").strip()
        idol = self.findIdolByCode(code)
        if idol:
            print("Enter new details (leave blank to keep current value):")
            name = self.input_name(isRequired=False)
            age = self.input_age(isRequired=False)
            skill = self.input_skill(isRequired=False)
            follower = self.input_follower(isRequired=False)

            if name:
                idol.name = name
            if age:
                idol.age = int(age)
            if skill:
                idol.skill = skill
            if follower:
                idol.follower = int(follower)

            print(f"Update successfully.")
        else:
            print(f"No idol found with code {code}.")

    def delete_idol(self):
        code = input("Enter the idol code to delete: ").strip()
        idol = self.findIdolByCode(code)
        if idol:
            self.idols.remove(idol)
            print(f"Idol with code {code} has been deleted.")
        else:
            print(f"No idol found with code {code}.")

    # Hiểm thị các idol store = False
    def show_available_idols(self):
        available_idols = []
        for idol in self.idols:
            if not idol.store:
                available_idols.append(idol)
        if available_idols:
            for idol in IdolGenerator(available_idols):
                print(idol)
        else:
            print("No available idols found.")

    def sort_available_idols_by_follower(self, ascending=True):
        available_idols = []
        for idol in self.idols:
            if not idol.store:
                available_idols.append(idol)

        available_idols.sort(key=lambda x: x.follower, reverse=not ascending)
        for idol in available_idols:
            print(idol)
