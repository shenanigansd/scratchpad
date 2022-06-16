import os
import csv
import numpy as np
import datetime

cwd = os.getcwd()
i = datetime.datetime.now()

apcsv = []
test = []

class importExcel(object):

    def __init__(self):
        teststr = "MontyPython"
    def import_ap_excel(self):
        for file in os.listdir(cwd + r'\input\ap'):
            if file.endswith('.csv'):
                apcsv.append(file)

    def import_excel_files(self):
        self.import_ap_excel()

class Generateff(object):

    def __init__(self):
        teststr = "MontyPython"

    def order_block(self,file,filename,data,**kwargs):
        
        '''        
        if ob_orderType == "EMBROIDERY":
            ob_orderType = "26.1"
        elif ob_orderType == "SCREENPRINT":
            ob_orderType = "13"
        else: 
            print
            ob_orderType = raw_input("In file " + "\"" + filename + "\"" + "the order type is " + str(data[1,14]) + ". " + "Please enter a value for \"id_OrderType\"\n")
        '''
        
        ondict = {"EMBROIDERY":"26.1","SCREENPRINT":"13"}
        try:
            ob_orderType = ondict[ob_orderType]
        except KeyError:
            temp = ob_orderType
            ob_orderType = raw_input("In file " + "\"" + filename + "\"" + "the order type is " + str(data[1,14]) + ". " + "Please enter a value for \"id_OrderType\"\n")
            ondict.update({temp, ob_orderType})
                

        file.write("---- Start Order ----\n") 
        for name, value in kwargs.items():
            print(f"{name}: {value!s}", file=file)))
        file.write("---- End Order ----\n")

    def customer_block(self,file,customer,**kwrags):
        
        if customer == "ap":
            cus_idCus = "3228"
            cus_company = "ap"

        file.write("---- Start Customer ----\n")
        for name, value in kwargs.items():
            print(f"{name}: {value!s}", file=file)
        file.write("---- End Customer ----\n")

    def contact_block(self,file,contact,**kwargs):
        
        if contact == "ap":
            pass
        if contact == "webstore":
            con_nameFirst = "Webstore"
            con_phone = "800-555-5555"
            con_email = "webstore@ap.com"

        file.write("---- Start Contact ----\n")
        for name, value in kwargs.items():
            print(f"{name}: {value!s}", file=file)
        file.write("---- End Contact ----\n")
        
    def design_block(self):
        pass

    def location_block(self):
        pass

    def product_block(self, file, **kwargs):
        file.write("---- Start Product ----\n")
        for name, value in kwargs.items():
            print(f"{name}: {value!s}", file=file)
        file.write("---- End Product ----\n")

    def payment_block(self, file, **kwargs):
        file.write("---- Start Payment ----\n")
        for name, value in kwargs.items():
            print(f"{name}: {value!s}", file=file)
        file.write("---- End Payment ----\n") 

    def create_array(self,x):
        filename = apcsv[x]
        fnap = os.path.join(cwd + r'\\input\\ap\\', filename)
        with open(fnap,'r') as file:
            data_iter = csv.reader(file, delimiter = ',', quotechar = '"')
            data = [data for data in data_iter]
        data_array = np.asarray(data, dtype = None)
        test.append(data_array)  
        return data_array,filename

    def create_ap_order(self,file,data, filename):
        file.write('\n"\n')
        self.order_block(file, filename,data, ob_extOrderID = str(data[1,0]+data[1,3]),ob_orderType = str(data[1,14]))
        self.customer_block(file,customer = "ap")
        self.contact_block(file,contact = "ap")
        self.payment_block(file)
        self.product_block(file)
        file.write('\n"\n')

    def createfile(self):
        file = open(cwd + "\\output\\%s_%s_%s.txt" % (i.month, i.day, i.year),'w+')
        for x in range(len(apcsv)):
            data, filename = self.create_array(x)
            ots = []
            tarr = []        
            for j in range(len(data[:,14])):
                if data[j,14] not in ots:
                    ots.append(data[j,14])
            ots = list(set(ots))
            ots.remove("Deco Type")
            for x in ots:
                exec("%s1 = []" % (x))
                exec("tarr.append(%s1)" % (x))
                for m in range(len(data[:,:])):
                    if data[m,14] == x:
                        exec("%s1.append(data[m,:])" % (x))
            for x in tarr:
                self.create_ap_order(file, data, filename)
        file.close()

if __name__ == "__main__":
    ime = importExcel()
    ime.import_excel_files()
    genff = Generateff()
    genff.createfile()
