# Birthday List Generator

## Introduction
This Python project aims to simplify the process of managing birthday gift giving by generating a birthday list and storing it in a JSON format. The JSON file includes information about who is giving a gift to whom, along with the Birthday it selfs.

## Features
- **Birthday List Generation**: Automatically generates a birthday list based on user input.
- **JSON Storage**: Saves the generated birthday list in a JSON file.
- **Year Tracking**: Records the year in which the birthday list was created.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:lunoack/BirthdayList.git
   ```
 
3. Navigate to the project directory:
    ```bash
    cd BirthdayList
    ```

## Usage
1. Run the Python script:
python KD_Birthdaylist.py
2. All birthdays are allready entered, the program will generate a birthday list.
4. The generated list will be saved in a JSON file named `KD-Geburtstagsgeschenklist_CURRENTYEAR.json` in the project directory.

## Example
Suppose you want to create a birthday list for your family. After running the script and entering the necessary information, the `birthday_list.json` file might look like this:
```json
{
  "Organisator": "Geburtstagskind",
  "liste": [
    {
      "Paul": "Vonzii 24.01."
    },
    {
      "Vonzii": "MaxM 19.07."
    }
}
```

## Contributing
Contributions are welcome! If you find a bug or have suggestions for improvements, please open an issue or submit a pull request.
