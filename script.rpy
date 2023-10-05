# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define men = Character('Чел', color="#9e992d")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
image office = "images/office.jpeg"
image fire = "images/fire.png"
image cat = "images/koshara.png"
define cosmo = "audio/cosmoTheme.mp3"
label start:
    play music cosmo
    scene bg room
    
    menu choice:
        "прааво":
            jump right
        "левооо":
            jump left

label right:
    scene office
    show cat
    men "Добро пожаловать в офис"
    return
label left:
    scene fire
    men "Добро пожаловать в ад"
    return