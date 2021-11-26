import requests
import json

class ticketManager:
    
    def __init__(self):
        self.pageNum = 0


    def connect():
        url = 'https://zccterra.zendesk.com/api/v2/tickets.json'
        user = 'nolan.matt@northeastern.edu/token'
        token = 'us7JSCXEcuEZjlnMuqoo8cnCCIbe0hNT8jVlMcS4'

        #do the http get request
        response = requests.get(url, auth=(user,token))

        #check for codes besides 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')
            exit()
    
        #Decode JSON response into a dictionary, and use data
        data = response.json()
        return data

    def factorData():
        #Example print
        subject_list = data['tickets']
        for subject in subject_list:
            print(subject['subject'])
        

    #def main():
        #print("running main")
        #task = ticketManager()
ticketManager.connect()

    #if __name__ == "__main__":
        #main()
