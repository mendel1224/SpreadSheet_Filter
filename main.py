

import csv
from config import purchasesFile, salesFile, currentInventory

idTracker = {}

# open sales file and save item ID to dictionary
with open(salesFile, 'r') as sales:
    salesReader = csv.reader(sales)
    for row in salesReader:
        idTracker[row[0]] = 1

# open purchase file and check if item ID is in sales file
with open(purchasesFile, 'r') as purchases, open(currentInventory, 'w', newline='') as inventory:
    purchaseReader = csv.reader(purchases)
    inventoryWriter = csv.writer(inventory)

    for row in purchaseReader:
        if row[0] not in idTracker:
            inventoryWriter.writerow(row)


