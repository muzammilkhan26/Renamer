# Bulk File Renamer

This is a Python program that allows bulk renaming of files in a specified folder based on mappings provided in an Excel file. It uses Tkinter for the graphical user interface (GUI) and Pandas for handling Excel files.

## How to Use

1. **Clone the Repository**:
`git clone 'https://github.com/muzammilkhan26/Renamer.git'`


2. **Install Required Libraries**:
Make sure you have Python installed. Then, install the required libraries using pip:
`pip install -r requirements.txt`

3. **Run the Program**:
Run the `main.pyw` script using Python:

4. **GUI Interface**:
- Click on the "Browse" button next to "Excel File Path" to select your Excel file containing the old and new filenames.
- Click on the "Browse" button next to "Folder Path" to select the folder where the files to be renamed are located.
- After selecting the paths, click on "Rename Files" to initiate the renaming process.

5. **Log Output**:
The log section will display the progress and any errors encountered during the renaming process.

## File Structure

- `main.pyw`: The main Python script containing the file renaming logic.
- `README.md`: This file explaining the usage and setup instructions.
- Other files: Any additional files or folders created during execution (e.g., log files).

## Notes

- Ensure that your Excel file has the columns "OldName" and "NewName" specifying the old and new filenames, respectively.
- Only Excel files with the extension `.xlsx` are supported.
