# Weightlifting Project (Hakop Hakopian)
For the Weightlifting application, a user will be able to log into
and be given examples of workout movements. If the user does not
have an account already made, they will be able to create an account
by signing up. If the user chooses to enroll in one on one coaching
they will be given that option.

## Install required libraries

Ensure that you are in the main directory and run the following

This _must_ be done before you can run the program.

__This is bold__

```shell
$ pip install -r reqiorements.txt

Note: You can also just import those packages in your Python file
```

## To run the program

Click the green run triangle icon in the top-right corner of the PyCharm file.
or right-click on the python file and click run.
```shell
$ python3 main.py
```

#### In the login prompt use the following credentials (optional)

* Username: ``test``
* Password: ``test``

## Functionality

### Create an account

A new account will be added to the customers.json file when users
fill out the sign-up page and clicks sign-up.

### Exit

The applications will exit when the ESC key is clicked or
by clicking window -> close. There is also an Exit button within the 
GUI that will exit the application.

## Data files

### users.json

This contains the users that created an account within the application.

| Name | pass | Age | Gender | Email          | Phone        |
|------|------|-----|--------|----------------|--------------|
| test | test | 26  | Male   | test@gmail.com | 555-555-5555 |


The format of the users.json file

```shell
{"test": {"Pass": "test", "Age": "26", "Gender": "Male", "Email": "test@gmail.com", "Phone": "555-555-5555"}}
```

## Class

### project

#### Methods

    build()
    stop()
    playSnatch()
    playClean()
    playDeadLift()
    playBackSquat()
    playFrontSquat()
    playChecker()
    Create()

## project.kv Variables

    name: public string
    username: public string
    password: public string
    cols: private int
    orientation: private string
    source: private string
    allow_stretch: public boolean
    keep_ratio: public boolean
    id: result
    text: public string
    font_name: private string
    font_size: priavte float
    size_hint: private float
    pos: private int
    id: private string
    multiline: private boolean
    play: private boolean
    opacity: private int

