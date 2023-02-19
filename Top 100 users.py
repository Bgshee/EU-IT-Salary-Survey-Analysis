url = 'https://randomuser.me/ ' 

# Make a get request 
response = requests.get("https://randomuser.me/" ) 

# Get the response data as a python object 
data = response.json()
# List of top 100 users
var= top_male_users;
topmale_users = []

for i in range(1, 101):
    topmale_users.append("User #" + str(i))

print(top_male_users)