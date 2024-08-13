
print()
print()
print('''                             ******************************************************************
                                \t    STUDENT REPORT CARD MANAGEMENT SYSTEM
                             ******************************************************************''')
print()

#============================ sql connection ==================================

import random as r
import mysql.connector as m

connection=''
try:
    conn=m.connect(host='localhost',user='root',password='aman',database='studentdb')
    cur=conn.cursor()
    connection='ok'
except:
    print('====connection to sql failed====')
    print('....please check code for correct PASSWORD and DATABASE ....')
    print()
    
if connection=='ok':
    cur.execute('show tables')
    rec=cur.fetchall()
    table=''
    if ('student',) in rec:
        table='ok'
    else:
        sql="CREATE TABLE student(roll int(4),ID INT(10) primary key,Name varchar(20),class int(3),pname varchar(20),total float(5,2)"
        sql1=",percent float(5,3),math int(3),chemistry int(3),physics int(3),cs int(3),english int(3),DOB DATE ,city varchar(15),sec char(3));"
        SQL=sql+sql1
        cur.execute(SQL)
        conn.commit()
        table='ok'
#=========================== functions ======================================

def profile():
    
    name=input('enter student name       :')
    clas=int(input('enter class (in digit)   :'))
    sec=input('enter section            :')
    pname=input('enter father name        :')
    city=input('enter city name          :')
    
    try:
        dt=Date()
    except IndexError:
        print('...enter date in correct format...')
        dt=Date()
    rl=ROLL()
    Id=ID()
    
    sql1='insert into student(name,class,sec,pname,dob,roll,Id,city) '
    sql2='values("{}",{},"{}","{}","{}",{},{},"{}")'

    cur.execute(sql1+sql2.format(name,clas,sec,pname,dt,rl,Id,city))
    conn.commit()
    print()
    print('========= student added =======')
    print()
    print('student name :  ',name)
    print('class        :  ',clas,sec)
    print('roll         :  ',rl)
    print('id           :  ',Id,'        PLEASE! Note your ID and ROLL')
    print('date of birth:  ',dt)
    print('parent name  :  ',pname)
    print('city         :  ',city)
    print()
    print('===============================')

def add_marks():
    
    name=input('enter student name       :')
    roll=int(input('enter roll no.           :'))
    clas=int(input('enter class              :'))
    sec=input('enter section            :')
    SQL='select name, roll, id from student where name="{}" and roll={} and class={} and sec="{}"'
    cur.execute(SQL.format(name,roll,clas,sec))
    rec=cur.fetchone()
    sqlm='select total from student where name="{}" and roll={} and class={} and sec="{}"'
    cur.execute(sqlm.format(name,roll,clas,sec))
    recm=cur.fetchone()
    if rec==None:
        print()
        print('===>>> record related to given information not found in file <<<===')
        print('            ....enter correct information of student...            ')
        print()
        #add_marks()

    else:
        if recm[0]==None:
            marks(name,roll,clas,sec)
            print()
            print('========== marks added ==========')
        else:
            print()
            print('\tmarks of "{}" already added in file'.format(name))
            choice=input('\tdo you want to modify marks [y/n]  :')
            if choice=='y':
               marks(name,roll,clas,sec)
            else:
                pass
            
    
def class_record():
    
    clas=int(input('enter class              :'))
    sec=input('enter section            :')
    print()
    sql='select Id,roll,name,pname,total,percent,physics,chemistry,math,cs,english,dob '
    sql1='from student where class={} and sec="{}" order by roll'

    cur.execute(sql+sql1.format(clas,sec))
    rec=cur.fetchall()

    if len(rec)==0:
        
        print('===>>> no record found, related to class={} "{}" <<<==='.format(clas,sec))
        print()

    else:
        
        print('ID      ',end='')
        print('ROLL   ',end='')
        print("student's name   ",end='')
        print('D.O.B.        ',end='')
        print("parent's name    ",end='')
        print('marks   ',end='')
        print('percent   ',end='')
        print('phy     ',end='')
        print('che     ',end='')
        print('math    ',end='')
        print('cs      ',end='')
        print('eng')

        for s in rec:
            l=len(str(s[0]))
            l1=len(str(s[1]))
            l2=len(str(s[2]))
            l3=len(str(s[3]))
            l4=len(str(s[4]))
            l5=len(str(s[5]))
            l6=len(str(s[6]))
            l7=len(str(s[7]))
            l8=len(str(s[8]))
            l9=len(str(s[9]))
            l10=len(str(s[11]))

            print(s[0],end='')#id
            for i in range(8-l):
                print(' ',end='')

            print(s[1],end='')#roll
            for i in range(7-l1):
                print(' ',end='')

            if len(s[2])<14:#student name
                   print(s[2],end='')
            else:
                   print(s[2][0:15],'.',end='')
            for i in range(17-l2):
                print(' ',end='')

            print(s[11],end='')#dob
            for i in range(14-l10):
                print(' ',end='')

            if len(s[3])<14:#parent name
                   print(s[3],end='')
            else:
                   print(s[3][0:15],end='')
                   print('  ',end='')
            for i in range(17-l3):
                print(' ',end='')

            print(s[4],end='')#marks
            for i in range(8-l4):
                print(' ',end='')

            print(s[5],'%',end='')#percent
            for i in range(8-l5):
                print(' ',end='')

            print(s[6],end='')#physics
            for i in range(8-l6):
                print(' ',end='')

            print(s[7],end='')#chemistry
            for i in range(8-l7):
                print(' ',end='')

            print(s[8],end='')#math
            for i in range(8-l8):
                print(' ',end='')

            print(s[9],end='')#cs
            for i in range(8-l9):
                print(' ',end='')

            print(s[10])#english
    print()

def student_record():
    name=input('enter student name       :')
    roll=int(input('enter student roll       :'))
    clas=int(input('enter class              :'))
    sec=input('enter section            :')

    sql='select * from student where name="{}" and roll={} and class={} and sec="{}"'
    cur.execute(sql.format(name,roll,clas,sec))
    rec=cur.fetchone()
    
    if rec==None:
        print()
        print('===>>> record of "{}" not found in file <<<==='.format(name))
        print('            ....try again....')
        print()
        
    else:
        if rec[6]==None:
            print()
            print('\t===>>> marks of "{}" not added in file<<<==='.format(name))
            choice=input('\tdo you want to add marks[y/n]    :')
            print()
            if choice=='y':
                marks(name,roll,clas,sec)
                print()
                print('==========marks added=========')
            elif choice=='n':
                record(name,rec)
        else:
            record(name,rec)
            

def modify_profile():
    
    name=input('enter student name (old)      : ')
    roll=int(input('enter roll                    : '))
    clas=int(input('enter class                   : '))
    sec=input('enter section                 :')
    sql='select name,pname,dob,class,sec from student where name="{}" and roll={} and class={} and sec="{}"'
    cur.execute(sql.format(name,roll,clas,sec))
    rec=cur.fetchall()

    if len(rec)==0:
        print('\n===>>> record of "{}" not found in file <<<==='.format(name))
        print('           ......try again.......')
        #modify_profile()
        
    else:
        print()
        print('====>>> NOTE: to skip input, press ENTER button <<<====')
        print()

        Name=input('enter student new name       : ')
        if len(Name)==0:
            Name=rec[0][0]
            print('your name will be            :',Name)

        pname=input('enter parent new name        : ')
        if len(pname)==0:
            pname=rec[0][1]
            print('your parent name will be     :',pname)

        try:
            clas=int(input('enter new class              : '))
        except ValueError:
            clas=rec[0][3]
            print('your class will be           :',clas)
        
        sec=input('enter section                :')
        if len(sec)==0:
            sec=rec[0][4]
            print('your section will be         :',sec)
            print()
        try:
            date=Date()
        except IndexError:
            date=rec[0][2]
            print('your D.O.B. will be                 :',date)
            print()

            
        sql1='update student set name="{}",pname="{}",class={},dob="{}",sec="{}" where roll={}'
        cur.execute(sql1.format(Name,pname,clas,date,sec,roll))
        conn.commit()
        print()
        print('========= student record updated ============')
        print()


def modify_marks():
    
    name=input('enter student name       :')
    roll=int(input('enter roll               :'))
    clas=int(input('enter class              :'))
    sec=input('enter section            :')
    print()
    print('====>>> NOTE: to skip input, press ENTER button <<<====')
    print()
    
    sql='select physics,chemistry,math,cs,english from student where name="{}" and roll={} and class={} and sec="{}"'
    cur.execute(sql.format(name,roll,clas,sec))
    rec=cur.fetchone()
    if rec==None:
        print('===>>> record of "{}" not found in file <<<==='.format(name))
        print('           ......try again.......')
        modify_marks()
    else:
        try:            
            s1=int(input('Enter marks of Maths     :'))
        except ValueError:
            s1=rec[2]

        try:
            s2=int(input('Enter marks of Chemistry :'))
        except ValueError:
            s2=rec[1]
                    
        try:
            s3=int(input('Enter marks of Physics   :'))
        except ValueError:
            s3=rec[0]

        try:
            s4=int(input('Enter marks of CS        :'))
        except ValueError:
            s4=rec[3]
        try:
            s5=int(input('Enter marks of English   :'))
        except ValueError:
            s5=rec[4]
        

        total=s1+s2+s3+s4+s5
        avg=total/5

        sql='update student set math={},chemistry={},physics={},cs={},english={},'
        sql1='total={},percent={} where name="{}" and roll={} and class={} and sec="{}";'
        SQL=sql+sql1
        cur.execute(SQL.format(s1,s2,s3,s4,s5,total,avg,name,roll,clas,sec))
        conn.commit()
        print()
        print('======= your marks updated as =======:')
        print()
        print('\tmath     :',s1)
        print('\tchemistry:',s2)
        print('\tphysics  :',s3)
        print('\tcs       :',s4)
        print('\tenglish  :',s5)
        print()


def DELETE():
    
    name=input('enter student name       :')
    clas=int(input('enter class              :'))
    sec=input('enter section            :')
    roll=int(input('enter roll               :'))
    
    sql='select name,id,roll from student where name="{}" and class={} and roll={} and sec="{}"'
    cur.execute(sql.format(name,clas,roll,sec))
    rec=cur.fetchall()
    if len(rec)==0:
        print()
        print('====>>> record of "{}" was not exist in file <<<===='.format(name))
        print()
    else:
        sql1='delete from student where name="{}" and roll={} and class={} and sec="{}"'
        cur.execute(sql1.format(name,roll,clas,sec))
        conn.commit()
        print()
        print('========= record of "{}" deleted from file ==========='.format(name))
        print()
        
#=================== additional funtions use in programe =================

def Date():
    
    d=input('enter D.O.B. in formate (yyyy-mm-dd):')
    
    if (d[4]=='-' and '-' in d and d[0]!='0' and d[0:2]!='00' and d[0:3]!='000' and d[0:4]!='0000' and d[5:7]!='00' and d[8:10]!='00'):
        dt=d.split('-')
        
        if int(dt[1])<13:
            
            if int(dt[1]) in (4,6,9,11) and int(dt[2])<31:
                return d
            
            elif int(dt[1]) in (1,3,5,7,8,10,12) and int(dt[2])<32:
                return d
            
            elif int(dt[1])==2:
                if(int(dt[0])%100==0):
                    if(int(dt[0])%400==0):
                        if(int(dt[2])<=29):
                            return d
                        
                        elif (int(dt[2]))<=28:
                            return d
                        
                        else:
                            print('=>> enter valid date................')
                            return Date()
                            
                elif (int(dt[0])%4==0):
                    if int(dt[2])<=29:
                        return d
                    
                    else:
                        print('=>> enter valid date................')
                        return Date()
                        
                else:
                    if int(dt[2])<=28:
                        return d
                    
                    else:
                        print('=>> enter valid date................')
                        return Date()
            else:
                print('=>> invalid day no. try agin........')
                return Date()
        else:
            print('=>> invalid month no. try again.....')
            return Date()
    else:
        print('=>> please enter date in formate (yyyy-mm-dd):')
        return Date()

def ID():
    sql='select id from student'
    cur.execute(sql)
    rec=cur.fetchall()
    while True:
        id=r.randrange(10101,99999)
        if (id,) not in rec:
            return id
        else:
            continue
 

def ROLL():
    
    b=[]
    sql='select roll from student'
    cur.execute(sql)
    rec=cur.fetchall()
    for i in rec:
        a=i[0]
        b.append(a)
    for j in range(1,100):
        if j not in b:
            return(j)

def marks(name,roll,clas,sec):
    
        def S1():
            s1=int(input('Enter marks of Maths     :'))
            if s1<101:
                return s1
            else:
                print()
                print('please enter marks between 0 and 100')
                print()
                return S1()
        s1=S1()
        
        def S2():
            s2=int(input('Enter marks of Chemistry :'))
            if s2<101:
                return s2
            else:
                print()
                print('please enter marks between 0 and 100')
                print()
                return S2()
        s2=S2()

        def S3():
            s3=int(input('Enter marks of Physics   :'))
            if s3<101:
                return s3
            else:
                print()
                print('please enter marks between 0 and 100')
                print()
                return S3()
        s3=S3()

        def S4():
            s4=int(input('Enter marks of CS        :'))
            if s4<101:
                return s4
            else:
                print()
                print('please enter marks between 0 and 100')
                print()
                return S4()
        s4=S4()

        def S5():
            s5=int(input('Enter marks of English   :'))
            if s5<101:
                return s5
            else:
                print()
                print('please enter marks between 0 and 100')
                print()
                return S5()
        s5=S5()

        
        total=s1+s2+s3+s4+s5
        avg=total/5

        sql='update student set math={},chemistry={},physics={},cs={},english={},'
        sql1='total={},percent={} where name="{}" and roll={} and class={} and sec="{}";'
        SQL=sql+sql1
        cur.execute(SQL.format(s1,s2,s3,s4,s5,total,avg,name,roll,clas,sec))
        conn.commit()


def record(name,rec):
    
    print(' _________________________________________________')
    print('|')
    print('|  student name :  ',name)
    print('|  class        :  ',rec[3],rec[14])
    print('|  roll         :  ',rec[0])
    print('|  id           :  ',rec[1])
    print('|  date of birth:  ',rec[5])
    print('|  parent name  :  ',rec[4])
    print('|  city         :  ',rec[13])
    print('|................................................')
    print('|  subject          marks')
    print('|................................................')
    print('|  physics      :  ',rec[10])
    print('|  chemistry    :  ',rec[9])
    print('|  maths        :  ',rec[8])
    print('|  cs           :  ',rec[11])
    print('|  englis       :  ',rec[12])
    print('|  total        :  ',rec[6])
    print('|  percent      :  ',rec[7],'%')

    if rec[6]==None:
        print('|_________________________________________________')
    elif rec[6]>165:
        print('|  ==PASS==')
        print('|_________________________________________________')
    else:
        print('|  ==FAIL==')
        print('|_________________________________________________')
    print()
        
#====================== function call =================================

if connection=='ok' and table=='ok':
    while True:
        print()
        print('===========================| MENU |================================  ')
        print()
        print('1. to add student name')
        print('2. to insert marks of student')
        print('3. to view record of class')
        print('4. to view record of a student')
        print('5. to modify student details')
        print('6. to modify student marks')
        print('7. to delete a record')
        print('8. EXIT')
        print()
        choice=input('=>ENTER YOUR CHOICE [1-8]  :')
        print()
        
        if choice=='1':
            print('========== admission of student ==========')
            print()
            profile()
            
        elif choice=='2':
            print('============= insert marks==============')
            print()
            add_marks()
            
        elif choice=='3':
            print('=========== view record of a class=========')
            print()
            class_record()
            
        elif choice=='4':
            print("======== view a student's detail =========")
            print()
            student_record()
            
        elif choice=='5':
            print("======== modify student's detail=======")
            print()
            modify_profile()
            
        elif choice=='6':
            print('======= modify marks of a student ======')
            print()
            modify_marks()
            
        elif choice=='7':
            print('========== delete student record ==========')
            print()
            DELETE()
            
        elif choice=='8':
            print('*'*80)
            print('         \t\t           thank you')
            print('*'*80)
            break
        
        else:
            print('    ......invalid input, try again.....')
            print()

