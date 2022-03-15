#key-value pairs
monthConversions = { 
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
#all of the keys have to be unique otherwise we will get error
print("**********************************Refering to particular key to see its pair****************************")
print(monthConversions["Nov"])
#
#
print("**********************************Refering to particular key to see its pair****************************")
print(monthConversions.get("Aug"))#in .get function we can specify value
print(monthConversions.get("Pen","Not a valid key"))# if not specified, we receive "None"