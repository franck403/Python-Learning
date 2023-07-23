# 1-Variables

### Naming a variable

- Variable names must begin with a letter or an underscore (_).
- They may not contain special characters or spaces.
- Underscores (_) are generally used to separate words in variable names.

### Standard types

In Python, variables can be of different types:

- Integer ``(int)``
- Floating number ``(float)``
- Character string ``(str)``
- Boolean ``(bool)``
- Other types such as ``lists``, ``dictionaries``, ``tuples``, etc.

### Some examples of variables and their types:

```python
agePerson = 14 # agePerson is of type int
nomJoueur = "MrBeast" # nomJoueur is of type str
continue_party = True # continue_party is of type bool
```

### Useful functions

- ``print()``: To display information on the screen.
- ``input()``: To read data entered on the keyboard by the user.
- ``type()``: To find out the type of a data item or variable.
- ``int()``,``str()``, ``float()``, ``bool()``: Convert data from one type to another.
- ``str.format()``: To format a string by inserting dynamic values.

##### Example of function usage :

```python
text = "The person's age is {} and his name is {}."
print(text.format(agePerson, namePlayer))
```

##### You can also use ``f-strings`` for formatting:

```python
text = f"The person's age is {agePerson} and his name is {playerName}.
```

## Result

```
<class 'int'>
<class 'str'>
L'âge de la personne est 14 et son nom est MrBeast.
Choisir un pseudo : Iwaki
Salut Iwaki
Entrez un prix HT : 25
Prix TTC = 30.0
1
```
