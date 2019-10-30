# doubleTrouble: A Python Duplicate Finder
This python code uses hashing to discover redundant files in a given directory. 
Depending on the needs of the user, this tool can be used for discovering only or to remove the duplicates.

# Requirements
doubleTrouble requires [click 7.x](https://click.palletsprojects.com/en/7.x/) and Python 3.x to run.
To install click, you can use pip in your shell.
 ```sh
 $ pip install click 
 ```
# Usage
For discovery purposes, run DoubleTrouble in your installation folder and specify a path to a directory where it should look for duplicates.
 ```sh
 $ pyhton3 doubleTrouble EXAMPLEPATH
 ```

To consider sub-directories, use the recursive option.
 ```sh
 $ python3 doubleTrouble -r EXAMPLEPATH
 ```
 
You can get rid of redundant files as well with d for delete.
  ```sh
 $ python3 doubleTrouble -d EXAMPLEPATH
 ```
 
 For more options type --help
 
```sh
 $ python3 doubleTrouble --help
```