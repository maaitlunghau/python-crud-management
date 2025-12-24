Idol
	- code: Ixxx
	- name: 2 - 10 characterss
	- age: 14 - 30 years old
	- skill: ["Tiktoker", ,"Music", "Mukbang"]
	- store: True | False (must >= 18)
	- follower,
	- reason,
	- year: >= 10

abstract: IdolAbstract
	- create_idol()
	- delete_idol()
	- find_all()
	- update_idol()

IdolManager: extend IdolAbstract:
	- override methods
	- CRUD functions
	- Nhập kho cho idol theo code (age >= 18)
	- Print &  Idol not yet been stored by follower (Generator)
		submenu: [1: ASC, 2: DESC, 3: Back menu]