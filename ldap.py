import  ldap

try:
  l = ldap.open("172.20.xx.xx",xxx)
  l.simple_bind_s("CN=azure_s_itisrvacc,OU=User,OU=DevOps,OU=Project,DC=cn133,DC=azure,DC=net","""password""")
except ldap.LDAPError,e:
  print "error when open ldap"
  print e

#baseDN = "ou=Dev,o=net.azure.cn133"
baseDN = "OU=Service,OU=Group,OU=DevOps,OU=Project,DC=cn133,DC=azure,DC=net"
searchScope = ldap.SCOPE_SUBTREE
retrieveAttributes = None
#searchFilter = "(&(memberOf=CN=DevOps_Grafana,OU=Service,OU=Group,OU=DevOps,OU=Project,DC=cn133,DC=azure,DC=net)(objectClass=person)(sAMAccountName=%s))"
searchFilter = "CN=DevOps_Grafana"
try:
        ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        result_set = []
        while 1:
                result_type, result_data = l.result(ldap_result_id, 0)
                if (result_data == []):
                        break
                else:
                        ## here you don't have to append to a list
                        ## you could do whatever you want with the individual entry
                        ## The appending to list is just for illustration.
                        if result_type == ldap.RES_SEARCH_ENTRY:
                                result_set.append(result_data)
#        print result_set[0][0][1]['member']

except ldap.LDAPError, e:
        print "error when search ldap"
        print e
