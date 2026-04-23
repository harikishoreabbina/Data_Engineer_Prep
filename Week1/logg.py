# LOGGING
# Logging is giving the useful messages about what the scriot is doing and what went wrong
# insted of print we use logging to track what is going on

import logging  # importing logging module

logging.basicConfig(filename = "app.log", level = logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
#  basicConfig is used to set the file name and log level
# here app.log is our file name and the message goes to app.log
# level = logging.ERROR , error messages are recorded
logging.error("Invalid row found") # this gives this message into log file

