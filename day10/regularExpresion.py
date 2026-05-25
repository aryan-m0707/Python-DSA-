# import re
# count=0
# pattern=re.compile('function')
# # print(pattern)

# matcher=pattern.finditer('A function in python is defined by a def statement. ' \
# 'pyhton the general syntax looks like this: def function-name(Parameter list): statements, i.e. the function body.' \
# 'The parameter python list consists of none or more parameters.')

# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),'...',i.group())
# print('The number of occurrence: ',count)



# import re
# count=0
# matcher=re.finditer('Hi','HiHiHiHi')

# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),'...',i.group())
# print('The number of occurrence: ',count)


# import re
# obj=input('Enter any charecter: ')
# objmatch=re.finditer(obj,'a7b @k9z')
# print(objmatch)
# for match in objmatch:
#     print(match.start(),"...",match.end(),'...',match.group())



# import re
# a=input('Enter string to perform match operation : ')
# match=re.match(a,'python is very important language')
# print(match)
# if match!=None:
#     print('match found at begining level')
#     print(match.start(),' ',match.end())
# else:
#     print('There is no matching at begining level')



# import re
# a=input('Enter string to perform match operation : ')
# match=re.fullmatch(a,'python is very') # if match is found then it returns object otherwise None
# print(match)
# if match!=None:
#     print('match found') 
#     print(match.start(),' ',match.end())
# else:
#     print('Full match not found')



# import re
# s=input('Enter mail id : ')
# # match=re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com',s) # if match is found then it returns object otherwise None
# match=re.fullmatch('\w[a-zA-Z0-9_.]*@rknec[.]edu',s) 
# print(match)
# if match!=None:
#     print('Vaild E-mail Id') 
# else:
#     print('Invaild E-mail Id')


# import re
# s=input('Enter mobile no: ')
# # match=re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com',s) # if match is found then it returns object otherwise None
# match=re.fullmatch('[0-9]\d{9}',s) 
# print(match)
# if match!=None:
#     print('Vaild mobile Id') 
# else:
#     print('Invaild mobile Id')


# import re
# s=input('Enter mobile no: ')
# # match=re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com',s) # if match is found then it returns object otherwise None
# match=re.search(s,'python sss dynamic lannn') 
# print(match)
# if match!=None:
#     print(match.start(),"...",match.end(),'...',match.group())
# else:
#     print('There is no matching anything')


# import re
# match1=re.findall('[0-9]','abcdd3hb7fyt5$%^&')
# match2=re.findall('[a-z]','abcdd3hb7fyt5$%^&')
# match3=re.findall('[0-9a-z]','abcdd3hb7fyt5$%^&')
# match4=re.findall('[^0-9a-z]','abcdd3hb7fyt5$%^&')
# print(match1)
# print(match2)
# print(match3)
# print(match4)


# import re
# match1=re.sub('[A-Z]','*','2587 ASDF SDgb iuyt')
# print(match1)# 2587 **** **gb iuyt


# import re
# match1=re.subn('[A-Z]','*','2587 ASDF SDgb iuyt')
# print(match1)# ('2587 **** **gb iuyt', 6) it also return number of replacement
# print(match1[0])
# print(match1[1])


