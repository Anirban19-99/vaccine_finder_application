import requests
import datetime
pin=input("Enter Pin Code:")
if(len(pin)!=6):
    print("Invalid Date")
    quit()

today=datetime.date.today()
date=today.strftime("%d-%m-%y")

data=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pin,date))
data=data.json()
total_centers=len(data['centers'])

if (total_centers==0):
    print("No Available Center")
    quit()
print("Total AVilable Center:",total_centers)
print()

for i in range  (total_centers):
    total_session = len(data['centers'][i]["sessions"])
    print("Center No {}:{}:{}".format(i+1,data['centers'][i]["name"],data['centers'][i]["address"]))
    fee = data['centers'][i]["fee_type"]


    if(data['centers'][i]["fee_type"]=="Paid"):
            vaccine_price=data['centers'][i]['vaccine_fees'][0]['fee']
    else:
        vaccine_price="Free"

    print("   Date         Min Age      Max Age       Vaccine Type         Price         First Dose      Second Dose    Precaution Dose")
    print("----------   ------------  -----------   ----------------    -----------    --------------  --------------- -------------------")


    for j in range(total_session):
        cur_session=data['centers'][i]['sessions'][j]
        prec_dose=(cur_session["available_capacity"]-(cur_session["available_capacity_dose1"]+cur_session["available_capacity_dose2"]))

        if(cur_session["allow_all_age"])=="false":
            print(cur_session["date"],cur_session["min_age_limit"],cur_session["max_age_limit"],cur_session["vaccine"],vaccine_price,cur_session["available_capacity_dose1"],cur_session["available_capacity_dose2"],prec_dose)
        else:
            print("{0:^12} {1:^12} {2:^14} {3:^16} {4:^16} {5:^16} {6:^16} {7:^16} ".format(cur_session["date"], cur_session["min_age_limit"], "All Age",
                  cur_session["vaccine"],vaccine_price, cur_session["available_capacity_dose1"],
                  cur_session["available_capacity_dose2"], prec_dose))
    print()
    print()
    print()


