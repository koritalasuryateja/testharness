# Project 1: Test Harness


## Personal Information
- Name: Koritala Surya Teja 
- Stevens Login: skorital1@stevens.edu

## Repository URL
(https://github.com/koritalasuryateja/testharness)

## Time Spent
I spent almost 18 hours on this project.

## Testing Approach
I have implemented a test harness in test.py that automates the testing process. This harness reads .in input files and compares the program's output to the expected .out files. Tests were written to cover a range of scenarios, including edge cases for error handling and standard usage.

## Known Bugs/Issues
No issues , the utility functions are currently running as expected.

## Difficult Issues and Resolutions
Error in test.py: The testing script (test.py) was encountering an error when running the wc.py script. This was addressed by modifying the run_test function to explicitly use the python interpreter to execute the script.

Error Handling in compare_json.py: The compare_json.py script was not exiting with a non-zero status in case of a JSONDecodeError. This was fixed by adding sys.exit(2) in the exception block to indicate an error.

## Implemented Extensions
- Command-Line Flags for wc.py: This utility supports flags to selectively count lines, words, or characters.

example comand:

```
$ ./your_script.py -l file.txt  # Count lines only
$ ./your_script.py -lw file.txt  # Count lines and words
```
- To support multiple files for wc.py: this utility lets you specify multiple files, where it will print a total
  
 example command:
```
$ ./your_script.py file1.txt file2.txt
```
- By default, gron uses json as the name of the base object. Add a flag --obj that takes an argument specifying a different base object
  
example:
```
$ ./your_script.py --obj o eg.json
o = {};
o.menu = {};
o.menu.id = "file"
o.menu.value = "File"
o.menu.popup = {};
o.menu.popup.menuitem = [];
o.menu.popup.menuitem[0] = {};
o.menu.popup.menuitem[0].value = "New"
o.menu.popup.menuitem[0].onclick = "CreateNewDoc()"
o.menu.popup.menuitem[1] = {};
o.menu.popup.menuitem[1].value = "Open"
o.menu.popup.menuitem[1].onclick = "OpenDoc()"
o.menu.popup.menuitem[2] = {};
o.menu.popup.menuitem[2].value = "Close"
o.menu.popup.menuitem[2].onclick = "CloseDoc()"
```

## program3: json_diff
utility script for comparing two JSON files

example:
```
file1.json:
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```
```
file2.json:
{
  "name": "Jane",
  "age": 25,
  "city": "San Francisco"
}
```
```
./json_diff.py file1.json file2.json
```

output:
```
@@ -1,7 +1,7 @@
 {

+"name": "Jane",
+"age": 25,
+"city": "San Francisco"
-"name": "John",
-"age": 30,
-"city": "New York"
 }

```
