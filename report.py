from tkinter import *
from PIL import ImageTk, Image  
from bs4 import BeautifulSoup
import random
import pyttsx3
import gtts
from playsound import playsound


app = Tk()

engine = pyttsx3.init()
# Html doc
html_doc ="""<html>
<head>
  <title>Head's title</title>
</head>

<body>

  <p class="element1">
  The Golden Touch of Midas

Once upon a time, there was a Greek King, Midas.
He was very rich and had lots of Gold. He had a daughter, who he loved a lot.
One day, Midas found an angel in need of help. He helped her and in return she agreed to grant a wish.
Midas wished that everything he touched would turn into gold. His wish was granted
On his way home, he touched rocks and plants and they turned into gold.
As he reached home, in excitement he hugged his daughter, who turned into gold.
Midas was devastated and he had learnt his lesson. Upon learning his lesson, Midas asked the angel to take his wish away.
Moral of the story
Greed is not good for you. Be content and satisfied to lead a happy and fulfilling life.</p>

<p class="element2">
The Tortoise and the Hare

This is an extremely popular story about a hare and a tortoise.
The hare is an animal that is known to move quickly, while a tortoise is one to move slowly.
One day, the hare challenged the tortoise to a race simply to prove that he was the best. The tortoise agreed.
Once the race began the hare was easily able to get a head start. Upon realizing that the tortoise is far behind. 
The overconfident hare decided to take a nap.
Meanwhile the tortoise, who was extremely determined and dedicated to the race was slowly nearing the finish line.
The tortoise won the race while the hare napped. Most importantly he did it with humility and without arrogance.

Moral of the story
When you work hard and persevere, you can achieve your goals. Slow and steady wins the race.</p>
<p class="element3">
The Boy who cried wolf

A farmer asked his son to take their herd of sheep grazing every day.
While the boy watched over the sheep, he got bored and decided to have some fun.
So, he shouted, “Wolf! Wolf!”. Upon hearing this the villagers ran to help him chase the Wolf away.
As they reached him, they realized that there was no Wolf and he was just kidding. 
The villagers were furious and they yelled at the boy for creating chaos and panic.
On the next day and the boy shouted “Wolf!” again and once again the villagers came to help him and saw that there was no wolf.
 This made them very angry again.
On the same day, the boy saw an actual Wolf that has terrorizing the sheep.
 The boy cried “Wolf! Wolf! please help me” and no villagers showed up as they believed that the boy was joking again.

Moral of the story
Don’t play with people’s trust, when it matters the most, they won’t believe you.</p>
<p class="element4">
The Three Little Pigs

Three Little pigs was sent out into the world by their mother to learn.
The three pigs, all decided to build a house on their own.
The first pig built a house of straw because he didn't want to put in a lot of effort and was lazy.
The second pig was a little less lazy than the first and he made a house of sticks.
The third pig was hardworking and he put in lots of effort and built a house of brick and stone.
One day a wolf came to attack them. He huffed and puffed and blew the house of straw.
He then huffed and puffed and blew the house the sticks.
He huffed and puffed and huffed and puffed at the house of bricks but eventually was out of breath and left.
Moral of the story
Always work hard and it will pay off. Don’t try to take shortcuts to make things work.</p>
<p class="element5">
The Fox and the Stork

Once there was a Fox and a stork. The Fox was selfish but he decided to invite the stork for dinner.
 The Stork was extremely happy to be invited and she reached his house on time.
The Fox opened the door and invited her in. 
They sat on the table; The Fox served her some soup in shallow bowls.
 While the fox licked up his soup, the Stork couldn't drink it because she has a long beak and the bowl was too shallow.
The next day, the Stork invited the fox over for dinner. 
She Served him soup as well but in two narrow vases.
 While the Stork enjoyed her soup and finished it, the fox went home very hungry realizing his mistake.
Moral of the Story
Don’t be selfish because it will come back to you at some point.</p>
<p class="element6">The Ant and the Grasshopper
The ant and the grasshopper were best friends with very different personalities.
The grasshopper would spend his days sleeping or playing his guitar while the ant would collect food and build his ant hill. 
Every now and then, the grasshopper would tell the ant to take a break. However, the ant would refuse and continue to complete his work.
Soon winter came making the days and nights cold. One day the colony of ants were busy trying to dry some grains of corn. The grasshopper who was extremely weak and
 hungry came up to the ants and asked "Can you please give me a piece of corn?" the ant replied "We worked hard for this corn all summer while you relaxed, why should we give it to you?"
The grasshopper was so busy singing and sleeping  that he didn't have enough food to last winter. The grasshopper realized his mistake.
Moral of the Story
Make use of opportunity while you have it</p>
<p class="element7">Be wise while counting
One day in Akbar’s court someone asked the question, "How many crows are there in the city?", No one had the answer.
Birbal quickly replied "Four thousand three hundred and twelve". He was asked how did he know this?
Birbal send " Send your man out to count the crows. If it is lesser than this number then some crows are visiting their families elsewhere and if it is more than this number, then some crows from outside are visiting their families here. Akbar was very happy with the answer and showered Birbal with gifts for his wit.
 
Moral of the story:
Sometimes you have to learn to think outside of the box.</p>
<p class="element8">The Monkey and the Crocodile
This is a story from Panchatantra.
A monkey lived on a berry tree on the River Bank. Once he saw a crocodile under the tree who looked hungry and tired. He gave the crocodile some berries, the crocodile thanked the monkey and became one of his friends. 
The monkey would give berries to the crocodile every day. One day the monkey even gave the crocodile extra berries to take to his wife.
His wife enjoyed the berries but told her husband that she wanted to eat the monkey's heart. She was a wicked and cunning woman. The crocodile was upset, but he decided that he needed to make his wife happy.
On the next day, the crocodile went to the monkey and said that his wife had called him for dinner. The crocodile carried the monkey on his back across the river. He told this monkey his wife's plan. 
The monkey had to think quickly if he wanted to save himself. He told the crocodile that he left his heart at on the berry tree and that they needed to return.
On reaching the monkey climbed the tree and spoke. "I'm not getting down; you betrayed my trust and that means our friendship is over"

Moral of the story
Never betray someone who trusts you and choose your friends wisely.</p>
<p class="element9">The foolish thief
One day, a wealthy man came to Akbar's court in hope to get help from Birbal. The man suspected that one of his servants had stolen from him.
The clever Birbal thought of a plan and gave all the merchant’s servants sticks of the same length. 
He also told them that the stick will grow three inches by tomorrow if they were the thief.
The next day, all the servants gathered around Birbal. He noticed that one of the servant’s sticks was three inches shorter than the others.
 Birbal immediately understood who the thief was.
The thief had cut the stick shorter by three inches as he thought it would grow three inches. Because of this his guilt was proven
Moral of the story
The truth will always come out one way or another so better to be truthful from the beginning.</p>
<p class="element10">The Brahmin’s dream
A poor Brahmin lived in a village all alone. He had no friends or relatives. He was known for being stingy and he used to beg for a living. The food he got as alms were kept in an earthen pot which was hung beside his bed. This allowed him to easily access the food when he got hungry.  
On one day, he got so much rice gruel that even after completing his meal, there was so much leftover in his pot. That night, he dreamt that his pot was overflowing with rice gruel and that if a famine came, he could sell the food and earn silver from it.
 This silver could then be used to buy a pair of goats who would soon have kids and create a herd. This herd in turn could be traded for buffaloes who would give milk from which he could make dairy products. These products could be sold in the market for more money.
This money would help him get married to a rich woman and together they would have a son who he could scold and love in equal measure. He dreamt that when his son wouldn’t listen, he would run after him with a stick.
Wrapped up in his dream the Brahmin picked up the stick near his bed and started hitting  the air with the stick. While flailing about, he hit the earthen pot with the stick, the pot broke and all the contents spilled over him.
 The Brahmin woke up with a start only to realize that everything was a dream.
Moral of the story
One should not build castles in the air.</p>

</body>
</head>
</html>"""
engine.say("Hello Here A Story For You. I Hope You will love it")
soup = BeautifulSoup(html_doc, 'html.parser')
app.title("Welcome")
img =Image.open('C:\\Users\\Akanchha Srivastav\\Downloads\\tree.jpg')
bg = ImageTk.PhotoImage(img)

app.geometry("650x450")

# Add image
label = Label(app, image=bg)
label.place(x = 0,y = 0)

# Add text
element1 = soup.body.find('p', attrs={'class' : 'element1'}).text
element2 = soup.body.find('p', attrs={'class' : 'element2'}).text
element3 = soup.body.find('p', attrs={'class' : 'element3'}).text
element4 = soup.body.find('p', attrs={'class' : 'element4'}).text
element5 = soup.body.find('p', attrs={'class' : 'element5'}).text
element6 = soup.body.find('p', attrs={'class' : 'element6'}).text
element7 = soup.body.find('p', attrs={'class' : 'element7'}).text
element8 = soup.body.find('p', attrs={'class' : 'element8'}).text
element9 = soup.body.find('p', attrs={'class' : 'element9'}).text
element10 = soup.body.find('p', attrs={'class' : 'element10'}).text
list=[element1,element2,element3,element4,element5,element6,element7,element8,element9,element10]

result=random.choice(list)

tts = gtts.gTTS(result)
tts.save("hello.mp3")

def changeText():  
   print(result)
    


label2 = Label(app, text=result,
               font=("Times New Roman", 14,"bold"),fg='black')

label2.pack(pady=2, padx=0)



# Define a function to play the music
def play_sound():
   playsound("hello.mp3")

# Add a Button widget
b1 = Button(app, text="Play Audio", command=play_sound)
b1.pack(pady=60)

def close():
   app.quit()

engine.runAndWait()
# Create a Button to call close()
Button(app, text= "Exit", font=("Calibri",14,"bold"), command=close).pack(pady=20)


app.mainloop()

