#NaN values
NA_Value = -1


# Default value in hours between Singapore (UTC+ 8) and Libson (UTC-1)
UTC_LAG_BETWEEN_SG_AND_LIBSON = 0 #hours


# Name of the training file
TRAIN_CSV_FILE_NAME = "data/train.csv"

# Name of the testing file
TEST_CSV_FILE_NAME = "data/test.csv"

# Max speed limit in km/h before discarding the row
MAX_SPEED_LIMIT_BEFORE_DISCARDING = 130

# Max duration for a drive (in seconds)
MAX_DURATION_BEFORE_DISCARDING = 3600 * 2 #thats 2 hours


# Poly files
LAT_ID = 0
LONG_ID = 1

TAXI_ID = 'TAXI_ID'
ORIGIN_CALL = 'ORIGIN_CALL'
ORIGIN_STAND = 'ORIGIN_STAND'
DAY_TYPE = 'DAY_TYPE'
CALL_TYPE = 'CALL_TYPE'
TRIP_ID = 'TRIP_ID'
POLYLINE = 'POLYLINE'
MISSING_DATA = 'MISSING_DATA'
TIMESTAMP = 'TIMESTAMP'
SPEED = 'SPEED'
LAST_SPEED = 'LAST_SPEED'
LAST_LAST_SPEED = 'LAST_LAST_SPEED'
DURATION = 'DURATION'
