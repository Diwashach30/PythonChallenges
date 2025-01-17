##Add your 7 friend names to the list. Use where to find a name that starts with the
##alphabet a.


friends_name = ['Ranjit','Anup','Aadarsha','Sharad','Swikar','Ashish','Krishna']

for friend in friends_name :
    if friend.startswith ('A'):
        print(f"Found a name that starts with 'A': {friend}")
        break
    