######
# By : Chip Cox
######
import adbase
import datetime
import mysql.connector

class dbtest(adbase.ADBase):
    def initialize(self):
        self.adapi = self.get_ad_api()
        self.adapi.log("Initializing %s",self.name)
        
        mydb=mysql.connector.connect(
                host="192.168.2.20",
                user="homeassistant",
                password="Mario!23",
                database="House10611",auth_plugin='mysql_native_password')

        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM House10611.rooms order by mod(breaker,2)*-1,breaker,subbreaker")

        myresult=mycursor.fetchall()

        for x in myresult:
            print(x)

