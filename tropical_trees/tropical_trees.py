#
#   A script that extracts data from a HUGE (60k+ rows, 60+ columns)
#   spreadsheet to help biologists do science.
#   Calculates the average height of the 8 surounding trees around
#   an individual tree, and returns a neat spreadsheet with
#   the individuals label, height, neighbouring average height, 
#   and death status.
#   
#   By Marcus Dahlström 2022
#

import openpyxl as op

datawb = op.load_workbook(filename="C:\\Users\\Marcus\\Documents\\data.xlsx")

###### Script config ######
STARTINGROW = 5        # Which row to start reading from
SHEETNAME = 'Sheet1'   # Which sheet to read data from
ROWSKIP = 12           # How many rows to skip, as each tree has several measurements
LABELCOL = 15           # Column 'O', Label
HEIGHTCOL = 27          # Column 'AA', Hfill
DEADCOL = 42            # Column 'AP', Dead. Coincidence that his column is the answer to everything?

###### Main script ######
sheet = datawb[SHEETNAME]
row_index = STARTINGROW

# Iterate the individual trees and extract the data
while True:
    # Start parsing the label into site, plot, and species
    tree_label = sheet.cell(row=row_index, column=LABELCOL).value
    # No more rows with data, stop extraction.
    if tree_label == None:
        break
    # Three different sites, with 18 different plots, and 100 trees in each plot.
    # Site id is K-M, 0-3.
    # Plot id is A-J, 0-10.
    site_id = tree_label[0]
    plot_id = [tree_label[2:4] , tree_label[4:7]]
    species = tree_label[8:11]
    # Check the death status from the last measurement before the next individual
    # beacause some trees recover from death.
    if sheet.cell(row=row_index+11, column=DEADCOL).value:
        dead = 1
    else:
        dead = 0
    # Check the latest height measurement.
    # If the tree is dead check the search has to go back up the rows
    # until a measurement is found.
    height_row = 11
    height = sheet.cell(row=row_index+height_row, column=HEIGHTCOL).value
    while height == None:
        height_row = height_row - 1
        height = sheet.cell(row=row_index+height_row, column=HEIGHTCOL).value
    # Look at the heights of the neighbouring trees
    

    print(f"{site_id} {plot_id} {species} {dead} {height}")
    row_index += ROWSKIP