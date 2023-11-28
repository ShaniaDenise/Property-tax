#Vairables
property_value = 0.0
#Constants
property_tax_rate = 0.0072
assess_value_rate = 0.6
#user input
property_value = float(input("Enter the actual value of the property here: "))
#Calc
assess_value = property_value * assess_value_rate
property_tax = property_tax_rate * assess_value
#output
print("The property tax would be", "${:.2f}".format(property_tax))
print("The assessment value would be", "${:.2f}".format(assess_value))