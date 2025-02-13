months = {
    "01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", 
    "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"
}

date_input = input("Enter the date (mm/dd/yyyy): ")
mm, dd, yyyy = date_input.split('/')

if mm in months:
    month = months[mm]
else:
    month = "Invalid month entered"

print("Date Output:", month, int(dd), ",", yyyy)