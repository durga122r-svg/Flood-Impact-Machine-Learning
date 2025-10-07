# Construction Site Material Management System (Pure Python Project)

import csv
import os

FILE_NAME = 'materials.csv'

# Ensure file exists
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Material_ID', 'Material_Name', 'Quantity', 'Unit_Cost', 'Total_Cost'])

# Add new material
def add_material():
    material_id = input('Enter Material ID: ')
    name = input('Enter Material Name: ')
    quantity = float(input('Enter Quantity: '))
    unit_cost = float(input('Enter Unit Cost: '))
    total_cost = quantity * unit_cost

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([material_id, name, quantity, unit_cost, total_cost])
    print(f"\n✅ Material '{name}' added successfully!\n")

# View all materials
def view_materials():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        materials = list(reader)
        for row in materials:
            print('\t'.join(row))
    print('\n')

# Update material quantity or cost
def update_material():
    material_id = input('Enter Material ID to update: ')
    updated = False

    with open(FILE_NAME, 'r') as file:
        reader = list(csv.reader(file))

    for row in reader:
        if row[0] == material_id:
            print(f"Current Data: {row}")
            quantity = float(input('Enter new Quantity: '))
            unit_cost = float(input('Enter new Unit Cost: '))
            row[2] = quantity
            row[3] = unit_cost
            row[4] = quantity * unit_cost
            updated = True
            break

    if updated:
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)
        print('\n✅ Material updated successfully!\n')
    else:
        print('\n❌ Material ID not found!\n')

# Delete a material
def delete_material():
    material_id = input('Enter Material ID to delete: ')
    deleted = False

    with open(FILE_NAME, 'r') as file:
        reader = list(csv.reader(file))

    header = reader[0]
    data = [row for row in reader if row[0] != material_id]

    if len(data) < len(reader):
        deleted = True

    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    if deleted:
        print('\n✅ Material deleted successfully!\n')
    else:
        print('\n❌ Material ID not found!\n')

# Generate report
def generate_report():
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        total_materials = 0
        total_value = 0
        for row in reader:
            total_materials += 1
            total_value += float(row['Total_Cost'])

    print(f"\n📦 Total Materials: {total_materials}")
    print(f"💰 Total Value of Inventory: ₹{total_value:.2f}\n")

# Main menu
def main():
    init_file()

    while True:
        print('--- Construction Site Material Management ---')
        print('1. Add New Material')
        print('2. View All Materials')
        print('3. Update Material')
        print('4. Delete Material')
        print('5. Generate Report')
        print('6. Exit')

        choice = input('Enter your choice (1-6): ')

        if choice == '1':
            add_material()
        elif choice == '2':
            view_materials()
        elif choice == '3':
            update_material()
        elif choice == '4':
            delete_material()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            print('\nExiting system... Goodbye! 👷‍♂️')
            break
        else:
            print('\n❌ Invalid choice! Please enter a number between 1 and 6.\n')

if __name__ == '__main__':
    main()
