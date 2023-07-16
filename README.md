# CPF Generator-and-Validator

This is a Python program that allows you to generate random CPFs and validate them, it is also possible to manage these CPFs by saving them in a JSON file.

The program has three main features:

1. CPF Generator: Allows the user to generate valid random CPFs.
After generating a CPF, you can save it to a list for later use or discard it. The program allows you to generate multiple CPFs and, when finished, all saved CPFs can be stored in a JSON file.

2. CPF Validator: Allows the user to validate a JSON file of CPFs or manually insert one or more CPFs for validation. 3secs on the valid and invalid CPFs screen, the user will return to the validation menu.

3. CPF Manager: allows the user to manually save CPFs in a JSON file, search CPFs in existing files and view saved CPFs. The user can choose from the following options:

* Save CPFs manually: The user can manually enter the CPFs he wants to save and provide a name for the file where they will be stored.
* Search a CPF file: User can select an existing file and view all CPFs saved in it.
* Exit Manager: Closes the CPFs management program.

## Requirements

Python 3.11.x

## How to use
1 Download or clone the program repository.

2 Make sure you have Python 3.11.x installed on your system.

3 Run the main.py file using the following command:

       python main.py

4 Follow the instructions provided by the program to generate and manage passwords.

## Files

* main.py: Contains the main function of the program, where the user can choose between the CPF Generator, CPF Validator and CPF Manager.
* algorithm_generator.py: Contains logic to generate valid CPFs.
*algorithm_validator.py: Contains logic to validate the inserted CPFs and return whether it is valid or invalid.
* manager.py: Contains functions to save, search and read CPFs in JSON files.

## Contribution
Contributions are welcome! If you encounter an issue, have a suggestion, or want to improve the code, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.
