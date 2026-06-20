"""
این جلسه بیشتر مرور جلسات گذشته و مباحث مثل شرط ها، تابع، لیست و دیکشنری بود
از جلسات آینده مقدمات ساخت بازی با Pygame شروع میشود
"""

def momtaz(st1, st2, st3):
    if st1["nomreh"] > st2["nomreh"]:
        if st1["nomreh"] > st3["nomreh"]:
            print ( "Nomreh Ali az hame bishtare")
        elif st3["nomreh"] > st1["nomreh"]:
            print ( "Nomreh Mohammad Reza az hame bishtare" )
        else:
            print ( "Nomreh Mohammad Reza va Ali az hame bishtare")
    elif st2["nomreh"] > st1["nomreh"]:
        if st2["nomreh"] > st3["nomreh"]:
            print ( "Nomreh Hesam az hame bishtare")
        elif st3["nomreh"] > st2["nomreh"]:
            print ( "Nomreh Mohammad Reza as hame bishtare.")
        else:
            print ( "Nomreh Mohammad Reza va Hesam az hame bishtare." )
    else:
        if st1["nomreh"] > st3["nomreh"]:
            print ( "Nomreh Ali va Hesam az hame bishtare" )
        elif st1["nomreh"] < st3["nomreh"]:
            print ( "Nomreh Mohammad Reza az hame bishtare" ) 
        else:
            print ( "Nomreh hame barabar ast" )


student_1 = { "first_name": "Ali", "last_name": "Mohammadi", "age": 10, "school": "Tavakoli", "nomreh": 19 }
student_2 = { "first_name": "Hesam", "last_name": "Ghasab Zadeh", "age": 10, "school": "Nikan", "nomreh": 18 }
student_3 = { "first_name": "Mohammad Reza", "last_name": "Bagheri", "age": 10, "school": "Nikan", "nomreh": 19 }
# student_4 = { "first_name": "Abolfazl", "last_name": "Mirhajian", "age": 22, "school": "nadareh", "nomreh": 20 }

# students = [ student_1, student_2, student_3 ]

momtaz(student_1, student_2, student_3)