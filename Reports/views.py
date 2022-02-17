from django.shortcuts import render, HttpResponse
from login.models import (
    Student_Signup_Form as student, 
    Prof_Signup_Form as prof
)

import pandas as pd

# Create your views here.

def stdReport(request):
    context = { }
    attendance_Dict ={ }
    # attendance_List = []

    # users = User.objects.all()
    loginUser = str(request.user)   #We need to convert it in string also
    # print("User type", type(loginUser))

    # studs = student.objects.get(str(loginUser))
    studs = student.objects.all()

    for s in studs:
        # print(type(s.Roll_Number))
        if s.Roll_Number == loginUser:
            context["Name"] = s.Name
            # print(s.Branch)
            context["Subjects"] = s.Subjects.all()

    ## Populating Attendance Record from CSV file 
    # Subject wise
    std_DB = pd.read_csv('services/AMS/std_DB.csv')

    for subj in context["Subjects"]:
        attend_count = std_DB.loc[std_DB["Rollno"] == loginUser, [str(subj)] ].values
        # print(attend_count[0][0])
        # print(len(attend_count))
        # print(type(attend_count))
        attendance_Dict[subj] = attend_count[0][0]
        # attendance_List.append(attend_count[0][0])

    context["Attendance_Dict"] = attendance_Dict
    # context["Attendance_List"] = attendance_List

    # return HttpResponse('Successfully stored in  the database')
    # subj_Attendance=zip(context["Subjects"], attendance_List)
    return render(request, 'Reports/std_report.html', context)



def profReport(request):
    context = { }

    ## Creating a dictionary to store the subject wise Student and its attendance count
    stud_Attendance_Cnt = { }

    loginUser = str(request.user)
    professors = prof.objects.all()

    for p in professors:
        # print(type(s.Roll_Number))
        if p.Email_ID == loginUser:
            context["Subjects"] = p.Offering_Courses.all()

    print(context["Subjects"] )

    studs = student.objects.all()
    ## Populating Attendance Record from CSV file 
    # Subject wise
    std_DB = pd.read_csv('services/AMS/std_DB.csv')

    for subj in context["Subjects"]:
        stud_atd_cnt = []
        for s in studs:
            if subj in s.Subjects.all():
                attend_count = std_DB.loc[std_DB["Rollno"] == s.Roll_Number, [str(subj)] ].values
                print(s.Roll_Number)
                print(attend_count)
                try:
                    stud_atd_cnt.append( [s.Roll_Number, attend_count[0][0] ] )
                except:
                    continue
        stud_Attendance_Cnt[str(subj)] = stud_atd_cnt

    context["stud_Attendance_Cnt"] = stud_Attendance_Cnt
    print(context)
    # return HttpResponse('Successfully stored in  the database')
    return render(request, 'Reports/prof_report.html', context)