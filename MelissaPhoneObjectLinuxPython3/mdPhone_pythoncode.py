from ctypes import *
from enum import Enum
import ctypes
import os
import sys

if (os.name == 'nt' and sys.version_info[:2] >= (3,8)):
  lib = ctypes.CDLL('mdPhone.dll', winmode=0)
elif (os.name == 'nt'):
  lib = ctypes.CDLL('mdPhone.dll')
else:
  lib = ctypes.CDLL('libmdPhone.so')

lib.mdPhoneCreate.argtypes = []
lib.mdPhoneCreate.restype = c_void_p
lib.mdPhoneDestroy.argtypes = [c_void_p]
lib.mdPhoneDestroy.restype = None
lib.mdPhoneInitialize.argtypes = [c_void_p, c_char_p]
lib.mdPhoneInitialize.restype = c_int
lib.mdPhoneGetInitializeErrorString.argtypes = [c_void_p]
lib.mdPhoneGetInitializeErrorString.restype = c_char_p
lib.mdPhoneSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdPhoneSetLicenseString.restype = c_bool
lib.mdPhoneGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdPhoneGetLicenseExpirationDate.restype = c_char_p
lib.mdPhoneGetBuildNumber.argtypes = [c_void_p]
lib.mdPhoneGetBuildNumber.restype = c_char_p
lib.mdPhoneGetDatabaseDate.argtypes = [c_void_p]
lib.mdPhoneGetDatabaseDate.restype = c_char_p
lib.mdPhoneLookup.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdPhoneLookup.restype = c_bool
lib.mdPhoneCorrectAreaCode.argtypes = [c_void_p, c_char_p, c_char_p]
lib.mdPhoneCorrectAreaCode.restype = c_bool
lib.mdPhoneComputeDistance.argtypes = [c_void_p, c_double, c_double, c_double, c_double]
lib.mdPhoneComputeDistance.restype = c_double
lib.mdPhoneComputeBearing.argtypes = [c_void_p, c_double, c_double, c_double, c_double]
lib.mdPhoneComputeBearing.restype = c_double
lib.mdPhoneGetAreaCode.argtypes = [c_void_p]
lib.mdPhoneGetAreaCode.restype = c_char_p
lib.mdPhoneGetNewAreaCode.argtypes = [c_void_p]
lib.mdPhoneGetNewAreaCode.restype = c_char_p
lib.mdPhoneGetPrefix.argtypes = [c_void_p]
lib.mdPhoneGetPrefix.restype = c_char_p
lib.mdPhoneGetSuffix.argtypes = [c_void_p]
lib.mdPhoneGetSuffix.restype = c_char_p
lib.mdPhoneGetExtension.argtypes = [c_void_p]
lib.mdPhoneGetExtension.restype = c_char_p
lib.mdPhoneGetCity.argtypes = [c_void_p]
lib.mdPhoneGetCity.restype = c_char_p
lib.mdPhoneGetState.argtypes = [c_void_p]
lib.mdPhoneGetState.restype = c_char_p
lib.mdPhoneGetCountyFips.argtypes = [c_void_p]
lib.mdPhoneGetCountyFips.restype = c_char_p
lib.mdPhoneGetCountyName.argtypes = [c_void_p]
lib.mdPhoneGetCountyName.restype = c_char_p
lib.mdPhoneGetMsa.argtypes = [c_void_p]
lib.mdPhoneGetMsa.restype = c_char_p
lib.mdPhoneGetPmsa.argtypes = [c_void_p]
lib.mdPhoneGetPmsa.restype = c_char_p
lib.mdPhoneGetTimeZone.argtypes = [c_void_p]
lib.mdPhoneGetTimeZone.restype = c_char_p
lib.mdPhoneGetTimeZoneCode.argtypes = [c_void_p]
lib.mdPhoneGetTimeZoneCode.restype = c_char_p
lib.mdPhoneGetCountryCode.argtypes = [c_void_p]
lib.mdPhoneGetCountryCode.restype = c_char_p
lib.mdPhoneGetLatitude.argtypes = [c_void_p]
lib.mdPhoneGetLatitude.restype = c_char_p
lib.mdPhoneGetLongitude.argtypes = [c_void_p]
lib.mdPhoneGetLongitude.restype = c_char_p
lib.mdPhoneGetDistance.argtypes = [c_void_p]
lib.mdPhoneGetDistance.restype = c_char_p
lib.mdPhoneGetResults.argtypes = [c_void_p]
lib.mdPhoneGetResults.restype = c_char_p
lib.mdPhoneGetResultCodeDescription.argtypes = [c_void_p, c_char_p, c_int]
lib.mdPhoneGetResultCodeDescription.restype = c_char_p
lib.mdPhoneGetStatusCode.argtypes = [c_void_p]
lib.mdPhoneGetStatusCode.restype = c_char_p
lib.mdPhoneGetErrorCode.argtypes = [c_void_p]
lib.mdPhoneGetErrorCode.restype = c_char_p

lib.mdGlobalPhoneCreate.argtypes = []
lib.mdGlobalPhoneCreate.restype = c_void_p
lib.mdGlobalPhoneDestroy.argtypes = [c_void_p]
lib.mdGlobalPhoneDestroy.restype = None
lib.mdGlobalPhoneInitialize.argtypes = [c_void_p, c_char_p]
lib.mdGlobalPhoneInitialize.restype = c_int
lib.mdGlobalPhoneGetInitializeErrorString.argtypes = [c_void_p]
lib.mdGlobalPhoneGetInitializeErrorString.restype = c_char_p
lib.mdGlobalPhoneSetLicenseString.argtypes = [c_void_p, c_char_p]
lib.mdGlobalPhoneSetLicenseString.restype = c_bool
lib.mdGlobalPhoneGetLicenseExpirationDate.argtypes = [c_void_p]
lib.mdGlobalPhoneGetLicenseExpirationDate.restype = c_char_p
lib.mdGlobalPhoneGetBuildNumber.argtypes = [c_void_p]
lib.mdGlobalPhoneGetBuildNumber.restype = c_char_p
lib.mdGlobalPhoneGetDatabaseDate.argtypes = [c_void_p]
lib.mdGlobalPhoneGetDatabaseDate.restype = c_char_p
lib.mdGlobalPhoneLookup.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p]
lib.mdGlobalPhoneLookup.restype = c_bool
lib.mdGlobalPhoneLookupNext.argtypes = [c_void_p]
lib.mdGlobalPhoneLookupNext.restype = c_bool
lib.mdGlobalPhoneGetPhoneNumber.argtypes = [c_void_p]
lib.mdGlobalPhoneGetPhoneNumber.restype = c_char_p
lib.mdGlobalPhoneGetSubscriberNumber.argtypes = [c_void_p]
lib.mdGlobalPhoneGetSubscriberNumber.restype = c_char_p
lib.mdGlobalPhoneGetCountry.argtypes = [c_void_p]
lib.mdGlobalPhoneGetCountry.restype = c_char_p
lib.mdGlobalPhoneGetCountryCode.argtypes = [c_void_p]
lib.mdGlobalPhoneGetCountryCode.restype = c_char_p
lib.mdGlobalPhoneGetInternationalPrefix.argtypes = [c_void_p]
lib.mdGlobalPhoneGetInternationalPrefix.restype = c_char_p
lib.mdGlobalPhoneGetNationPrefix.argtypes = [c_void_p]
lib.mdGlobalPhoneGetNationPrefix.restype = c_char_p
lib.mdGlobalPhoneGetNationalDestinationCode.argtypes = [c_void_p]
lib.mdGlobalPhoneGetNationalDestinationCode.restype = c_char_p
lib.mdGlobalPhoneGetLanguage.argtypes = [c_void_p]
lib.mdGlobalPhoneGetLanguage.restype = c_char_p
lib.mdGlobalPhoneGetAdministrativeArea.argtypes = [c_void_p]
lib.mdGlobalPhoneGetAdministrativeArea.restype = c_char_p
lib.mdGlobalPhoneGetLocality.argtypes = [c_void_p]
lib.mdGlobalPhoneGetLocality.restype = c_char_p
lib.mdGlobalPhoneGetUTC.argtypes = [c_void_p]
lib.mdGlobalPhoneGetUTC.restype = c_char_p
lib.mdGlobalPhoneGetDST.argtypes = [c_void_p]
lib.mdGlobalPhoneGetDST.restype = c_char_p
lib.mdGlobalPhoneGetLatitude.argtypes = [c_void_p]
lib.mdGlobalPhoneGetLatitude.restype = c_char_p
lib.mdGlobalPhoneGetLongitude.argtypes = [c_void_p]
lib.mdGlobalPhoneGetLongitude.restype = c_char_p
lib.mdGlobalPhoneGetResults.argtypes = [c_void_p]
lib.mdGlobalPhoneGetResults.restype = c_char_p
lib.mdGlobalPhoneGetResultCodeDescription.argtypes = [c_void_p, c_char_p, c_int]
lib.mdGlobalPhoneGetResultCodeDescription.restype = c_char_p

# mdPhone Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorOther = 1
	ErrorOutOfMemory = 2
	ErrorRequiredFileNotFound = 3
	ErrorFoundOldFile = 4
	ErrorDatabaseExpired = 5
	ErrorLicenseExpired = 6

class AccessType(Enum):
	Local = 0
	Remote = 1

class DiacriticsMode(Enum):
	Auto = 0
	On = 1
	Off = 2

class StandardizeMode(Enum):
	ShortFormat = 0
	LongFormat = 1
	AutoFormat = 2

class SuiteParseMode(Enum):
	ParseSuite = 0
	CombineSuite = 1

class AliasPreserveMode(Enum):
	ConvertAlias = 0
	PreserveAlias = 1

class AutoCompletionMode(Enum):
	AutoCompleteSingleSuite = 0
	AutoCompleteRangedSuite = 1
	AutoCompletePlaceHolderSuite = 2
	AutoCompleteNoSuite = 3

class ResultCdDescOpt(Enum):
	ResultCodeDescriptionLong = 0
	ResultCodeDescriptionShort = 1

class MailboxLookupMode(Enum):
	MailboxNone = 0
	MailboxExpress = 1
	MailboxPremium = 2

class mdPhone(object):
	def __init__(self):
		self.I = lib.mdPhoneCreate()

	def __del__(self):
		lib.mdPhoneDestroy(self.I)

	def Initialize(self, p1):
		return ProgramStatus(lib.mdPhoneInitialize(self.I, p1.encode('utf-8')))

	def GetInitializeErrorString(self):
		return lib.mdPhoneGetInitializeErrorString(self.I).decode('utf-8')

	def SetLicenseString(self, p1):
		return lib.mdPhoneSetLicenseString(self.I, p1.encode('utf-8'))

	def GetLicenseExpirationDate(self):
		return lib.mdPhoneGetLicenseExpirationDate(self.I).decode('utf-8')

	def GetBuildNumber(self):
		return lib.mdPhoneGetBuildNumber(self.I).decode('utf-8')

	def GetDatabaseDate(self):
		return lib.mdPhoneGetDatabaseDate(self.I).decode('utf-8')

	def Lookup(self, phone, zip=""):
		return lib.mdPhoneLookup(self.I, phone.encode('utf-8'), zip.encode('utf-8'))

	def CorrectAreaCode(self, phone, zip):
		return lib.mdPhoneCorrectAreaCode(self.I, phone.encode('utf-8'), zip.encode('utf-8'))

	def ComputeDistance(self, p1, p2, p3, p4):
		return lib.mdPhoneComputeDistance(self.I)

	def ComputeBearing(self, p1, p2, p3, p4):
		return lib.mdPhoneComputeBearing(self.I)

	def GetAreaCode(self):
		return lib.mdPhoneGetAreaCode(self.I).decode('utf-8')

	def GetNewAreaCode(self):
		return lib.mdPhoneGetNewAreaCode(self.I).decode('utf-8')

	def GetPrefix(self):
		return lib.mdPhoneGetPrefix(self.I).decode('utf-8')

	def GetSuffix(self):
		return lib.mdPhoneGetSuffix(self.I).decode('utf-8')

	def GetExtension(self):
		return lib.mdPhoneGetExtension(self.I).decode('utf-8')

	def GetCity(self):
		return lib.mdPhoneGetCity(self.I).decode('utf-8')

	def GetState(self):
		return lib.mdPhoneGetState(self.I).decode('utf-8')

	def GetCountyFips(self):
		return lib.mdPhoneGetCountyFips(self.I).decode('utf-8')

	def GetCountyName(self):
		return lib.mdPhoneGetCountyName(self.I).decode('utf-8')

	def GetMsa(self):
		return lib.mdPhoneGetMsa(self.I).decode('utf-8')

	def GetPmsa(self):
		return lib.mdPhoneGetPmsa(self.I).decode('utf-8')

	def GetTimeZone(self):
		return lib.mdPhoneGetTimeZone(self.I).decode('utf-8')

	def GetTimeZoneCode(self):
		return lib.mdPhoneGetTimeZoneCode(self.I).decode('utf-8')

	def GetCountryCode(self):
		return lib.mdPhoneGetCountryCode(self.I).decode('utf-8')

	def GetLatitude(self):
		return lib.mdPhoneGetLatitude(self.I).decode('utf-8')

	def GetLongitude(self):
		return lib.mdPhoneGetLongitude(self.I).decode('utf-8')

	def GetDistance(self):
		return lib.mdPhoneGetDistance(self.I).decode('utf-8')

	def GetResults(self):
		return lib.mdPhoneGetResults(self.I).decode('utf-8')

	def GetResultCodeDescription(self, resultCode, opt=0):
		return lib.mdPhoneGetResultCodeDescription(self.I, resultCode.encode('utf-8'), ResultCdDescOpt(opt).value).decode('utf-8')

	def GetStatusCode(self):
		return lib.mdPhoneGetStatusCode(self.I).decode('utf-8')

	def GetErrorCode(self):
		return lib.mdPhoneGetErrorCode(self.I).decode('utf-8')

# mdGlobalPhone Enumerations
class ProgramStatus(Enum):
	ErrorNone = 0
	ErrorOther = 1
	ErrorOutOfMemory = 2
	ErrorRequiredFileNotFound = 3
	ErrorFoundOldFile = 4
	ErrorDatabaseExpired = 5
	ErrorLicenseExpired = 6

class AccessType(Enum):
	Local = 0
	Remote = 1

class DiacriticsMode(Enum):
	Auto = 0
	On = 1
	Off = 2

class StandardizeMode(Enum):
	ShortFormat = 0
	LongFormat = 1
	AutoFormat = 2

class SuiteParseMode(Enum):
	ParseSuite = 0
	CombineSuite = 1

class AliasPreserveMode(Enum):
	ConvertAlias = 0
	PreserveAlias = 1

class AutoCompletionMode(Enum):
	AutoCompleteSingleSuite = 0
	AutoCompleteRangedSuite = 1
	AutoCompletePlaceHolderSuite = 2
	AutoCompleteNoSuite = 3

class ResultCdDescOpt(Enum):
	ResultCodeDescriptionLong = 0
	ResultCodeDescriptionShort = 1

class MailboxLookupMode(Enum):
	MailboxNone = 0
	MailboxExpress = 1
	MailboxPremium = 2

class mdGlobalPhone(object):
	def __init__(self):
		self.I = lib.mdGlobalPhoneCreate()

	def __del__(self):
		lib.mdGlobalPhoneDestroy(self.I)

	def Initialize(self, p1):
		return ProgramStatus(lib.mdGlobalPhoneInitialize(self.I, p1.encode('utf-8')))

	def GetInitializeErrorString(self):
		return lib.mdGlobalPhoneGetInitializeErrorString(self.I).decode('utf-8')

	def SetLicenseString(self, p1):
		return lib.mdGlobalPhoneSetLicenseString(self.I, p1.encode('utf-8'))

	def GetLicenseExpirationDate(self):
		return lib.mdGlobalPhoneGetLicenseExpirationDate(self.I).decode('utf-8')

	def GetBuildNumber(self):
		return lib.mdGlobalPhoneGetBuildNumber(self.I).decode('utf-8')

	def GetDatabaseDate(self):
		return lib.mdGlobalPhoneGetDatabaseDate(self.I).decode('utf-8')

	def Lookup(self, phone, country="", origcountry=""):
		return lib.mdGlobalPhoneLookup(self.I, phone.encode('utf-8'), country.encode('utf-8'), origcountry.encode('utf-8'))

	def LookupNext(self):
		return lib.mdGlobalPhoneLookupNext(self.I)

	def GetPhoneNumber(self):
		return lib.mdGlobalPhoneGetPhoneNumber(self.I).decode('utf-8')

	def GetSubscriberNumber(self):
		return lib.mdGlobalPhoneGetSubscriberNumber(self.I).decode('utf-8')

	def GetCountry(self):
		return lib.mdGlobalPhoneGetCountry(self.I).decode('utf-8')

	def GetCountryCode(self):
		return lib.mdGlobalPhoneGetCountryCode(self.I).decode('utf-8')

	def GetInternationalPrefix(self):
		return lib.mdGlobalPhoneGetInternationalPrefix(self.I).decode('utf-8')

	def GetNationPrefix(self):
		return lib.mdGlobalPhoneGetNationPrefix(self.I).decode('utf-8')

	def GetNationalDestinationCode(self):
		return lib.mdGlobalPhoneGetNationalDestinationCode(self.I).decode('utf-8')

	def GetLanguage(self):
		return lib.mdGlobalPhoneGetLanguage(self.I).decode('utf-8')

	def GetAdministrativeArea(self):
		return lib.mdGlobalPhoneGetAdministrativeArea(self.I).decode('utf-8')

	def GetLocality(self):
		return lib.mdGlobalPhoneGetLocality(self.I).decode('utf-8')

	def GetUTC(self):
		return lib.mdGlobalPhoneGetUTC(self.I).decode('utf-8')

	def GetDST(self):
		return lib.mdGlobalPhoneGetDST(self.I).decode('utf-8')

	def GetLatitude(self):
		return lib.mdGlobalPhoneGetLatitude(self.I).decode('utf-8')

	def GetLongitude(self):
		return lib.mdGlobalPhoneGetLongitude(self.I).decode('utf-8')

	def GetResults(self):
		return lib.mdGlobalPhoneGetResults(self.I).decode('utf-8')

	def GetResultCodeDescription(self, resultCode, opt=0):
		return lib.mdGlobalPhoneGetResultCodeDescription(self.I, resultCode.encode('utf-8'), ResultCdDescOpt(opt).value).decode('utf-8')
