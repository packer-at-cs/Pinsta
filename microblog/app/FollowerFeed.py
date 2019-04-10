userID = [0, 1, 2, 3]

userPost = {0: ['post1', 'post2', 'post3'], 1: ['post1', 'post2', 'post3'], 2: ['post1', 'post2', 'post3'], 3: ['post1', 'post2', 'post3']}

userFollowers = {0: [1, 2, 3], 1: [0, 2], 2: [3], 3: [0,2]}



def addFollower():
  print('enter your ID')
  user = int(input())
  if user not in userID:
    print('this user does not exist. Try again.')
    user = int(input())
  print("Enter User ID of person you would like to add. ")
  a = int(input())
  if a in userFollowers[user]:
    print('you already follow them')
  elif a not in userID:
    print('This user does not exist')
  else:
    userFollowers[user].append(a)
    print(userFollowers[user])

def viewFeed():
  print("Who's feed would you like to view?")
  iD = int(input())
  if iD in userID:
    print(userPost[iD])
  else:
    print("this user doesn't exist")
    iD = int(input())

def newUser():
  print('enter ID of user')
  iD = int(input())
  if iD not in userID:
    userID.append(iD)
  else:
    print('this user already exists')
    iD = int(input())

def main():
  print("What would you like to do? 'Add followers' or 'view feed?' or 'register new user'")
  a = input()
  if a == 'view feed':
    viewFeed()
  elif a == 'add followers':
    addFollower()
  elif a == 'new user':
    newUser()
  else:
    print("I don't understand")
    a = input()

main()
