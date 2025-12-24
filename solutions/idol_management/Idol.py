class Idol:
    def __init__(
        self, code, name, age, skill, is_stored=False, follower=0, reason="", year=0
    ):
        self.code = code
        self.name = name
        self.age = age
        self.skill = skill 
        self.is_stored = is_stored # optional
        self.follower = follower
        self.reason = reason # optional
        self.year =  year # optional
        
    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def skill(self):
        return self._skill

    @property
    def is_stored(self):
        return self._is_stored

    @property
    def follower(self):
        return self._follower

    @property
    def reason(self):
        return self._reason

    @property
    def year(self):
        return self._year

    @code.setter
    def code(self, value):
        self._code = value

    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value

    @skill.setter
    def skill(self, value):
        self._skill = value

    @is_stored.setter
    def is_stored(self, value):
        self._is_stored = value

    @follower.setter
    def follower(self, value):
        self._follower = value

    @reason.setter
    def reason(self, value):
        self._reason = value

    @year.setter
    def year(self, value):
        self._year = value
        
    def __str__(self):
        return f"Code: {self.code}, name: {self.name}, age: {self.age}, skil: {self.skill}, is_stored: {self.is_stored}, follower: {self.follower}, reason: {self.reason}, year: {self.year}"