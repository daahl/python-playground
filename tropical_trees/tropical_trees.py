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

###### Script config ######
STARTINGROW = 5        # Which row to start reading from
SHEETNAME = 'Sheet1'   # Which sheet to read data from
ROWSKIP = 12           # How many rows to skip, as each tree has several measurements
LABELCOL = 15           # Column 'O', Label
HEIGHTCOL = 27          # Column 'AA', Hfill
DEADCOL = 42            # Column 'AP', Dead. Coincidence that his column is the answer to everything?

datawb = op.load_workbook(filename="C:\\Users\\Marcus\\Documents\\data.xlsx", read_only=True)
outputwb = None


###### Tree object ######
class tree:
    def __init__(self, label) -> None:
        # Required: Each tree has a unique label and id.
        # Plot id reoccurs between sites.
        # Three different sites, with 18 different plots, and 100 trees ("positions") in each plot.
        # Site id is S, R, or M
        # Plot id is K-M, 1-3.
        # Pos id is A-J, 1-10.
        # Assume that new trees are alive on init.
        # Assume 8 neighbours, even for corner and edge positions.
        self.label = label
        self.id = label[0:7]
        self.site = label[0]
        self.plot = label[2:4]
        self.pos = label[4:7]
        self.species = label[8:]
        self.height = None
        self.dead = 0
        self.neighbours = [None] * 8


###### Main script ######
sheet = datawb[SHEETNAME]
row_index = STARTINGROW
trees = {} # Dict to keep track of all the trees that have been extracted

# Iterate the individual trees and extract the data until no data rows remain
while True:
    # Start parsing the label into site, plot, and species
    tree_label = sheet.cell(row=row_index, column=LABELCOL).value
    # No more rows with data, stop extraction.
    if tree_label == None:
        break

    # Add new trees to the dict
    current_tree = tree(tree_label)
    tree_hash = hash(current_tree)
    if tree_hash not in trees:
        trees[tree_hash] = current_tree

    # Check the death status from the last measurement before the next individual
    # because some trees recover from death.
    if sheet.cell(row=row_index+11, column=DEADCOL).value:
        trees[tree_hash].dead = 1

    # Check the latest height measurement.
    # If the tree is dead check the search has to go back up the rows
    # until a measurement is found.
    height_row = 11
    trees[tree_hash].height = sheet.cell(row=row_index+height_row, column=HEIGHTCOL).value
    while trees[tree_hash].height == None:
        height_row = height_row - 1
        trees[tree_hash].height = sheet.cell(row=row_index+height_row, column=HEIGHTCOL).value
    
    # Add this tree to trees that are its neighbour.
    # Plots:
    #   K1 L1 M1
    #   K2 L2 M2
    #   K3 L3 M3
    # Positions:
    #   A1 B1 C1 ... J1
    #   ...
    #   A10 B10 C10 ... J10
    # Neighbours in plots are looked at clockwise, starting with the top left one
    #   0 1 2
    #   3 x 4
    #   5 6 7
    # Case: Individual in center => 8 neighbours
    # Case: Individual at edge => 5 neighbours
    # Case: Individual in corner => only 3 neighbours
    # Neighbours exits between plots, but not between sites.

    neighbours = [None] * 8
    neighbours_id = [None] * 8
    plot_chars = ["K", "L", "M"]
    pos_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    # General case, all neighbours exists.
    # TODO: ides now is to look for edge cases using the char arrays
    #       and to compute the neighbour ids from the current tree plot and pos id
    #       after that use the neighbour array to add this tree to the neighbouring trees self.neigbours
    #       and the neighbour trees to this trees neighbour array.
    
    print(f"{trees[tree_hash].site} {trees[tree_hash].plot} {trees[tree_hash].species} {trees[tree_hash].dead} {trees[tree_hash].height}")
    row_index += ROWSKIP