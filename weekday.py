# weekday.py
# Author: Kealan McGuinness
# Write a program that outputs whether or not today is a weekday.


# I tried to use the same logic as used in the week05 task where we created a tuple to help identify the summer months. 
# I first tried to use the numbering method used in the week 05 task .ie weekdays = days(1:5) - but it kept failing when mirroring the method in the lab.
# So I defined the weekdays and the weekend days in a list of days.
# I created a list for both uppercase and lowercase in case the respondent entered response in lower case. 


day = input ("What day is it?: ") 

weekdays = ("Monday", 
            "monday", 
            "Tuesday", 
            'tuesday', 
            'wednesday', 
            "Wednesday", 
            'thursday' 
            "Thursday", 
            'friday', 
            "Friday"
)

weekend = ("Saturday", 'saturday', "sunday" , "Sunday")

if day in weekdays:
    print ("Yes, unfortunately today is a weekday!")
if day in weekend:
    print ("It is the weekend, yay!")


   
