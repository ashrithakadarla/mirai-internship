import requests
user_prompt="Ronaldo winning the world cup his jersey number is 7 and the jersey is manufactured by PUMA, along with the Portugal football team."
url=f"https://image.pollinations.ai/prompt/{user_prompt}"

print(f"Generating for: {user_prompt}")

response=requests.get(url)
print(response)

if(response.status_code==200):
    with open("GOAT.png","wb") as file:
        file.write(response.content)
    print("Success")
else:
    print("ERROR")