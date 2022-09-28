print("Task 1: \n")
print("I am signing up for Replit's 100 days of Python challenge! I will make sure to spend\nsome time every day coding along, for a minimum of 10 minutes a day. I'll be using\nReplit, an amazing online IDE so I can do this from my phone wherever I happend to be.\nNo excuses for not coding from the middle of a field!")
print("\nTask 1/2: \n")
a={'malware':'a set of code which does a specific job in a bad intention',
  "spybot":"it spies the data in the system anonymously",
  "trojan":"it intrudes the system as a trusted source and then starts executing in the background",
  "worms":"they infect the systems by infestion they corrupt everywhere they go"}
print("keys()\n",a.keys(),"\n")
ak=a.keys()
print("values()\n",a.values(),"\n")
print("fromkeys()\n",dict.fromkeys(ak),"\n")	
print("get()\n",a.get('spybot'),"\n")	
a1=a.copy()
print("copy()\n",a1,"\n")
a.pop("worms")
print('pop()\n',a,"\n")
a2=a.clear()
print("clear()\n",a2,"\n")
print("\nTask 2\n")
a=12300
b=18
print("NET: ",((b/100)*a)+a)
print("GST: ",((b/100)*a))
print('\nTask 3\n')
import pandas as pd
offence=("Sending threartening messages by email","Sending defamatory messages by email","Forgery of electronics","Bogus websites,cyber fraud ","Email spoofing","Web jacking","Email Abuse","Online sale of drugs","Online sale of arms")
Law=("SEC.503 IPC(INDIAN PENAL CODE)","SEC.499 IPC","SEC.463 IPC","SEC.420 IPC","SEC.463 IPC","SEC.383 IPC","SEC.500 IPC","narcotics drugs and Psychotropics substances (NDPS) Act 1985","Arms Act 1959")
df=pd.DataFrame(offence,Law)
print(df)
print(df[3:4])
print("\nTask 5")
print("\nCalculating  Elecr price")
unit=int(input("\nNumber of Units used: "))

if unit<100:
    price=unit*0.50
    print("Your Price : Rs.",price)
elif unit>101 and unit<200:
    price=unit*0.75
    print("Your Price : Rs.",price)
elif unit>201 and unit<300:
    price=unit*1.20
    print("Your Price : Rs.",price)
else:
    price=unit*1.50
    print("Your Price : Rs.",price)
    