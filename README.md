PROJECT TITLE-REAL ESTATE CRUD MANAGER 

The Real Estate CRUD Manager is a Python-based console application built to manage and organize real estate property records in a simple and efficient way.
CRUD stands for Create, Read, Update, and Delete, which are the four basic operations required for managing data in any system. This project simulates a very small real estate management system where the user can store multiple property details and perform various operations through a clean menu-driven interface.
This application allows users to add properties by entering information such as Property ID, Address, Price, and Owner Name.
Once the data is added, the program also provides options to:

View all available properties in a clear list format

Update an existing property by searching it through its Property ID

Delete a property record based on the provided ID


The entire system works in memory using Python lists and dictionaries, making it extremely beginner-friendly.
This project is perfect for learners who want to understand:

How CRUD operations work
How to build menu-driven applications
How to store and manipulate data structures in Python
How small-scale management systems function

Although simple, this project can be expanded further by adding features like saving data to files, using JSON storage, or even converting it into a web application using Flask or Django.
Overall, the Real Estate CRUD Manager provides a solid foundation for learning how real-world data management systems operate.

Features:
1.Add new property details
2.View all stored property records
3.Update a property using its ID
4.Delete a property using its ID
5.Simple menu-driven interface
6.Beginner-friendly Python code

Technologies Used:
1.Python language 
2.Console-based input/output

steps to install the project :
1. Download the Project
You can download the project in two ways:
Option A: Clone from GitHub
If you have Git installed:
git clone https://github.com/your-username/your-repository-name.git

Option B: Download ZIP
1. Open your GitHub repository
2. Click Code (green button)
3. Select Download ZIP
4. Extract the ZIP file to any folder on your computer

2. Install Python (if not already installed)
1. Go to https://www.python.org/downloads
2. Download the latest version
3. Install it with "Add Python to PATH" checked
   
3. Open the Project Folder
Navigate inside the extracted or cloned project folder:
You can open it in VS Code
Or open it in your terminal using:
cd path/to/project

4. Install Dependencies (if any)
If your project uses a requirements file:
pip install -r requirements.txt
If your project doesn't have additional libraries, skip this step.

5. Run the Application
Use the following command:
python main.py
(or whatever your main file name is)
This will launch the CRUD menu interface in the terminal.

6. Start Using the System
You will see a menu like:
1. Add Property
2. View Properties
3. Update Property
4. Delete Property
5. Exit
Just enter the number to perform actions.

7. (Optional) Save Data Between Sessions
If your project uses JSON:
The JSON file will automatically store all property records
No need to set up any database

How to Run:
1. Clone the repository:
git clone https://github.com/aashi-payasi/project-real-crud-manager.git
2. Go to the project folder:
cd your-repository-name
3. Run the Python file:
python real_estate_manager.py

Instructions for testing :
To ensure the Real Estate CRUD Manager works correctly, follow the steps below to test all major functionalities. These tests help verify correctness, reliability, and input validation.

1. Launch the Application
Run the program using:
python main.py
The main menu should appear with the CRUD options.

3. Test “Create Property” Function
1. Choose Option 1: Add Property
2. Enter valid details:
Owner name
Location
Price
Area
Status (Available/Sold/Rented)

4. Verify:
Property ID is generated automatically
Success message is displayed
Property appears in the list when you view all properties
Negative tests:
Enter empty owner name → Should show “Invalid input”
Enter alphabets instead of price → Should show “Enter a numeric value”

3. Test “View Properties”
1. Choose Option 2: View Properties
2. Verify:
All properties appear in a clean table/list
Recently added property is shown correctly
If no properties exist, system should show:
“No properties found.”

4. Test “Update Property”
1. Choose Option 3: Update Property
2. Enter a valid property ID
3. Modify one or more fields (price, owner, status, etc.)
4. Verify:
Only the updated values have changed
Other fields remain the same
Success message is displayed
Negative tests:
Enter a non-existing ID → Should show:
“Property ID not found.”
Enter invalid field values → Should show validation messages

5. Test “Delete Property”
1. Choose Option 4: Delete Property
2. Enter the property ID you want to delete
3. Verify:
Property is removed from the database/list
It does NOT appear when viewing properties
system shows:
“Property deleted successfully.”
Negative tests:
Enter wrong ID → Should display error message

6. Test Input Validation
Try entering:
Alphabets for numeric fields
Blank values
Special characters in name/location
Very large price values
Expected behavior:
The system must prevent invalid entries and show proper warnings.

7. Test Program Stability
1. Add multiple properties
2. Update several fields
3. Delete some properties
4. Keep running different operations
The program should:
NOT crash
Always return to the main menu
Maintain consistent IDs and data

8. Test Exit Option
Select Option 5: Exit
Verify:
Program closes smoothly
No error messages appear

9. (Optional) If using JSON storage
Restart the program
View properties
Check that previously saved properties still exist

This confirms that file handling works correctly.

screenshot of program running in terminal : 
C:\Users\bhoomika payasi\Pictures\Screenshots\Screenshot 2025-11-21 232959.png




License
This project is open-source and free to use for learning purposes
