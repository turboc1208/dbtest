######
# By : Chip Cox
######
import adbase
import datetime

class dbtest(adbase.ADBase):
    def initialize(self):
        self.adapi = self.get_ad_api()
        self.adapi.log("Initializing %s",self.name)
