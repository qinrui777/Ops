cat grafana_sync.py 
#!/usr/bin/python

import json
import os
import time 
import ldap
import datetime
import requests
import re

requests.packages.urllib3.disable_warnings()
header = {'Authorization':'Basic YWRtaWde4DM1LdwedwePGtQQTV2fU5+dw=='}

userList = []
orgList = []

### GetLdapInfo 
def getLdapInfo():

    try:
        l = ldap.open("172.20.xx.xx7",389)
        l.simple_bind_s("CN=azure_s_itisrvacc,OU=User,OU=DevOps,OU=Project,DC=cn133,DC=azure,DC=net","""xx%,iieH""")
    except ldap.LDAPError,e:
        print "error when open ldap"
        print e

    baseDN = "OU=Project,OU=Group,OU=DevOps,OU=Project,DC=cn133,DC=azure,DC=net"
    searchScope = ldap.SCOPE_ONELEVEL
    retrieveAttributes = None
    searchFilter = "CN=*"
    try:
        ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        result_set = []
        while 1:
                result_type, result_data = l.result(ldap_result_id, 0)
                if (result_data == []):
                        break
                else:
                        if result_type == ldap.RES_SEARCH_ENTRY:
                                result_set.append(result_data)
        for i in result_set:
            grp = "".join(i[0][1]["name"])
            if grp in orgList:
                print grp, " is in grafana orgList. "
            else:
                print grp ,"  >>>>>> Attention <<<<<<< is Not in grafana orgList, we will add it."
###change IT  ##addOrg(grp) 

            if i[0][1].has_key('member'):
                for j in i[0][1]["member"]:
                    cn = re.split(r"=|,",j)[1]
                    if cn in userList:
                        if 1==getUserorgIdByName(cn):     ## judge whether new user
                            print  cn,"is a new user,shouled in org **",grp
                            mapping(getOrgIdByName(grp),getUserIdByName(cn))
                        else:
                            print cn,"has correct org to user relationship >>>>",grp
                    else:
                        print cn," has not yet logged in to the system.....waiting for...."
                   
    except ldap.LDAPError, e:
        print "error when search ldap"
        print e

### Get all orgs in grafana, to a List type
def getOrgList():
    getAllOrgsUrl="https://grafana.cn133.azure.net/api/orgs/"
    header = {'Authorization':'Basic YWRtaW46SDM1LmpRPGtQQTV2fU5+dw=='}
    orgs = requests.get(getAllOrgsUrl, headers=header,verify=False)
    
    global orgList
    for i in orgs.json():
         org =  i['name']
         orgList.append(org)
####    custom define org to orgList
####    orgList.append('wechatweb')

### Get all users in grafana,to a List type
def getUserList():
    allUserUrl="https://grafana.cn133.azure.net/api/users"
    users = requests.get(allUserUrl, headers=header,verify=False)
    global userList
    for i in users.json():
        user = i['login']
        userList.append(user)

def grepOrgByUser(user):
    os.system('bash /root/script/mapping.sh {0}'.format(user))

def addOrg(myOrg):
    addOrgUrl="https://grafana.cn133.azure.net/api/orgs"
    header = {'Authorization':'Basic YWRtaW46SDM1LmpRPGtQQTV2fU5+dw=='}
    d = {"name":myOrg}
    result = requests.post(addOrgUrl,headers=headers,data=d, verify=False)
##    print result.json()

### return Org Id int type
def getOrgIdByName(orgName):
    getOrgIdUrl="https://grafana.cn133.azure.net/api/orgs/name/"+orgName
    org =  requests.get(getOrgIdUrl, headers=header,verify=False) 
    return org.json()['id']

### retunr User Id 
def getUserIdByName(userName):
    getUserIdUrl="https://grafana.cn133.azure.net/api/users/lookup?loginOrEmail="+userName
    user =  requests.get(getUserIdUrl, headers=header,verify=False)
    return user.json()['id']

### retunr User org ID  int tyep
def getUserorgIdByName(userName):
    getUserIdUrl="https://grafana.cn133.azure.net/api/users/lookup?loginOrEmail="+userName
    user =  requests.get(getUserIdUrl, headers=header,verify=False)
    return user.json()['orgId']

def mapping(oid,uid):
    mappingUrl="https://grafana.cn133.azure.net/api/users/"+str(uid)+"/using/"+str(oid)
    d = {}
    requests.post(mappingUrl, headers=header,data=d,verify=False)
    print  "******we have  mapping **"+str(uid)+"to ***"+str(oid)
     
   
if __name__ == "__main__":

    begin_time_stamp = datetime.datetime.now() 
    print "Begin time is  -----",begin_time_stamp
    
    getOrgList()
    getUserList() 
    
    getLdapInfo()

    end_time_stamp = datetime.datetime.now()
    print "End time is  -----",end_time_stamp
[1m[31mXDOSMCNSA0025:~/script #(B[m 
