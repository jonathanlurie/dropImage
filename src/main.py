'''
BLANK_PY
=============
Copyright (c) 2015, Jonathan LURIE, All rights reserved.
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public
License along with this library.
'''

import os
import os.path
import datetime
from SettingFileReader import *

import dropbox


# ask the user to go to some webpage to get a new token
def getNewAccessToken():

    # loading a setting from the setting file
    settings = SettingFileReader()
    appkey = settings.getSetting("dropbox", "appkey")
    appsecret = settings.getSetting("dropbox", "appsecret")

    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(appkey, appsecret)

    # Have the user sign in and authorize this token
    authorize_url = flow.start()
    print '\n1. Go to: ' + authorize_url
    print '2. Click "Allow" (you might have to log in first)'
    print '3. Copy the authorization code.'
    code = raw_input("Enter the authorization code here: ").strip()

    #jump line
    print("")

    # This will fail if the user enters an invalid authorization code
    access_token, user_id = flow.finish(code)

    return access_token



# uplaod a file to Dropbox
# dbRelativeUrl will be a subfolder of the main Dropbox App folder
def uploadFile(client, localUrl, dbRelativeUrl):
    print("\n\tUploading file...")

    # measuring time t0
    t0 = datetime.datetime.now()

    f = open(localUrl, 'rb')
    response = client.put_file(dbRelativeUrl, f)

    # measuring time t1
    t1 = datetime.datetime.now()
    tElapsed = t1 - t0
    nbSec = tElapsed.total_seconds()

    if(response):
        #print "uploaded:", response
        print("\tUploading DONE (" + str(nbSec) + "s)")


# Ask Dropbox to share the file with a link,
# and return the link as a string
def getRawLink(client, dbRelativeUrl):
    shareInfo = client.share(dbRelativeUrl, short_url=False)

    rawLink = shareInfo["url"] + "&raw=1"
    return rawLink


# main
if __name__ == '__main__':

    # cleaning terminal + intro
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n--------------------------- DropImage -----------------------------------------\n")


    # reads parameters from settings.ini
    # loading a setting from the setting file
    settings = SettingFileReader()

    # reads the access token
    access_token = settings.getSetting("dropbox", "accessToken")


    # verify if the access token is still valid, if not, generate new one
    tokenIsValid = False

    while(not tokenIsValid):
        try:

            client = dropbox.client.DropboxClient(access_token)
            #print 'linked account: ', client.account_info()
            print("Connected to Dropbox as " + client.account_info()["display_name"] )
            tokenIsValid = True

        except:
            print "The access token is not valid anymore, generate another one"
            access_token = getNewAccessToken()

            # update the token within the setting file
            settings.setSetting( "dropbox", "accessToken", access_token)



    # loop to drop images
    quit = False
    while(not quit):

        fileAddress = raw_input('\nInput a local file address, or leave blank to quit :\n> ').strip()

        # nothing was on the input
        if(not fileAddress):
            quit = True
        else:
            # a file address was input, lets test it
            ## the file does exist locally
            if(os.path.isfile(fileAddress)):
                # the file will be placed on a subfolder system matching
                # the current year/month/day
                todayFolder = datetime.date.today().strftime('%Y/%m/%d')
                dbRelativeUrl = "/images/" + todayFolder + "/" + os.path.basename(fileAddress)

                # uplading the file to Dropbox
                uploadFile(client, fileAddress, dbRelativeUrl)

                # share, getting the link of the raw file
                rawLink = getRawLink(client, dbRelativeUrl)

                print("\n\tThe link to the raw file is:")
                print("\t" + rawLink)


            ## the file does not exit
            else:
                print("\n\tERROR : the local file:")
                print("\t" + fileAddress)
                print("\tdoes not exist!")





    exit()
