from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
print ("{:>35}".format("COVID-19"))
STATE = ['Maharastra','Tamil Nadu','Delhi','Gujrat','Uttar Pradesh','Rajasthan','West Bengal','Madhya Pradesh','Haryana','Karnatka','Bihar','Andra Pradesh','Telangana','Jammu Kahmir','Assam','Oddisa','Punjab','Kerala','Uttarakhand','Jharkhand','Chattisgarh','Tripura','Ladakh','Goa','Himachal Pradesh','Manipur','Puducherry','Nagaland','Arunachal Pradesh','Sikkim']
TOTAL_CASES = ['113445','48019','44688','24628','14598','13216','11909','11083','8272','7530','6810','6720','5406','5298','4511','4338','3371','2623','1942','1839','1784','1090','649','629','560','500','368','216','181','99','72']
DEATHS = ['5537','528','1837','1534','435','308','495','476','118','95','39','88','191','63','08','14','71','21','25','9','9','1','1','0','7','0','6','4','0','0','0']
RECOVERED = ['57851','26782','16500','17090','8904','9962','6028','8152','3748','4456','4571','3513','3027','2781','2412','2974','2461','1234','1216','1121','934','556','85','85','361','159','301','99','103','7','8']
table = PrettyTable(['STATE','TOTAL_CASES','DEATHS','RECOVERED'])
for x in range(0,30):
    table.add_row([STATE[x],TOTAL_CASES[x],DEATHS[x],RECOVERED[x]])
print (table)

VAL='YES'
while VAL=='YES':
    print ("Enter the graphical representation u want to see") 
    print ("1- Total cases / Deaths / Recoveries ") 
    print ("2- STATE/TERRITORY VS TOTAL CASES")
    print ("3- STATE/TERRITORY VS DEATHS")
    print ("4- STATE/TERRITORY VS RECOVERED")
    print ("On the basis of data select which query u want to know")
    print ("5- Which state has the highest COVID-19 cases")
    print ("6- Which state has the lowest COVID-19 cases")
    print ("7- Which state has the highest DEATHS")
    print ("8- Which state has the lowest DEATHS")
    print ("9- Which state has the highest RECOVERIES")
    print ("10- Which state has the lowest RECOVERIES")
    
   
    
    num = int(input("Enter your choice: \n Please choose a number from options"))
    print ("You chose option no-")
    print (num)

# bar graph for choice-1
    if num==1:
        exp_vals = [346394,11921,187481]
        exp_labels = ["TOTAL CASES","DEATHS","RECOVERED"]
        plt.axis("equal")
        plt.pie(exp_vals,labels=exp_labels, shadow=True, autopct='%1.1f%%',radius=1.5)
        plt.show()
    
# bar graph for choice 2
    elif num==2:
    
        STATES=['Maharastra','Tamil Nadu','Delhi','Gujrat','Uttar Pradesh','Rajasthan','West Bengal','Madhya Pradesh','Haryana','Karnatka','Bihar','Andra Pradesh','Telangana','Jammu Kahmir','Assam','Oddisa','Punjab','Kerala','Uttarakhand','Jharkhand','Chattisgarh','Tripura','Ladakh','Goa','Himachal Pradesh','Manipur','Puducherry','Nagaland','Arunachal Pradesh','Sikkim']
        CASES=[113445,48019,44688,24628,14598,13216,11909,11083,8272,7530,6810,6720,5406,5298,4511,4338,3371,2623,1942,1839,1784,1090,649,629,560,500,368,216,181,99]
        xpos = np.arange(len(STATES))
        xpos
        plt.bar(xpos,CASES, label="CASES")

        plt.xticks(xpos,STATES,rotation=90)
        plt.ylabel("STAES/TERRITORY")
        plt.title('CASES')
        plt.legend()
        plt.show()

# bar graph for choice-3
    elif num==3:
        STATES=['Maharastra','Tamil Nadu','Delhi','Gujrat','Uttar Pradesh','Rajasthan','West Bengal','Madhya Pradesh','Haryana','Karnatka','Bihar','Andra Pradesh','Telangana','Jammu Kahmir','Assam','Oddisa','Punjab','Kerala','Uttarakhand','Jharkhand','Chattisgarh','Tripura','Ladakh','Goa','Himachal Pradesh','Manipur','Puducherry','Nagaland','Arunachal Pradesh','Sikkim']
        DEATHS=[5537,528,1837,1534,435,308,495,476,118,95,39,88,191,63,8,14,71,21,25,9,9,1,1,0,7,0,6,4,0,0]
        xpos = np.arange(len(STATES))
        xpos
        plt.bar(xpos,DEATHS, label="DEATHS")
        plt.xticks(xpos,STATES,rotation=90)
        plt.ylabel("STAES/TERRITORY")
        plt.title('DEATHS')
        plt.legend()
        plt.show()

# bar graph for choice-4
    elif num==4:
        STATES=['Maharastra','Tamil Nadu','Delhi','Gujrat','Uttar Pradesh','Rajasthan','West Bengal','Madhya Pradesh','Haryana','Karnatka','Bihar','Andra Pradesh','Telangana','Jammu Kahmir','Assam','Oddisa','Punjab','Kerala','Uttarakhand','Jharkhand','Chattisgarh','Tripura','Ladakh','Goa','Himachal Pradesh','Manipur','Puducherry','Nagaland','Arunachal Pradesh','Sikkim']
        RECOVERED=[57851,26782,16500,17090,8904,9962,6028,8152,3748,4456,4571,3513,3027,2781,2412,2974,2461,1234,1216,1121,934,556,85,85,361,159,301,99,103,7]
        xpos = np.arange(len(STATES))
        xpos
        plt.bar(xpos,RECOVERED, label="RECOVERED")
        plt.xticks(xpos,STATES,rotation=90)
        plt.ylabel("STAES/TERRITORY")
        plt.title('RECOVERED')
        plt.legend()
        plt.show()

# answer for choice-5
    elif num==5:
        print("MAHARASTRA")

#answer for choice-6
    elif num==6:
        print("SIKKIM")

#answer for choice-7
    elif num==7:
        print("MAHARASTRA")

#answer for choice-8
    elif num==8:
        print("SIKKIM, ANDRA PRADESH, NAGALAND, MANIPUR, GOA are with 0 death cases")
        print("LADAKH, TRIPURA are with 1 death case")

#answer for choice-9
    elif num==9:
        print("MAHARASTRA")

# answer for choice -10
    elif num==10:
        print("ANDRA PRADESH")
        

    VAL=input("Do you want to continue- YES/NO")




