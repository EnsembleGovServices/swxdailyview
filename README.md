# SWx Daily View
## End-points list & its meaning

In SWx Daily View we have main 3 modules

1. KP Forecast Data

2. Goes Proton Flux Data

3. Latitude Index Data

## NOTE
    Before using any endpoint we have one request query parameter

    named as time_stamp

    time_stamp --> The Unix epoch (or Unix time or POSIX time or Unix timestamp) is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT)
    
    for example: 
    time_stamp: 1665464364
    which is based on location and time_zone

    {
        "countryCode": "US",
        "countryName": "United States",
        "zoneName": "America/Anchorage",
        "gmtOffset": -28800,
        "timestamp": 1665464364
    }

    human redable conversion as below:

    for time_stamp: 1665464364

    Supports Unix timestamps in seconds, milliseconds, microseconds and nanoseconds.
    Assuming that this timestamp is in seconds:
    GMT: Tuesday, 11 October 2022 04:59:24
    Your time zone: Tuesday, 11 October 2022 10:29:24 GMT+05:30
    Relative: 8 hours ago

**In 1. Kp forecast data:**

We have 3 endpoints
1. /current-kp-index
2. /get-interval-kp-data
3. /predicted-kp-index

/current-kp-index

--> This will return today's current kp index in which we get the today's from 00:00 to 23:59 kp rates according
to the desired time_stamp,we count all the occurrence then returns the maximum occurrence of kp_index as an output


/get-interval-kp-data

--> This will be going to return the interval kp_index rates and the intervals must be [00-03,03-06,06-09,09-12,12-15,15-18,18-21,21-00] with their respective kp_index and noaa_scale values

/predicted-kp-index

--> This end-point will return the highest predicted kp_index for the next 3 days from the desired date with its respective noaa_scale value.

**In 2. Goes Proton Flux Data**

We have 1 endpoint

/get-proton-flux-data

--> which gives the proton flux data in 4 major intervals

1. 6 hours
2. 1 day
3. 3 days
4. 7 days

with 3 respective groups gt_10, gt_50 and gt_100 with their time_tag and flux values.


**In 3. Latitude Index Data**

We have 2 endpoints

1. /get-mid-latitude
2. /get-high-latitude

Both endpoint will return noaa_scale prediction percentage

categories are divided as below

{


"minor": G1 --> >5 kp_index,

"moderate": G2 --> >6 kp_index,

"strong": G3 --> >7 kp_index,

"severe": G4 --> >8 kp_index,

"extreme": G5 --> >9 kp_index

}






