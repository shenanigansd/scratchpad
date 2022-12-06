import csv
import datetime
import os

import numpy as np

cwd = os.getcwd()
i = datetime.datetime.now()

apcsv = []
test = []


class importExcel(object):
    def __init__(self):
        teststr = "MontyPython"

    def import_ap_excel(self):
        for file in os.listdir(cwd + r"\input\ap"):
            if file.endswith(".csv"):
                apcsv.append(file)

    def import_excel_files(self):
        self.import_ap_excel()


class Generateff(object):
    def __init__(self):
        teststr = "MontyPython"

    def order_block(
        self,
        file,
        filename,
        data,
        ob_extOrderID="",
        ob_extSource="",
        ob_extDate="",
        ob_orderType="",
        ob_cusPONum="",
        ob_termsName="",
        ob_cusServRep="",
        ob_cusType="",
        ob_cusLoc="",
        ob_saleStatus="",
        ob_commishAllow="",
        ob_holdOrderText="",
        ob_dateOrderPlaced="",
        ob_orderRequestShip="",
        ob_orderDropDead="",
        ob_salesTaxOverride="",
        ob_applySalesTax1="",
        ob_applySalesTax2="",
        ob_applySalesTax3="",
        ob_applySalesTax4="",
        ob_shipTaxable="",
        ob_accountSalesTax1="",
        ob_accountSalesTax2="",
        ob_accountSalesTax3="",
        ob_accountSalesTax4="",
        ob_addressDescription="",
        ob_addressCompany="",
        ob_address1="",
        ob_address2="",
        ob_addressCity="",
        ob_addressState="",
        ob_addressZip="",
        ob_addressCountry="",
        ob_shipMethod="",
        ob_curShipping="",
        ob_stsOrderShipAddressAdd="",
        ob_notesArt="",
        ob_notesProduction="",
        ob_notesReceiving="",
        ob_notesPurchasing="",
        ob_notesShipping="",
        ob_notesAccounting="",
        ob_notesPurchasingSub="",
    ):

        """
        if ob_orderType == "EMBROIDERY":
            ob_orderType = "26.1"
        elif ob_orderType == "SCREENPRINT":
            ob_orderType = "13"
        else:
            print
            ob_orderType = raw_input("In file " + "\"" + filename + "\"" + "the order type is " + str(data[1,14]) + ". " + "Please enter a value for \"id_OrderType\"\n")
        """

        ondict = {"EMBROIDERY": "26.1", "SCREENPRINT": "13"}
        try:
            ob_orderType = ondict[ob_orderType]
        except KeyError:
            temp = ob_orderType
            ob_orderType = raw_input(
                "In file "
                + '"'
                + filename
                + '"'
                + "the order type is "
                + str(data[1, 14])
                + ". "
                + 'Please enter a value for "id_OrderType"\n'
            )
            ondict.update({temp, ob_orderType})

        file.write("---- Start Order ----\n")
        file.write("ExtOrderID: %s\n" % (ob_extOrderID))
        file.write("ExtSource: %s\n" % (ob_extSource))
        file.write("date_External: %s\n" % (ob_extDate))
        file.write("id_OrderType: %s\n" % (ob_orderType))
        file.write("CustomerPurchaseOrder: %s\n" % (ob_cusPONum))
        file.write("TermsName: %s\n" % (ob_termsName))
        file.write("CustomerServiceRep: %s\n" % (ob_cusServRep))
        file.write("CustomerType: %s\n" % (ob_cusType))
        file.write("id_CompanyLocation: %s\n" % (ob_cusLoc))
        file.write("id_SalesStatus: %s\n" % (ob_saleStatus))
        file.write("sts_CommishAllow: %s\n" % (ob_commishAllow))
        file.write("HoldOrderText: %s\n" % (ob_holdOrderText))
        file.write("date_OrderPlaced: %s\n" % (ob_dateOrderPlaced))
        file.write("date_OrderRequestedToShip: %s\n" % (ob_orderRequestShip))
        file.write("date_OrderDropDead: %s\n" % (ob_orderDropDead))
        file.write("sts_Order_SalesTax_Override: %s\n" % (ob_salesTaxOverride))
        file.write("sts_ApplySalesTax01: %s\n" % (ob_applySalesTax1))
        file.write("sts_ApplySalesTax02: %s\n" % (ob_applySalesTax2))
        file.write("sts_ApplySalesTax03: %s\n" % (ob_applySalesTax3))
        file.write("sts_ApplySalesTax04: %s\n" % (ob_applySalesTax4))
        file.write("sts_ShippingTaxable: %s\n" % (ob_shipTaxable))
        file.write("coa_AccountSalesTax01: %s\n" % (ob_accountSalesTax1))
        file.write("coa_AccountSalesTax02: %s\n" % (ob_accountSalesTax2))
        file.write("coa_AccountSalesTax03: %s\n" % (ob_accountSalesTax3))
        file.write("coa_AccountSalesTax04: %s\n" % (ob_accountSalesTax4))
        file.write("AddressDescription: %s\n" % (ob_addressDescription))
        file.write("AddressCompany: %s\n" % (ob_addressCompany))
        file.write("Address1: %s\n" % (ob_address1))
        file.write("Address2: %s\n" % (ob_address2))
        file.write("AddressCity: %s\n" % (ob_addressCity))
        file.write("AddressState: %s\n" % (ob_addressState))
        file.write("AddressZip: %s\n" % (ob_addressZip))
        file.write("AddressCountry: %s\n" % (ob_addressCountry))
        file.write("ShipMethod: %s\n" % (ob_shipMethod))
        file.write("cur_Shipping: %s\n" % (ob_curShipping))
        file.write("sts_Order_ShipAddress_Add: %s\n" % (ob_stsOrderShipAddressAdd))
        file.write("NotesToArt: %s\n" % (ob_notesArt))
        file.write("NotesToProduction: %s\n" % (ob_notesProduction))
        file.write("NotesToReceiving: %s\n" % (ob_notesReceiving))
        file.write("NotesToPurchasing: %s\n" % (ob_notesPurchasing))
        file.write("NotestoShipping: %s\n" % (ob_notesShipping))
        file.write("NotesToAccounting: %s\n" % (ob_notesAccounting))
        file.write("NotesToPurchasingSub: %s\n" % (ob_notesPurchasingSub))
        file.write("---- End Order ----\n")

    def customer_block(
        self,
        file,
        customer,
        cus_ExtCusId="",
        cus_idCus="",
        cus_company="",
        cus_idCompanyLoc="",
        cus_terms="",
        cus_webURL="",
        cus_emailMain="",
        cus_addressDesc="",
        cus_addressCompany="",
        cus_address1="",
        cus_address2="",
        cus_addressCity="",
        cus_addressState="",
        cus_addressZip="",
        cus_addressCountry="",
        cus_stsSalesTax1="",
        cus_stsSalesTax2="",
        cus_stsSalesTax3="",
        cus_stsSalesTax4="",
        cus_coaAccountSalesTax1="",
        cus_coaAccountSalesTax2="",
        cus_coaAccountSalesTax3="",
        cus_coaAccountSalesTax4="",
        cus_taxExemptNumber="",
        cus_idDiscountLevel="",
        cus_idDefCalc1="",
        cus_idDefCalc2="",
        cus_cusServRep="",
        cus_cusType="",
        cus_cusSource="",
        cus_referenceFrom="",
        cus_SICCode="",
        cus_SICDesc="",
        cus_nEmployeeCount="",
        cus_custom1="",
        cus_custom2="",
        cus_custom3="",
        cus_custom4="",
        cus_custom5="",
        cus_custom6="",
        cus_custom7="",
        cus_custom8="",
        cus_custom9="",
        cus_custom10="",
    ):

        if customer == "ap":
            cus_idCus = "3228"
            cus_company = "ap"

        file.write("---- Start Customer ----\n")
        file.write("ExtCustomerID: %s\n" % (cus_ExtCusId))
        file.write("id_Customer: %s\n" % (cus_idCus))
        file.write("Company: %s\n" % (cus_company))
        file.write("id_CompanyLocation: %s\n" % (cus_idCompanyLoc))
        file.write("Terms: %s\n" % (cus_terms))
        file.write("WebsiteURL: %s\n" % (cus_webURL))
        file.write("EmailMain: %s\n" % (cus_emailMain))
        file.write("AddressDescription: %s\n" % (cus_addressDesc))
        file.write("AddressCompany: %s\n" % (cus_addressCompany))
        file.write("Address1: %s\n" % (cus_address1))
        file.write("Address2: %s\n" % (cus_address2))
        file.write("AddressCity: %s\n" % (cus_addressCity))
        file.write("AddressState: %s\n" % (cus_addressState))
        file.write("AddressZip: %s\n" % (cus_addressZip))
        file.write("AddressCountry: %s\n" % (cus_addressCountry))
        file.write("sts_ApplySalesTax01: %s\n" % (cus_stsSalesTax1))
        file.write("sts_ApplySalesTax02: %s\n" % (cus_stsSalesTax2))
        file.write("sts_ApplySalesTax03: %s\n" % (cus_stsSalesTax3))
        file.write("sts_ApplySalesTax04: %s\n" % (cus_stsSalesTax4))
        file.write("coa_AccountSalesTax01: %s\n" % (cus_coaAccountSalesTax1))
        file.write("coa_AccountSalesTax02: %s\n" % (cus_coaAccountSalesTax2))
        file.write("coa_AccountSalesTax03: %s\n" % (cus_coaAccountSalesTax3))
        file.write("coa_AccountSalesTax04: %s\n" % (cus_coaAccountSalesTax4))
        file.write("TaxExemptNumber: %s\n" % (cus_taxExemptNumber))
        file.write("id_DiscountLevel: %s\n" % (cus_idDiscountLevel))
        file.write("id_DefaultCalculator1: %s\n" % (cus_idDefCalc1))
        file.write("id_DefaultCalculator2: %s\n" % (cus_idDefCalc2))
        file.write("CustomerServiceRep: %s\n" % (cus_cusServRep))
        file.write("CustomerType: %s\n" % (cus_cusType))
        file.write("CustomerSource: %s\n" % (cus_cusSource))
        file.write("ReferenceFrom: %s\n" % (cus_referenceFrom))
        file.write("SICCode: %s\n" % (cus_SICCode))
        file.write("SICDescription: %s\n" % (cus_SICDesc))
        file.write("n_EmployeeCount: %s\n" % (cus_nEmployeeCount))
        file.write("CustomField01: %s\n" % (cus_custom1))
        file.write("CustomField02: %s\n" % (cus_custom2))
        file.write("CustomField03: %s\n" % (cus_custom3))
        file.write("CustomField04: %s\n" % (cus_custom4))
        file.write("CustomField05: %s\n" % (cus_custom5))
        file.write("CustomField06: %s\n" % (cus_custom6))
        file.write("CustomField07: %s\n" % (cus_custom7))
        file.write("CustomField08: %s\n" % (cus_custom8))
        file.write("CustomField09: %s\n" % (cus_custom9))
        file.write("CustomField10: %s\n" % (cus_custom10))
        file.write("---- End Customer ----\n")

    def contact_block(
        self,
        file,
        contact,
        con_nameFirst="",
        con_nameLast="",
        con_department="",
        con_title="",
        con_phone="",
        con_fax="",
        con_email="",
        con_stsContactAdd="",
        con_stsEnableBulkEmail="",
    ):

        if contact == "ap":
            pass
        if contact == "webstore":
            con_nameFirst = "Webstore"
            con_phone = "800-555-5555"
            con_email = "webstore@ap.com"

        file.write("---- Start Contact ----\n")
        file.write("NameFirst: %s\n" % (con_nameFirst))
        file.write("NameLast: %s\n" % (con_nameLast))
        file.write("Department: %s\n" % (con_department))
        file.write("Title: %s\n" % (con_title))
        file.write("Phone: %s\n" % (con_phone))
        file.write("Fax: %s\n" % (con_fax))
        file.write("Email: %s\n" % (con_email))
        file.write("sts_Contact_Add: %s\n" % (con_stsContactAdd))
        file.write("sts_Enable_Bulk_Email: %s\n" % (con_stsEnableBulkEmail))
        file.write("---- End Contact ----\n")

    def design_block(self):
        pass

    def location_block(self):
        pass

    def product_block(
        self,
        file,
        prod_partNumber="",
        prob_partColorRange="",
        prob_partColor="",
        prob_curUnitPriceUserEntered="",
        prob_orderInstruct="",
        prob_size1Req="",
        prob_size2Req="",
        prob_size3Req="",
        prob_size4Req="",
        prob_size5Req="",
        prob_size6Req="",
        prob_stsProdProductOverride="",
        prob_partDescription="",
        prob_curUnitCost="",
        prob_stsEnableCommisson="",
        prob_idProductClass="",
        prob_stsProdSalesTaxOverride="",
        prob_stsEnableTax1="",
        prob_stsEnableTax2="",
        prob_stsEnableTax3="",
        prob_stsEnableTax4="",
        prob_stsProdSecondaryUnitsOverride="",
        prob_stsUseSecondaryUnits="",
        prob_unitsQty="",
        prob_unitsType="",
        prob_UnitsArea1="",
        prob_UnitsArea2="",
        prob_unitsPricing="",
        prob_stsUnitsPurchasing="",
        prob_stsUnitsPurchasingExtraPercent="",
        prob_stsUnitsPurchasingExtraRound="",
        prob_stsProdBehaviorOverride="",
        prob_stsProductSourceSupplied="",
        prob_stsProductSourcePurchase="",
        prob_stsProductSourceInventory="",
        prob_stsProductionDesigns="",
        prob_stsProductionSubcontract="",
        prob_stsProductionComponents="",
        prob_stsStorageShip="",
        prob_stsStorageInventory="",
        prob_invoicingInvoice="",
    ):
        file.write("---- Start Product ----\n")
        file.write("PartNumber: %s\n" % (prod_partNumber))
        file.write("PartColorRange: %s\n" % (prob_partColorRange))
        file.write("PartColor: %s\n" % (prob_partColor))
        file.write("cur_UnitPriceUserEntered: %s\n" % (prob_curUnitPriceUserEntered))
        file.write("OrderInstructions: %s\n" % (prob_orderInstruct))
        file.write("Size01_Req: %s\n" % (prob_size1Req))
        file.write("Size02_Req: %s\n" % (prob_size2Req))
        file.write("Size03_Req: %s\n" % (prob_size3Req))
        file.write("Size04_Req: %s\n" % (prob_size4Req))
        file.write("Size05_Req: %s\n" % (prob_size5Req))
        file.write("Size06_Req: %s\n" % (prob_size6Req))
        file.write("sts_Prod_Product_Override: %s\n" % (prob_stsProdProductOverride))
        file.write("PartDescription: %s\n" % (prob_partDescription))
        file.write("cur_UnitCost: %s\n" % (prob_curUnitCost))
        file.write("sts_EnableCommission: %s\n" % (prob_stsEnableCommisson))
        file.write("id_ProductClass: %s\n" % (prob_idProductClass))
        file.write("sts_Prod_SalesTax_Override: %s\n" % (prob_stsProdSalesTaxOverride))
        file.write("sts_EnableTax01: %s\n" % (prob_stsEnableTax1))
        file.write("sts_EnableTax02: %s\n" % (prob_stsEnableTax2))
        file.write("sts_EnableTax03: %s\n" % (prob_stsEnableTax3))
        file.write("sts_EnableTax04:  %s\n" % (prob_stsEnableTax4))
        file.write(
            "sts_Prod_SecondaryUnits_Override: %s\n"
            % (prob_stsProdSecondaryUnitsOverride)
        )
        file.write("sts_UseSecondaryUnits: %s\n" % (prob_stsUseSecondaryUnits))
        file.write("Units_Qty: %s\n" % (prob_unitsQty))
        file.write("Units_Type:  %s\n" % (prob_unitsType))
        file.write("Units_Area1: %s\n" % (prob_UnitsArea1))
        file.write("Units_Area2: %s\n" % (prob_UnitsArea2))
        file.write("sts_UnitsPricing: %s\n" % (prob_unitsPricing))
        file.write("sts_UnitsPurchasing: %s\n" % (prob_stsUnitsPurchasing))
        file.write(
            "sts_UnitsPurchasingExtraPercent: %s\n"
            % (prob_stsUnitsPurchasingExtraPercent)
        )
        file.write(
            "sts_UnitsPurchasingExtraRound: %s\n" % (prob_stsUnitsPurchasingExtraRound)
        )
        file.write("sts_Prod_Behavior_Override: %s\n" % (prob_stsProdBehaviorOverride))
        file.write("sts_ProductSource_Supplied: %s\n" % (prob_stsProductSourceSupplied))
        file.write("sts_ProductSource_Purchase: %s\n" % (prob_stsProductSourcePurchase))
        file.write(
            "sts_ProductSource_Inventory: %s\n" % (prob_stsProductSourceInventory)
        )
        file.write("sts_Production_Designs: %s\n" % (prob_stsProductionDesigns))
        file.write("sts_Production_Subcontract: %s\n" % (prob_stsProductionSubcontract))
        file.write("sts_Production_Components: %s\n" % (prob_stsProductionComponents))
        file.write("sts_Storage_Ship: %s\n" % (prob_stsStorageShip))
        file.write("sts_Storage_Inventory: %s\n" % (prob_stsStorageInventory))
        file.write("sts_Invoicing_Invoice: %s\n" % (prob_invoicingInvoice))
        file.write("---- End Product ----\n")

    def payment_block(
        self,
        file,
        payb_datePayment="",
        payb_curPayment="",
        payb_payType="",
        payb_paymentNum="",
        payb_cardNameLast="",
        payb_cardNameFirst="",
        payb_cardExpDate="",
        payb_notes="",
    ):
        file.write("---- Start Payment ----\n")
        file.write("date_Payment: %s\n" % (payb_datePayment))
        file.write("cur_Payment: %s\n" % (payb_curPayment))
        file.write("PaymentType: %s\n" % (payb_payType))
        file.write("PaymentNumber: %s\n" % (payb_paymentNum))
        file.write("Card_Name_Last: %s\n" % (payb_cardNameLast))
        file.write("Card_Name_First: %s\n" % (payb_cardNameFirst))
        file.write("Card_Exp_Date: %s\n" % (payb_cardExpDate))
        file.write("Notes: %s\n" % (payb_notes))
        file.write("---- End Payment ----\n")

    def create_array(self, x):
        filename = apcsv[x]
        fnap = os.path.join(cwd + r"\\input\\ap\\", filename)
        with open(fnap, "r") as file:
            data_iter = csv.reader(file, delimiter=",", quotechar='"')
            data = [data for data in data_iter]
        data_array = np.asarray(data, dtype=None)
        test.append(data_array)
        return data_array, filename

    def create_ap_order(self, file, data, filename):
        file.write('\n"\n')
        self.order_block(
            file,
            filename,
            data,
            ob_extOrderID=str(data[1, 0] + data[1, 3]),
            ob_orderType=str(data[1, 14]),
        )
        self.customer_block(file, customer="ap")
        self.contact_block(file, contact="ap")
        self.payment_block(file)
        self.product_block(file)
        file.write('\n"\n')

    def createfile(self):
        file = open(cwd + "\\output\\%s_%s_%s.txt" % (i.month, i.day, i.year), "w+")
        for x in range(len(apcsv)):
            data, filename = self.create_array(x)
            ots = []
            tarr = []
            for j in range(len(data[:, 14])):
                if data[j, 14] not in ots:
                    ots.append(data[j, 14])
            ots = list(set(ots))
            ots.remove("Deco Type")
            for x in ots:
                exec("%s1 = []" % (x))
                exec("tarr.append(%s1)" % (x))
                for m in range(len(data[:, :])):
                    if data[m, 14] == x:
                        exec("%s1.append(data[m,:])" % (x))
            for x in tarr:
                self.create_ap_order(file, data, filename)
        file.close()


if __name__ == "__main__":
    ime = importExcel()
    ime.import_excel_files()
    genff = Generateff()
    genff.createfile()
