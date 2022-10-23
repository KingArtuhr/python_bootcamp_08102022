#1
marketing = ['loyality program', 'client promotion', 'market reserch']
print(marketing)

#2
marketing.append('public relations')
print(marketing)

#3
print(marketing[2])

#4
marketing.insert(1, 'investor relation')
print(marketing)

#5
email_marketing = marketing.copy()
print(email_marketing)

#6
email_marketing.sort()
print(email_marketing)

#7
internal_emails = ['internal communication']

#8
email_marketing.extend(internal_emails)
print(email_marketing)

#9

email_tuple = tuple(email_marketing)
print(email_tuple)


