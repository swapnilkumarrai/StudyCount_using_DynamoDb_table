import study_dynamo_db1
import datetime

date_format1="%Y-%m-%d"
date_format2="%Y-%m"

def generate_study_count():
    #To generate no. of blocks on a specific date
    study_count=0
    date1=month1=year1=0

    n=input("Enter 'y' for year, 'd' for date or 'm' for month: ")

    if(n=='d'):
        date1=input('Enter date: ')
        month1=input('Enter month: ')
        year1=input('Enter year: ')
        default_date=f'{year1}-{month1}-{date1}'
        date1=datetime.datetime.strptime(default_date, date_format1)
        print(f'You are looking for {date1}')
    if(n=='m'):
        month1=input('Enter month: ')
        year1=input('Enter year: ')
        default_date=f'{year1}-{month1}'
        month1=datetime.datetime.strptime(default_date, date_format2)
        print(f'You are looking for {month1}')
    if(n=='y'):
        year1=input('Enter year: ')
        default_date=f'{year1}-09-03'
        year1=datetime.datetime.strptime(default_date, date_format1)
        year1=year1.year
        print(f'You are looking for {year1}')


    for i in range(0, len(study_dynamo_db1.lis)):
        date=study_dynamo_db1.lis[i]
        study_created=datetime.datetime.strptime(date, date_format1)
        x=f'{study_created.year}-{study_created.month}'
        date2=study_created
        month2=datetime.datetime.strptime(x, date_format2)
        year2=study_created.year
        
        if(date1==date2):
            study_count=study_count+1
        if(month1==month2):
            study_count=study_count+1
        if(year1==year2):
            study_count=study_count+1

    print("Total no. of studies created: ",study_count)



generate_study_count()