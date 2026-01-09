import string
import hashlib
import time

# function for hashing using different methods
def hash(method, value):
    hashedValue = hashlib.new(method, value.encode()).hexdigest()
    return hashedValue

# function to get user's password
def getPassword(characters):
    isCorrect = False

    while isCorrect == False:
        userPassword = input("Enter your password: ")
        isCorrect2 = 0
        
        # check the length is 4 and every character used is in 'characters' string
        if len(userPassword) == 4:
            for x in range(len(userPassword)):
                if userPassword[x] in characters:
                    isCorrect2 += 1
                else:
                    print("All characters must be ASCII letters or integers")
        else:
            print("Length must be 4")
        
        if isCorrect2 == len(userPassword):
            isCorrect = True
    
    return userPassword

# try every possible combination to find user's password & measure time taken
def findPassword(hashedPassword, characters, method):
    start = time.time()

    for byte1 in range(len(characters)):
        for byte2 in range(len(characters)):
            for byte3 in range(len(characters)):
                for byte4 in range(len(characters)):
                    curr = characters[byte1] + characters[byte2] + characters[byte3] + characters[byte4]
                    if (hash(method, curr) == hashedPassword):
                        end = time.time()
                        print("Found: " + curr)
                        print(f"Found in: {end - start} seconds")
                        return
    print("Not Found")

# initialising characters allowed string and getting user's password
characters = string.ascii_letters + string.digits
userPassword = getPassword(characters)

# use md5 to hash & crack it
hashedPassword = hash('md5', userPassword)
findPassword(hashedPassword, characters, 'md5')

# use sha256 to hash & crack it
hashedPassword = hash('sha256', userPassword)
findPassword(hashedPassword, characters, 'sha256')