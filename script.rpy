define l = Character("Lorenzo")
image sprite_main = "manga.png"

label start:
scene background
show sprite_main
l "Hello, How Are You?"

menu :
 "Good":
   jump reply1

 "Bad":
   jump reply2

 "Weird":
   jump reply3

label reply1:
l "Good, My day was so exhausting but good for you"
jump ending

label reply2:
l "Why?"
jump ending

label reply3:
l "How?"
jump ending

label ending:
l "Anyways, It's time for me to say goodbye so goodbye and good day"

return