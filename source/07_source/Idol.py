class Idol:
    def __init__(
        self, code, name, age, skill, store=False, follower=0, note="", year=0
    ):
        self.code = code
        self.name = name
        self.age = age
        self.skill = skill
        self.store = store
        self.follower = follower
        self.note = note
        self.year = year

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
    def store(self):
        return self._store

    @property
    def follower(self):
        return self._follower

    @property
    def note(self):
        return self._note

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

    @store.setter
    def store(self, value):
        self._store = value

    @follower.setter
    def follower(self, value):
        self._follower = value

    @note.setter
    def note(self, value):
        self._note = value

    @year.setter
    def year(self, value):
        self._year = value

    def __str__(self):
        return f"Code={self.code}, name={self.name}, age={self.age}, skill={self.skill}, store={self.store}, follower={self.follower}, note={self.note}, year={self.year}"
