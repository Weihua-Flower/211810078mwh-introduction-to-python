#!/usr/bin/env python
# coding: utf-8

# # 作业

# In[1]:


# 练习 7.1: 汽车租赁
car_type = input("您想租什么样的汽车？ ")
print("让我看看我是否能找到一辆 " + car_type + " 给您。")


# In[2]:


# 练习 7.2: 餐馆订位
num_people = int(input("有多少人用餐？ "))
if num_people > 8:
    print("对不起，没有空桌。")
else:
    print("有空桌可供用餐。")


# In[3]:


# 练习 7.3: 10 的整数倍
num = int(input("请输入一个数："))
if num % 10 == 0:
    print(num, "是10的整数倍。")
else:
    print(num, "不是10的整数倍。")


# # 课堂练习while

# In[4]:


current_number=1
while current_number<=5:
    print (current_number)
    current_number+=1


# In[5]:


prompt='\nTell me something, and I will repeat it back to you:'
prompt+='\nEnter "quit" to end the progam.'

message=""
while message!='quit':
    message=input(prompt)
    print(message)


# In[6]:


prompt='\nTell me something, and I will repeat it back to you:'
prompt+='\nEnter "quit" to end the progam.'

message=""
while message!='quit':
    message=input(prompt)
    
    if message!='quit':
        print(message)
    


# In[7]:


prompt='\nTell me something, and I will repeat it back to you:'
prompt+='\nEnter "quit" to end the progam.'

active=True
while active:
    message=input(prompt)
    
    if message=='quit':
        active=False
    else:
        print (message)


# In[ ]:





# In[1]:


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program: "
while True:
    city = input(prompt)
    
    if city == 'quit':
        active = False  # 当输入为 'quit' 时，将 active 设置为 False，退出循环
        break
    else:
        print(f"I'd love to go to {city.title()}!")


# In[2]:


current_number=0
while current_number<10:
    current_number+=1
    if current_number%2==0:
        continue
        
    print(current_number)


# # 作业

# In[3]:


#比萨配料
while True:
    topping = input("请输入比萨配料（输入'quit'结束）：")
    if topping == 'quit':
        break
    else:
        print("要在比萨中添加：" + topping)


# In[4]:


#电影票
while True:
    age = input("请输入您的年龄（输入'quit'结束）：")
    if age == 'quit':
        break
    age = int(age)  # 将输入的年龄转换为整数类型
    if age < 3:
        print("您的票价为：免费")
    elif 3 <= age <= 12:
        print("您的票价为：$10")
    else:
        print("您的票价为：$15")


# In[6]:


#三种出路
#while
prompt='\n请输入一些比萨配料:'
prompt+='\nEnter "quit" to end the progam.'

message=""
while message!='quit':
    message=input(prompt)
    if message != 'quit':
        print("要在比萨中添加：" + message)


# In[7]:


#active
active = True
while active:
    topping = input("请输入比萨配料（输入'quit'结束）：")
    if topping == 'quit':
        active = False
    else:
        print("要在比萨中添加：" + topping)


# # 课堂练习

# In[11]:


unconfirmed_users = ['a', 'b', 'c']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# In[14]:


pets=['A','B','C',"A",'A']
print(pets)

while 'A' in pets:
    pets.remove('A')
    
print(pets)


# In[16]:


responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False

print("\n--- Poll results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


# # 作业

# In[18]:


# 练习 7.8: 熟食店
sandwich_orders = ['tuna', 'chicken', 'pastrami', 'vegetable', 'pastrami', 'ham', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    if sandwich != 'pastrami':
        print("I made your " + sandwich + " sandwich.")
        finished_sandwiches.append(sandwich)
print("I made your pastrami sandwich.")

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)
print("- pastrami")


# In[20]:


# 练习 7.9: 五香烟熏牛肉卖完了
sandwich_orders = ['tuna', 'chicken', 'pastrami', 'vegetable', 'pastrami', 'ham', 'pastrami']
print("\nThe pastrami is sold out!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nUpdated sandwich orders:")
print(sandwich_orders)


# In[21]:


# 练习 7.10: 梦想中的度假胜地
dream_destination = input("If you could visit one place in the world, where would you go? ")
print("You dream of visiting " + dream_destination + ".")


# # 课堂练习Function

# In[24]:


def greet_user():
    """显示简单的问候"""
    print("Hello!")

greet_user()


# In[25]:


def greet_user(username):
    """显示简单的问候"""
    print(f"Hello,{username.title()}")

greet_user('jesse')


# In[26]:


#8.1
def display_message():
    print("本章的主题是函数。")

# 调用函数显示消息
display_message()


# In[27]:


#8.2
def favorite_book(title):
    print("One of my favorite books is " + title + ".")

# 调用函数，并传递一本书的书名作为实参
favorite_book("Alice in Wonderland")


# In[ ]:




