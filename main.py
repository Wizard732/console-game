def input_people():
    name = input("Введите свое имя: ")
    age = int(input("Введите свой возраст: "))
    color = input("Введите свой любимый цвет: ")
    question = input("Любишь ли вы игры? (да/нет): ")
    name = name
    age = age
    color = color
    question = question.lower()
    point = 0
    return name, age, color, question, point
name, age, color, question, point = input_people()

class Player:
    def __init__ (self,name, age, color, question, point):
        self.name = name
        self.age = age
        self.color = color
        self.question = question
        self.point = point
    
    def info(self):
        player = {
            "name": self.name,
            "age": self.age,
            "color": self.color,
            "question": self.question,
            "point": self.point
        }
        return player
    
    def answer(self):
        print(f"Привет {self.name}!")
        if (self.age < 18):
            print("Ты еще маленький!")           
        else:
            print("Ты уже взрослый!")

        if (self.color == "синий" or self.color == "красный"):
            print("Оченть смелый цвет!")
        else:
            print("Интересный выбор цвета!")

    def points(self):
        if (self.question == "да"):
            self.point += 1
            print("Отлично! Ты получил 1 балл!")
        else:
            print("Жаль! Ты не получил баллов!")
        if (self.color == "синий" or self.color == "красный"):
                self.point += 1
                print("За выбор любимого цвета ты получил еще 1 балл!")
        else:
                print("К сожалению, ты не получил баллов за цвет.")

        print(f"Всего у тебя {self.point} баллов!")   

player = Player(name, age, color, question, point)
player.answer()
player.points()

favorite_game = input("Какая твоя любимая игра? ")
favorite_genre = input("Какой твой любимый жанр игр? ")

class game_quiz:
    def __init__(self, player):
          self.player = player

    def info_game(self,favorite_game, favorite_genre,):
          favorite_game = favorite_game.lower()
          favorite_genre = favorite_genre.lower()

          if favorite_game == "гта 5":
            self.player.point += 2
            print("Круто! Ты получил 2 балла за любимую игру!")
          else:
            print("Интересный выбор игры!")

          if favorite_genre == "экшен":
            self.player.point += 1
            print("Отличный жанр! Ты получил 1 балл за любимый жанр!")
          else:
            print("Интересный жанр!")

          print(f"У тебя всего {self.player.point} баллов!")


quiz = game_quiz(player)
quiz.info_game(favorite_game, favorite_genre)


