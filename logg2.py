import logging


logging.basicConfig(filename = "errors.log", level = logging.WARNING, format = "%(asctime)s - %(levelname)s - %(message)s")
                                # we are using level = warning, so it will print only the warning and higher loggs only
                                            
logging.info("program started")
logging.error("Invalid value in row 13")
logging.critical("The input data is Invalid")



#Logging is used in large data sets 
# if we have 1000 rows in a file we can not check everything manually
# by using logging the row with errors are recorded and logged
# so after the compling we can go back and resolve it and pipelines are not stopped


#THEIR ARE 5 LEVELS OF LOGGING
# DEBUD < INFO < WARNING < ERROR < CRITICAL
# DEBUG = Details 
# INFO  = Normal message
# WARNING = Something unexpected
# ERROR  = Serious issue
# CRITICAL = Very Serious