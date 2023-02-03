# Pi-Temp-Humidity

Some code to read a temperature and humidity sensor from a raspberry pi and store it on my SRCF server

Plan/Sections:
 - Data collection on raspberry pi
 - Data transfer from raspberry pi to SRCF
 - Online plot on SRCF website
 
Raspberry Pi Data structure:
```
LOCAL
    |
    |--> current_data.csv
    |      - this will be the file that the pi writes current readings to
    |
    |--> LOCAL_ARCHIVE
    |    | - where back issues of current_data.csv will be stored
    |    | - files will be named by date time start/stop e.g.:
    |    |
    |    |--> 2023-01-13-18-54-21_2023-01-13-20-17-06.csv
    |    |--> 2023-01-13-20-17-07_2023-01-13-22-21-35.csv
