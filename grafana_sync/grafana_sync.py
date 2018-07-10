#!/usr/bin/python

import json
import os
import time 
import ldap
import datetime
import requests
import re

requests.packages.urllib3.disable_warnings()
mytoken=os.environ['GRAFANA_TOKEN']
interval=os.environ['INTERVAL']
ldappw=os.environ['LDAPPW']

header = {
    'Authorization': 'Basic '+mytoken,
    'Content-Type': 'application/json',
}

adGroupList = []
gfGroupList = []
gfAllUserList = []

def getLdapGroupList():
    
    try:
        l = ldap.open("172.20.1.167",389)
        l.simple_bind_s("CN=azure_s_itisrvacc,OU=User,OU=DevOps,OU=Project,DC=cn133,DC=azure,DC=net",ldappw)
    except ldap.LDAPError,e:
        print "Error when open ldap"
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
            if (len(result_data) == 0):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)

        global adGroupList
        for i in result_set:
            grp = "".join(i[0][1]["name"])
            adGroupList.append(grp)
 
    except ldap.LDAPError, e:
        print "Error when search ldap"
        print e

## Get a ldap user list by group name 
def getadUserListByGrp(grp):
    try:
        l = ldap.open("172.20.1.167",389)
        l.simple_bind_s("CN=azure_s_itisrvacc,OU=User,OU=DevOps,OU=Project,DC=cn133,DC=azure,DC=net",ldappw)
    except ldap.LDAPError,e:
        print "Error when open ldap"
        print e

    baseDN = "OU=Project,OU=Group,OU=DevOps,OU=Project,DC=cn133,DC=azure,DC=net"
    searchScope = ldap.SCOPE_ONELEVEL
    retrieveAttributes = None
    searchFilter = "CN="+str(grp)
    try:
        ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        result_set = []
        while 1:
            result_type, result_data = l.result(ldap_result_id, 0)
            if (len(result_data) == 0):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)

        for i in result_set:
            aduserList = []
            if i[0][1].has_key('member'):
                for j in i[0][1]["member"]:
                    cn = re.split(r"=|,",j)[1]
                    aduserList.append(cn)
            return aduserList
    
    except ldap.LDAPError, e:
        print "Error when search ldap"
        print e

### Get all orgs in grafana, to a List type
def getGfGroupList():
    getAllOrgsUrl="https://grafana.cn133.azure.net/api/orgs/"
    orgs = requests.get(getAllOrgsUrl, headers=header,verify=False)
    
    global gfGroupList
    for i in orgs.json():
         org =  i['name']
         gfGroupList.append(org)

## Get a grafana user list by org name 
def getGfUserlistByorg(orgName):
    getUserlistByorgUrl="https://grafana.cn133.azure.net/api/orgs/"+str(getOrgIdByName(orgName))+"/users"
    UserInOrg = requests.get(getUserlistByorgUrl, headers=header,verify=False)
    gfUserList = []
    for i in UserInOrg.json():
         user =  i['login']
         gfUserList.append(user)
    return  gfUserList

### Get all users in grafana,to a List type
def getGfAllUserList():
    allUserUrl="https://grafana.cn133.azure.net/api/users"
    users = requests.get(allUserUrl, headers=header,verify=False)
    global gfAllUserList
    for i in users.json():
        user = i['login']
        gfAllUserList.append(user)
    return gfAllUserList


### Return Org Id <int> type
def getOrgIdByName(orgName):
    getOrgIdUrl="https://grafana.cn133.azure.net/api/orgs/name/"+str(orgName)
    org =  requests.get(getOrgIdUrl, headers=header,verify=False) 
    return org.json()['id']

### Return  User Id
def getUserIdByName(userName):
    getUserIdUrl="https://grafana.cn133.azure.net/api/users/lookup?loginOrEmail="+userName
    user =  requests.get(getUserIdUrl, headers=header,verify=False)
    return user.json()['id']

def compareGrpList():
                                                                   ##  for test gfGroupList.remove("testpro1")
    res_grp = list(set(adGroupList).difference(set(gfGroupList)))  ##  list(set(b).difference(set(a))) # In b but not in a
    return res_grp

### Return a list
def compareUserList(grp):
    res_user = list(set(getadUserListByGrp(grp)).difference(set(getGfUserlistByorg(grp))))
    return  res_user
    
### Return a list
def getDelUserList(grp):
    res_user = list(set(getGfUserlistByorg(grp)).difference(set(getadUserListByGrp(grp))))
    return  res_user
    
def addOrg(myOrg):
    addOrgUrl="https://grafana.cn133.azure.net/api/orgs"
    d = '{"name":"' + myOrg +'"}'
    result = requests.post(addOrgUrl,headers=header,data=d, verify=False)

def addUserToOrg(userName,uid):
    addUserToOrgUrl="https://grafana.cn133.azure.net/api/orgs/"+str(uid)+"/users"
    d = '{"loginOrEmail": "' + userName + '", "role": "Viewer"}'
    r = requests.post(addUserToOrgUrl, headers=header, data=d, verify=False)
    print r

def deleteUserInOrg(orgId,userId):
    deleteUserInOrgUrl="https://grafana.cn133.azure.net/api/orgs/"+str(orgId)+"/users/"+str(userId)   #/api/orgs/:orgId/users/:userId
    r = requests.delete(deleteUserInOrgUrl, headers=header, verify=False)
    print r
    
    
if __name__ == "__main__":

    while 1:
        begin_time_stamp = datetime.datetime.now()
        print "Begin time is  -----",begin_time_stamp

        getLdapGroupList()
    
        getGfGroupList() 
    
        getGfAllUserList()
    
        #addUserToOrg("az_a_twangfw",20)
    
        diff_grp = compareGrpList()
        
        if len(diff_grp) != 0:      
            print "**there a diff grp**"   
            print diff_grp
            for i in diff_grp:
                addOrg(i)          
                print "add org  -----"
                print i
        else:
            print "There is no new group....."

### add user to group     
        for i in adGroupList:
            print "In ldap ,there is grp :  " + i 
            diff_user  = compareUserList(i)
            for j in diff_user:
                if j in gfAllUserList:                                     ##judge whether login the grafana system
                    print j + "  has logged in grafana  "
                    print j
                    print getOrgIdByName(i)    
                    addUserToOrg(j,getOrgIdByName(i))                   ##add user to organization
                else:
                    print j + "  yet not log in grafana. >>Just Known It<< "    ## do nothing

### delete user in group                    
        for i in adGroupList:
            del_user = getDelUserList(i)
            if len(del_user) != 0:
                for j in del_user:
                    if j != "admin":
                        print "user in groupppp will be delete" + j
                        print  getOrgIdByName(i)    
                        deleteUserInOrg(getOrgIdByName(i),getUserIdByName(j))        ##delete user in organization
            else:
                print "No user will be delete."
                    
                    
        end_time_stamp = datetime.datetime.now()
        print "End time is  -----",end_time_stamp
        time.sleep(int(interval))