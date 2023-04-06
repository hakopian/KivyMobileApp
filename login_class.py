import main

class project(main.App):
    def build(self):
        screen = main.Builder.load_file('project.kv')
        return screen
    def stop(self):
        self.root.ids.video.play = False
        self.root.ids.video1.play = False
        self.root.ids.video2.play = False
        self.root.ids.video3.play = False
        self.root.ids.video4.play = False

        self.root.ids.video.opacity = 0
        self.root.ids.video1.opacity = 0
        self.root.ids.video2.opacity = 0
        self.root.ids.video3.opacity = 0
        self.root.ids.video4.opacity = 0
    def playSnatch(self):
        self.root.ids.video.opacity = 1
        self.root.ids.video.play = True
    def playClean(self):
        self.root.ids.video1.opacity = 1
        self.root.ids.video1.play = True
    def playDeadLift(self):
        self.root.ids.video2.opacity = 1
        self.root.ids.video2.play = True
    def playBackSquat(self):
        self.root.ids.video3.opacity = 1
        self.root.ids.video3.play = True
    def playFrontSquat(self):
        self.root.ids.video4.opacity = 1
        self.root.ids.video4.play = True
    def checker(self):

        accounts = open('test_data.txt','r')

        if self.root.ids.user_n.text in accounts:
            if accounts[self.root.ids.user_n.text]["Pass"] == self.root.ids.pass_w.text:
                self.root.current = "workout-selection"
            else:
                self.root.ids.result.text = f'Username does not exist, please Sign Up'
        else:
            self.root.ids.result.text = f'Username does not exist, please Sign Up'
    def create(self):
        with open('users.json') as fp:
            accounts = main.json.load(fp)

            if self.root.ids.username.text not in accounts:
                accounts[self.root.ids.username.text] = {}
                accounts[self.root.ids.username.text]['Pass'] = self.root.ids.password.text
                accounts[self.root.ids.username.text]['Age'] = self.root.ids.age.text
                accounts[self.root.ids.username.text]['Gender'] = self.root.ids.Gender.text
                accounts[self.root.ids.username.text]['Email'] = self.root.ids.Email.text
                accounts[self.root.ids.username.text]['Phone'] = self.root.ids.Phone.text

        with open('users.json', 'w') as fp:
            main.json.dump(accounts, fp)
