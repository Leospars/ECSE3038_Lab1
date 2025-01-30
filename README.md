# lab

## Aim

To become more familiar with Git, GitHub and Python and the development environment.

## Requirements

Students should create a repository on GitHub and push code to this repository. Students should also make changes to the code on their local machine and commit these changes to the repository.

The code that the students are expected to write will not be specific to a particular topic. 

## Outline

In the Python programming language, you are expected to design and implement a simple script that performs actions as defined be the requirements below. These actions or functions must be added to your code one after the other separated by a commit to the repository hosted on GitHub. 

Addition of any further functionality is up to you but the following functions must be included:

1. Write a function, `parallel()`, that, when called, prints the effective resistance of a network of resistors connected in parallel. The function should be able to accept a single **list** as argument.
    
    Use the example provided below to test the functionality of your function. ie, copy the line below into your python script to call the function you wrote. 
    
    ```python
    parallel([330, 1000, 2200])
    ```
    
    Your script should print the following:
    
    ```python
    "222.973 ohms"
    ```
    

(5 marks)

1. Write a function, `potential_divider()`, that takes **two values** as argument: a number that represents a voltage supply value, and a **list** of numbers that represent resistance values of resistors connected in series. The function should output the voltage drop across each resistor in your resistor list. The function should be able to accept a **list** of any length.
    
    
    ![circuit.png](circuit.png)
    
    eg. 
    
    ```python
    > potential_divider(9, [3000, 1000])
    > "6.75v"
    > "2.25v"
    ```
    
    (5 marks)
    
2. Write a function, `temperature_check()`, that accepts a single number, a patient's body temperature, and a single character, the unit of temperature. The function should output whether the patient is hypothermic, hyperthermic or has normal body temperature based on the number passed to the function. 
    
    The second value passed as argument should tell the function whether the condition should calculated in degrees celcius or degrees fahrenheit.
    
    An appropriate message should be written to the screen with the result. You’re free to use what ever reasonable temperature limits you feel will adequately act as boundaries for these conditions.
    
    eg. 
    
    ```python
    > temperature_check(14, "C")
    > "the patient is hypothermic"
    
    > temperature_check(37, "C")
    > "the patient's temperature is normal"
    
    > temperature_check(37, "F")
    > "the patient is hypothermic"
    ```
    
    (5 marks)
    

## Important

All three functions must be written in one `app.py` file.

The inclusion of a a file called `README.md` is mandatory. Your README.md should be located in the root of your repository.  

Therefore, your repo must contain only two files, a single `app.py` and a `README.md`.

The README should contain: 

- A summary of the expected behaviour of each function included in your code.
- The reason the code was written (eg. for the purpose of an assignment, etc).
- A short joke.

The `README.md` should be properly formatted with the markdown syntax.

(5 marks)

## Note

There is no maximum number of commits that can be made the to repo. There should, however, be at least 3 commits since each function after the first should be implemented and committed one at a time. 

Each commit should be accompanied by a short and meaningful commit message that outlines what changes were made.

## Submission

Due date is Friday, January 31, 2025 at 11:59PM.

The repo name must be "ECSE3038_lab1".

You're only required to provide a link to your GitHub repository. 

Any commits made to the repo after the due date will not be considered.

If you prefer to make your repo private, remember to add me as a collaborator. My github username is irpl.