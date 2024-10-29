# Inventory Filter Program

This Python program filters inventory data from CSV files. It takes two input files: one representing all purchases and another representing all sales. It then generates a third file that contains only the rows from the purchases file that do not appear in the sales file, creating a "current inventory" file.

## Files

- **Input Files**:
  - `purchasesFile`: The CSV file containing all purchase records. The file name can be customized by the user.
  - `salesFile`: The CSV file containing all sales records. The file name can be customized by the user.

- **Output File**:
  - `currentInventory`: The CSV file generated by the program, containing only items from `purchasesFile` that are not found in `salesFile`. The file name for this output can also be customized.

## Configuration

To set your custom file names, create a `config.py` file with the following variables:

```python
# config.py
purchasesFile = "your_purchases_file.csv"  # Replace with your purchases file name
salesFile = "your_sales_file.csv"          # Replace with your sales file name
currentInventory = "your_output_file.csv"   # Replace with your desired output file name
