python-3.6.5
import requests
import json

url = "https://api.ciscospark.com/v1"
api_call ="/people"
print("welcome, this script will allow you to delete multiple Webex Teams users by entering their email addresses")
print("This script will not ask for any confirmation before deleting the users. USE IT WITH CAUTION. deleted users CANNOT be retrieved and all deleted data is gone for good")
#script version
print("version 1 - May 24, 2018")
print("author : Bertrand PESLE")
#Gathering your access token that has the rights to delete users from the organization you want to delete users to
access_token = input("Enter your full-admin token : ")
#transforming the emails list to a python list
emails_input = input("Entrez les adresses emails à supprimer séparées par ; et sans espaces : ")  
liste_emails_input = emails_input.split(";")

#qty email will counts the number of emails entered and will be use to run the delete mecanism for that amount of time
qty_email = len(liste_emails_input)
print("You have entered "+ str(qty_email)+" emails addresses")

#headers parameters for the request that will permit us to get the ID of a user using its email address
headers = {
    "content-type" : "application/json; charset=utf-8",
    "authorization" : "Bearer " + access_token,
    }

i = 0
url +=api_call
from ciscosparkapi import CiscoSparkAPI
api = CiscoSparkAPI(access_token= access_token)

while i<qty_email:    
    user2delete_input = liste_emails_input[i]
    print("You are about to delete : "+user2delete_input)
    querystring = {"email":user2delete_input}
    response = requests.get(url, headers = headers, params=querystring).json()
    for item in response["items"]:
        id_user = item['id']
    api.people.delete(personId = id_user)
    print("--------------------Moving to the next user-------------------")
    if i == qty_email-1:
        print("")
        print("")
        print("Your deletion request is completed !!!!")
        print("")
    i = i +1
