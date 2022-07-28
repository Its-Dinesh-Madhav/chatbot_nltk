from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import datetime, date

bot = ChatBot('Buddy', storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='sqlite:///database.sqlite3')

trainer = ListTrainer(bot)
trainer.train([
'Hi',
'Helloo!',
'How are you',
'I am good, Thank you!',
'What can you do for me ?',
'I am made to give Information about VCET college.',
'What else can you do?',
'I can help you know more about VCET college.',
'What makes this college special?',
'This college has excellent professors and best campus for students.',
'Tell me about VCET college',
'VCET means a Body committed to enhancement of Knowledge. VCET was established as a registered society in 1970 by late Padmashri H. G. alias Bhausaheb Vartak for the noble cause of education in rural areas. VCET college, Vasai is located on the sprawling campus of Vidyavardhini, spread over an area of 12.27 acres. It is a short, two minutes walk from Vasai Road (W) Railway Station.',
'Tell me more about VCET college',
'You can visit this official site for more information https://vcet.edu.in/',
'What are contact available for reference?',
'Here is contact number you can refer:0250 233 8234',
'What are the branches available in VCET?',
'Branches available are:CSE-DS,AI-DS,Computers,IT,CIVIL,MECH,EXTC',
'How many Seats available for all Branches?',
'Mech,Extc,Comps,IT & Civil:120,AI & CSE:60',
'What more facilities are provided?',
'College has playground,gymkhana,Seminar Halls,Laboratories,library,Girls common room and much more',
'What are the Extra-Curricular activites?'
'Students Council, Sports Committee, Literati, NSS',
'What are the Co-curricular activites?'
'IEE,SAE,ISA,CSI,IETE,ISHRAE,VMEA,HACKATHON',
'What functions are organized by college?',
'College organizes Zeal,Hackathon,Aavhan (sport event) and much more.',
'Thank You',
'Welcome, Have a Good Day!!'

])

name = input("Enter Your Name: ")

now = datetime.now()
today = now.strftime("%A")
time = now.strftime("%H:%M:%S")

print("Hi, I am VCET Bot!!")
print(f"Today is {today}, current time is {time} ")
print("Let me know how can I help you?")

while True:
    request = input(name + ':')
    if request == 'Bye' or request == 'bye':
        print('Bot: Bye')
        break
    else:
        response = bot.get_response(request)
        print('Bot:', response)
