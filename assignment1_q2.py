from datetime import date
c_date = date.today()
s1 = c_date.strftime('%d-%m-%Y') 
print('current date: ',s1) 
print('year: ',s1[6:])                                                            