#write a programme to calculate and print the electricity bill of a given customer
def calculate_electricity_bill():
    customer_id=input("Enter the customer's ID: ")
    customer_name=input("Enter the customer's name: ")
    unit_consumed=float(input("Enter unit consumed(in Kw): "))
    cost_per_unit=float(input("Enter the cost of energy(in Naira): "))

    total_amount=unit_consumed*cost_per_unit
    print("Electricity Bill")
    print("Customer ID: ",customer_id)
    print("Customer's Name: ",customer_name)
    print("Units Consumed: ",unit_consumed)
    print("Cost of Energy: ",cost_per_unit)
    print("Total Amount To Pay: ",total_amount)
calculate_electricity_bill()