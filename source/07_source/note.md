tạo 1 cái abstract (IdolAbstract), create_idol(), delete_idol(), find_all(), update_idol()

Idol 
(code: Ixxx, name: 2 - 10 kí tự, age: 14 - 30, 
skill: [Tikoker, Music, Mukbang]
store: true/ false (ở tù)
follower
note: lý do ở tù
year: Nhập kho bao lâu (>=10)

IdolManager kế thừa idol abstract
+ Overide method abstract 
+ CRUD
+ Nhập kho cho idol theo code (>= 18), cập nhật lý do (note), year trong khu
+ In ra các idol chưa nhận kho (Generator)
+ Sắp xếp idol chưa nhập kho theo follower (Submenu - 1: ASC, 2: DESC 3: Return menu - sử dụng nhập sai, thì cho nhập đúng)