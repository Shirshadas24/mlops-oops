class chat:
    __user_id = 1
    def __init__(self):
        self.id=chat.__user_id
        chat.__user_id += 1
        self.__nulli='Default'
        self.name = ''
        self.password = ''
        self.is_logged_in = False
        # self.menu()
    def get_nulli(self):
        return self.__nulli
    def set_nulli(self, value):
        self.__nulli = value
    @staticmethod
    def get_id():
        return chat.__user_id
    @staticmethod
    def set_id(value):
        chat.__user_id = value
    def menu(self):
        user_input=input("Enter your choice\n1. Login\n2. signup\n3. press to post\n4.press to message someone\n5. press to exit\n")
        if user_input == '1':
            self.login()
        elif user_input == '2':
            self.signup()
        elif user_input == '3':
            self.post()
        elif user_input == '4':
            self.message()
        elif user_input == '5':
            exit()
        else:
            print("Invalid choice")
            self.menu()  
    def signup(self):
        email=input("Enter your email")
        pwd=input("Enter your password")
        self.name = email
        self.password = pwd
        print("Successfully signed in\n")
        self.menu()
    def login(self):
        if self.name == '' and self.password == '':
            print("Please signup first\n")
            self.menu()
        else:
            email=input("Enter your email")
            pwd=input("Enter your password")
            if self.name == email and self.password == pwd:
                self.is_logged_in = True
                print("Successfully logged in\n")
                self.menu()
            else:
                print("Invalid credentials\n")
                self.menu()
            print("\n")
            self.menu()
    def post(self):
        if self.is_logged_in:
            post=input("Enter your post: ")
            print("Successfully posted\n")
        else:
            print("Please login first\n")
        self.menu()
    def message(self):
        if self.is_logged_in:
            message=input("Enter your message: ")
            frd=input("Enter your friend name: ")
            print("Successfully messaged\n")
        else:
            print("Please login first\n")
        self.menu()
    def exit(self):
        print("Thank you for using our service\n")
