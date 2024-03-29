#!/bin/bash

# Name:    MelissaPhoneObjectLinuxPython3
# Purpose: Use the Melissa Updater to make the MelissaPhoneObjectLinuxPython3 code usable

######################### Constants ##########################

RED='\033[0;31m' #RED
NC='\033[0m' # No Color

######################### Parameters ##########################

phone=""
license=""
quiet="false"

while [ $# -gt 0 ] ; do
  case $1 in
    -p | --phone) 
        phone="$2"
        
        if [ "$phone" == "-l" ] || [ "$phone" == "--license" ] || [ "$phone" == "-q" ] || [ "$phone" == "--quiet" ] || [ -z "$phone" ];
        then
            printf "${RED}Error: Missing an argument for parameter \'phone\'.${NC}\n"  
            exit 1
        fi 
        ;;
    -l | --license) 
        license="$2"
        
        if [ "$license" == "-q" ] || [ "$license" == "--quiet" ] || [ "$license" == "-p" ] || [ "$license" == "--phone" ] || [ -z "$license" ];
        then
            printf "${RED}Error: Missing an argument for parameter \'license\'.${NC}\n"  
            exit 1
        fi  
        ;;
    -q | --quiet) 
        quiet="true" 
        ;;
  esac
  shift
done

# ######################### Config ###########################
RELEASE_VERSION='2024.03'
ProductName="DQ_PHONE_DATA"

# Uses the location of the .sh file 
CurrentPath=$(pwd)
ProjectPath="$CurrentPath/MelissaPhoneObjectLinuxPython3"

DataPath="$ProjectPath/Data" # To use your own data file(s), change to your DQS release data file(s) directory
if [ ! -d "$DataPath" ] && [ "$DataPath" = "$ProjectPath/Data" ]; 
then
  mkdir -p "$DataPath"
fi

# Config variables for download file(s)
Config_FileName="libmdPhone.so"
Config_ReleaseVersion=$RELEASE_VERSION
Config_OS="LINUX"
Config_Compiler="GCC48"
Config_Architecture="64BIT"
Config_Type="BINARY"

Wrapper_FileName="mdPhone_pythoncode.py"
Wrapper_ReleaseVersion=$RELEASE_VERSION
Wrapper_OS="ANY"
Wrapper_Compiler="PYTHON"
Wrapper_Architecture="ANY"
Wrapper_Type="INTERFACE"

# ######################## Functions #########################
DownloadDataFiles()
{
    printf "========================== MELISSA UPDATER =========================\n"
    printf "MELISSA UPDATER IS DOWNLOADING DATA FILE(S)...\n"

    ./MelissaUpdater/MelissaUpdater manifest -p $ProductName -r $RELEASE_VERSION -l $1 -t $DataPath 

    if [ $? -ne 0 ];
    then
        printf "\nCannot run Melissa Updater. Please check your license string!\n"
        exit 1
    fi     
    
    printf "Melissa Updater finished downloading data file(s)!\n"
}

DownloadSO() 
{
    printf "\nMELISSA UPDATER IS DOWNLOADING SO(S)...\n"
    
    # Check for quiet mode
    if [ $quiet == "true" ];
    then
        ./MelissaUpdater/MelissaUpdater file --filename $Config_FileName --release_version $Config_ReleaseVersion --license $1 --os $Config_OS --compiler $Config_Compiler --architecture $Config_Architecture --type $Config_Type --target_directory $ProjectPath &> /dev/null
        if [ $? -ne 0 ];
        then
            printf "\nCannot run Melissa Updater. Please check your license string!\n"
            exit 1
        fi
    else
        ./MelissaUpdater/MelissaUpdater file --filename $Config_FileName --release_version $Config_ReleaseVersion --license $1 --os $Config_OS --compiler $Config_Compiler --architecture $Config_Architecture --type $Config_Type --target_directory $ProjectPath 
        if [ $? -ne 0 ];
        then
            printf "\nCannot run Melissa Updater. Please check your license string!\n"
            exit 1
        fi
    fi
    
    printf "Melissa Updater finished downloading $Config_FileName!\n"
}

DownloadWrapper() 
{
    printf "\nMELISSA UPDATER IS DOWNLOADING WRAPPER(S)...\n"
    
    # Check for quiet mode
    if [ $quiet == "true" ];
    then
        ./MelissaUpdater/MelissaUpdater file --filename $Wrapper_FileName --release_version $Wrapper_ReleaseVersion --license $1 --os $Wrapper_OS --compiler $Wrapper_Compiler --architecture $Wrapper_Architecture --type $Wrapper_Type --target_directory $ProjectPath &> /dev/null
        if [ $? -ne 0 ];
        then
            printf "\nCannot run Melissa Updater. Please check your license string!\n"
            exit 1
        fi
    else
        ./MelissaUpdater/MelissaUpdater file --filename $Wrapper_FileName --release_version $Wrapper_ReleaseVersion --license $1 --os $Wrapper_OS --compiler $Wrapper_Compiler --architecture $Wrapper_Architecture --type $Wrapper_Type --target_directory $ProjectPath 
        if [ $? -ne 0 ];
        then
            printf "\nCannot run Melissa Updater. Please check your license string!\n"
            exit 1
        fi
    fi
    
    printf "Melissa Updater finished downloading $Wrapper_FileName!\n"
}

CheckSOs() 
{
    if [ ! -f $ProjectPath/$Config_FileName ];
    then
        echo "false"
    else
        echo "true"
    fi
}

########################## Main ############################
printf "\n====================== Melissa Phone Object ========================\n                    [ Python3 | Linux | 64BIT ]\n"

# Get license (either from parameters or user input)
if [ -z "$license" ];
then
  printf "Please enter your license string: "
  read license
fi

# Check license from Environment Variables 
if [ -z "$license" ];
then
  license=`echo $MD_LICENSE` 
fi

if [ -z "$license" ];
then
  printf "\nLicense String is invalid!\n"
  exit 1
fi

# Use Melissa Updater to download data file(s) 
# Download data file(s) 
DownloadDataFiles $license # Comment out this line if using own DQS release

# Download SO(s)
DownloadSO $license 

# Download wrapper(s)
DownloadWrapper $license

# Check if all SO(s) have been downloaded. Exit script if missing
printf "\nDouble checking SO file(s) were downloaded...\n"

SOsAreDownloaded=$(CheckSOs)

if [ "$SOsAreDownloaded" == "false" ];
then
    printf "\n$Config_FileName not found"
    printf "\nMissing the above data file(s).  Please check that your license string and directory are correct.\n"

    printf "\nAborting program, see above.\n"
    exit 1
fi

printf "\nAll file(s) have been downloaded/updated!\n"

# Start
# Run project
if [ -z "$phone" ];
then
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./MelissaPhoneObjectLinuxPython3
    python3 $ProjectPath/MelissaPhoneObjectLinuxPython3.py --license $license  --dataPath $DataPath
else
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./MelissaPhoneObjectLinuxPython3
    python3 $ProjectPath/MelissaPhoneObjectLinuxPython3.py --license $license  --dataPath $DataPath --phone "$phone"
fi
