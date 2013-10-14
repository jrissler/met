#################################################################
# MET v2 Metadate Explorer Tool
#
# This Software is Open Source. See License: https://github.com/TERENA/met/blob/master/LICENSE.md
# Copyright (c) 2012, TERENA All rights reserved.
#
# This Software is based on MET v1 developed for TERENA by Yaco Sistemas, http://www.yaco.es/
# MET v2 was developed for TERENA by Tamim Ziai, DAASI International GmbH, http://www.daasi.de
#########################################################################################

'''
Created on Sep 19, 2013

@author: tamim
'''
import sys, os
import logging.config
from optparse import OptionParser

from django.core import management;import met.settings as settings;management.setup_environ(settings)
from met.metadataparser.refresh_metadata import refresh

class RefreshMetaData:

    def process(self, options):
        logger = None
        log_config = options.log
        
        if log_config:
        
            logging.config.fileConfig(log_config)
            logger = logging.getLogger("Refresh")
    
        refresh(logger)


def commandlineCall(argv, ConvertClass=RefreshMetaData):

    optParser = OptionParser()
    optParser.set_usage("refresh [--log  <file>")
    
    optParser.add_option(
        "-l",
        "--log",
        type="string",
        dest="log",
        help="The logger configuration file",
        default=None,
        metavar="LOG")


    (options, args) = optParser.parse_args()
    
    errorMessage = ""
    
    if options.log and not os.path.exists(options.log):
        errorMessage = "File '%s' does not exist." % options.log
    
    if errorMessage:
        print errorMessage
        print optParser.get_usage()
        exit (1)
    
    objConvert = ConvertClass()
    objConvert.process(options)


if __name__ == '__main__':

    commandlineCall(sys.argv)