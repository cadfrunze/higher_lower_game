class User:

    def __int__(self):
        print("Userul a fost creeat")


user_1 = User()
user_1.id = "Bun"
user_1.username = "maryus"
user_1.password = "manci_pula"
user_1.boolean = True

user_2 = User()
user_2.id = "Bun"
user_2.username = "frodo"
user_2.boolean = False
print(user_1.username)
print(user_2.username)