import random
import calendar
import datetime
# import importlib.util
# spec = importlib.util.spec_from_file_location("Hjemme", "/Users/andreasschade/PycharmProjects/Scrapying/scrapoing projects/hjemme.py")
# hjemme = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)
# hjemme.MyClass()

def len_iter(i):
    return sum(1 for e in i)



from datetime import date
# alternativ dictonarry-to-key metode
# værrelser = {
#     617: "Schade"
#     ,618: "Philipp"
#     ,619: "Nadia"
#     # ,620: "Oscar"
#     ,621: "Solvej"
#     ,622: "Benne"
#     # ,623: "Maja + Kristian"
#     ,625: "Niels"
#     ,626: "Lucas"
#     ,628: "Claes"}

værrelser = {
    "Schade": 617
    ,"Philipp": 618
    ,"Nadia": 619
    ,"Oscar": 620
    ,"Solvej": 621
    # ,"Benne": 622
    ,"Maja + Kristian": 623
    ,"Niels": 625
    ,"Lucas": 626
    ,"Claes": 628}

a1=a2=a3=0
seed_num = 320
# ----------------------------------------------------
# for bestemt rækkefølge
# while True:
# seed_num = seed_num+1
# ----------------------------------------------------
print('Seed number =',seed_num, 'SEED numb! ----')
random.seed(seed_num)
rækkefølge = random.sample(værrelser.items(),len(værrelser))
print("rækkefølge",rækkefølge)
# print("værrelses længde:",len(værrelser))



now_date = datetime.datetime.now()
now = now_date.strftime('%Y,%m')
now_update = now_date.strftime('%d/%m/%Y')
# now_week = now_date.strftime('%Y,%-m,%-d')
print(now_update)
# kan også laves til HTML
c = calendar.LocaleHTMLCalendar(calendar.MONDAY)
week_number = datetime.date(int(now_date.strftime('%Y')),int(now_date.strftime('%-m')),int(now_date.strftime('%-d'))).isocalendar()[1]
d = "2019-W{0}".format(week_number-1)
week_start_date = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w").strftime('%d/%m')
week_end_date = datetime.datetime.strptime(d + '-0', "%Y-W%W-%w").strftime('%d/%m')
n = 0
n1 = 0
WEEK_STRING =[]
WEEK_TABLES =""""""
UGE_COUNT =0
i=0
CURRENT_WEEK_FLAG =0
PASSED_CURRENT_FLAG =0
for i in range(2):
    for i in c.itermonthdates(int(now[0:4]),int(now[5:7])+i):
        dato = i.strftime('%A the %d. %B %Y, uge: %w')

        if i.strftime('%d/%m/%Y')==now_update:
            CURRENT_WEEK_FLAG = 1

        if i.strftime('%w') == '1':
            MONDAY_STRING_NAME='<td class ="mandag"> {0} </td>'.format(str((rækkefølge[n])[0])+' '+(str((rækkefølge[n][1]))))
            MONDAY_STRING_DATE='<td class ="mandag"> {0} </td>'.format(i.strftime('%d/%m'))
            week_number = datetime.date(int(i.strftime('%Y')), int(i.strftime('%-m')),
                                        int(i.strftime('%-d'))).isocalendar()[1]
            d = "2019-W{0}".format(week_number - 1)
            week_start_date = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w").strftime('%d/%m')
            week_end_date = datetime.datetime.strptime(d + '-0', "%Y-W%W-%w").strftime('%d/%m')
            n=n+1
        elif i.strftime('%w') == '2':
            TUESDAY_STRING_NAME='<td class ="tirsdag" > {0} </td>'.format(str((rækkefølge[n])[0])+' '+(str((rækkefølge[n][1]))))
            TUESDAY_STRING_DATE='<td class ="mandag"> {0} </td>'.format(i.strftime('%d/%m'))
            n=n+1
        elif i.strftime('%w') == '3':
            WEDNESDAY_STRING_NAME='<td class ="onsdag"> {0} </td>'.format(str((rækkefølge[n])[0])+' '+(str((rækkefølge[n][1]))))
            WEDNESDAY_STRING_DATE='<td class ="mandag"> {0} </td>'.format(i.strftime('%d/%m'))
            n=n+1
        # elif i.strftime('%w') == '4':
        #     print('torsdag')
        # elif i.strftime('%w') == '5':
        #     print('fredag')
        # elif i.strftime('%w') == '6':
        #     print('lørdag')
        elif i.strftime('%w') == '0':
            WEEK_STRING.append(str(UGE_COUNT))
            if CURRENT_WEEK_FLAG == 1 or PASSED_CURRENT_FLAG:
                PASSED_CURRENT_FLAG=1
                if CURRENT_WEEK_FLAG == 1:
                    WEEK_STRING[UGE_COUNT] = """
                    <table id="current">
                    <caption><b>Uge nummer: {0}, hvilket svarer til datoerne: {1}-{2} <b/></caption>
                    <tr>
                    <th>Mandag</th><th>Tirsdag</th><th>Onsdag</th>
                    </tr>
                    <tr>{6}{7}{8}
                    </tr>
                    </tr>
                    <tr>{3}{4}{5}
                    </tr>    
                    </table>
                    <br/><br/>
                    """.format(week_number, week_start_date, week_end_date, MONDAY_STRING_NAME,
                               TUESDAY_STRING_NAME, WEDNESDAY_STRING_NAME, MONDAY_STRING_DATE,
                               TUESDAY_STRING_DATE, WEDNESDAY_STRING_DATE)
                else:
                    WEEK_STRING[UGE_COUNT]="""
                    <table style="width:70%">
                    <caption>Uge nummer: {0}, hvilket svarer til datoerne: {1}-{2} </caption>
                    <tr>
                    <th>Mandag</th><th>Tirsdag</th><th>Onsdag</th>
                    </tr>
                    <tr>{6}{7}{8}
                    </tr>
                    </tr>
                    <tr>{3}{4}{5}
                    </tr>    
                    </table>
                    <br/><br/>
                    """.format(week_number, week_start_date, week_end_date,MONDAY_STRING_NAME,TUESDAY_STRING_NAME,WEDNESDAY_STRING_NAME,MONDAY_STRING_DATE,TUESDAY_STRING_DATE,WEDNESDAY_STRING_DATE)
            else:
                WEEK_STRING[UGE_COUNT]=""""""""
            # print(WEEK_STRING)
            MONDAY_STRING=TUESDAY_STRING=WEDNESDAY_STRING=''
            CURRENT_WEEK_FLAG = 0
            WEEK_TABLES = (WEEK_TABLES+WEEK_STRING[UGE_COUNT])
            UGE_COUNT = UGE_COUNT +1
        if n1 < 1:
            start_date = i.strftime('%d/%m/%Y')
        n1 = n1+1
        if n1 == len_iter(c.itermonthdates(2019,3)):
            end_date = i.strftime('%d/%m/%Y')


        # print(dato)
        # if "Mon" in dato or "Tue" in dato or "Wedn" in dato:
        #     print(rækkefølge[n])
        #     n=n+1
        if n == len(værrelser):
            n = 0

# ----------------------------------------------------
# for bestemt rækkefølge
# a1 = int((rækkefølge[n-3])[1])
# a2 = int((rækkefølge[n-2])[1])
# a3 = int((rækkefølge[n-1])[1])
# print('de sidste er', a1,a2,a3)
# if a1==621 and a2==619 and a3==617:
#     break
# ----------------------------------------------------

dic1 = dict(rækkefølge)
# print(dic1.items())
# print(dic1.values())

c1=calendar.HTMLCalendar(calendar.MONDAY)
monthhtml = c1.formatmonth(2019,3,3000)



html_str_start = f"""
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {{
border: 1px solid black;
border-collapse: collapse;
}}
th, td {{
padding: 5px;
text-align: center;
}}
th{{
background-color: #54CEB6;
color: #000000;}}
#current {{
font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
border-collapse: collapse;
width: 70%;
}}
#current th{{
background-color: #F30B0B;
color: #000000;}}
tr:hover {{background-color:#f5f5f5;}}
</style>
</head>
<body>
<center>
<h1>Madklub 6. Øst!</h1>
<p>Dato: {start_date} - {end_date}</p>
{WEEK_TABLES}
"""
html_str_end="""
<p align="left"><i>Rækkefølge: seed number = {0}</i></p>
<p align="left"><i>Sidste update: {1}</i></p>
</center>
</body>
</html>
""".format(seed_num, now_update,)


Html_file= open("Madklub_HTML.html","w")
Html_file.write(html_str_start)
Html_file.write(html_str_end)
Html_file.close()




#
# html_str = """
# <table border=1>
#      <tr>
#        <th>Number</th>
#        <th>Square</th>
#      </tr>
#      <indent>
#      <% for i in range(10): %>
#        <tr>
#          <td><%= i %></td>
#          <td><%= i**2 %></td>
#        </tr>
#      </indent>
# </table>
# """


# c1 = calendar.Calendar(firstweekday=0)
#
# for i in c1.itermonthdays(2019,3):
#     print(i)
# d=datetime.date(2019,12,5)
# i = today()
# print(str(now))
# print(c1.__format__('%A,%d,%B,%Y'))
