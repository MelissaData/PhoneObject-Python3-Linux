import mdPhone_pythoncode
import os
import sys
import json


class DataContainer:
    def __init__(self, phone="", zip_code="", result_codes=[]):
        self.phone = phone
        self.zip_code = zip_code
        self.result_codes = result_codes

class PhoneObject:
    """ Set license string and set path to data files  (.dat, etc) """
    def __init__(self, license, data_path):
        self.md_phone_obj = mdPhone_pythoncode.mdPhone()
        self.md_phone_obj.SetLicenseString(license)
        self.data_path = data_path

        """
        If you see a different date than expected, check your license string and either download the new data files or use the Melissa Updater program to update your data files.
        """

        p_status = self.md_phone_obj.Initialize(data_path)
        if (p_status != mdPhone_pythoncode.ProgramStatus.ErrorNone):
            print("Failed to Initialize Object.")
            print(p_status)
            return
        
        print(f"                DataBase Date: {self.md_phone_obj.GetDatabaseDate()}")
        print(f"              Expiration Date: {self.md_phone_obj.GetLicenseExpirationDate()}")
      
        """
        This number should match with file properties of the Melissa Object binary file.
        If TEST appears with the build number, there may be a license key issue.
        """
        print(f"               Object Version: {self.md_phone_obj.GetBuildNumber()}\n")
    

    def execute_object_and_result_codes(self, data):
        self.md_phone_obj.Lookup(data.phone, data.zip_code)
        result_codes = self.md_phone_obj.GetResults()

        """ 
        ResultsCodes explain any issues Phone Object has with the object.
        List of result codes for Phone Object
        https://wiki.melissadata.com/?title=Result_Code_Details#Phone_Object
        """

        return DataContainer(data.phone, data.zip_code, result_codes)


def parse_arguments():
    license, test_phone, data_path = "", "", ""

    args = sys.argv
    index = 0
    for arg in args:
        
        if (arg == "--license") or (arg == "-l"):
            if (args[index+1] != None):
                license = args[index+1]
        if (arg == "--phone") or (arg == "-p"):
            if (args[index+1] != None):
                test_phone = args[index+1]
        if (arg == "--dataPath") or (arg == "-d"):
            if (args[index+1] != None):
                data_path = args[index+1]
        index += 1

    return (license, test_phone, data_path)

def run_as_console(license, test_phone, data_path):
    print("\n\n========== WELCOME TO MELISSA PHONE OBJECT LINUX PYTHON3 ===========\n")

    phone_object = PhoneObject(license, data_path)

    should_continue_running = True

    if phone_object.md_phone_obj.GetInitializeErrorString() != "No error":
      should_continue_running = False
      
    while should_continue_running:
        if test_phone == None or test_phone == "":        
          print("\nFill in each value to see the Phone Object results")
          phone = str(input("Phone: "))
        else:        
          phone = test_phone
        
        data = DataContainer(phone)

        """ Print user input """
        print("\n============================== INPUTS ==============================\n")
        print(f"\t               Phone: {phone}")

        """ Execute Phone Object """
        data_container = phone_object.execute_object_and_result_codes(data)

        """ Print output """
        print("\n============================== OUTPUT ==============================\n")
        print("\n\tPhone Object Information:")

        print(f"\t     Area Code: {phone_object.md_phone_obj.GetAreaCode()}")
        print(f"\t        Prefix: {phone_object.md_phone_obj.GetPrefix()}")
        print(f"\t        Suffix: {phone_object.md_phone_obj.GetSuffix()}")
        print(f"\t          City: {phone_object.md_phone_obj.GetCity()}")
        print(f"\t         State: {phone_object.md_phone_obj.GetState()}")
        print(f"\t      Latitude: {phone_object.md_phone_obj.GetLatitude()}")
        print(f"\t     Longitude: {phone_object.md_phone_obj.GetLongitude()}")
        print(f"\t     Time Zone: {phone_object.md_phone_obj.GetTimeZone()}")
        print(f"\t  Result Codes: {data_container.result_codes}")

        # print(f"\t New Area Code: {phone_object.md_phone_obj.GetNewAreaCode()}")
        # print(f"\t     Extension: {phone_object.md_phone_obj.GetExtension()}")
        # print(f"\t    CountyFips: {phone_object.md_phone_obj.GetCountyFips()}")
        # print(f"\t    CountyName: {phone_object.md_phone_obj.GetCountyName()}")
        # print(f"\t           Msa: {phone_object.md_phone_obj.GetMsa()}")
        # print(f"\t          Pmsa: {phone_object.md_phone_obj.GetPmsa()}")
        # print(f"\tTime Zone Code: {phone_object.md_phone_obj.GetTimeZoneCode()}")
        # print(f"\t  Country Code: {phone_object.md_phone_obj.GetCountryCode()}")
        # print(f"\t      Distance: {phone_object.md_phone_obj.GetDistance()}")


        rs = data_container.result_codes.split(',')
        for r in rs:
            print(f"        {r}: {phone_object.md_phone_obj.GetResultCodeDescription(r, mdPhone_pythoncode.ResultCdDescOpt.ResultCodeDescriptionLong)}")


        is_valid = False
        if not (test_phone == None or test_phone == ""):
            is_valid = True
            should_continue_running = False    
        while not is_valid:
        
            test_another_response = input(str("\nTest another phone? (Y/N)\n"))
            

            if not (test_another_response == None or test_another_response == ""):         
                test_another_response = test_another_response.lower()
            if test_another_response == "y":
                is_valid = True
            
            elif test_another_response == "n":
                is_valid = True
                should_continue_running = False            
            else:
            
              print("Invalid Response, please respond 'Y' or 'N'")

    print("\n============= THANK YOU FOR USING MELISSA PYTHON3 OBJECT ===========\n")
    


"""  MAIN STARTS HERE   """

license, test_phone, data_path = parse_arguments()

run_as_console(license, test_phone, data_path)