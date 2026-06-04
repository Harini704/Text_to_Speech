from gtts import gTTS
import os
text = "The Lion and the Mouse One day, a lion was sleeping in the forest when a little mouse ran across his paw. The lion woke up and caught the mouse.Please let me go,begged the mouse. Someday I may help you.The lion laughed.How can such a tiny creature help me?But he let the mouse go.A few days later, the lion was trapped in a hunter's net. Hearing his roars, the mouse rushed over and began gnawing the ropes. Soon, the lion was free.The lion said,I was wrong. Even a small friend can be a great help.Moral: Kindness is never wasted, and even the smallest can help the strongest."
language = 'en'
obj = gTTS(text = text,lang=language,slow=False)
obj.save("sample.mp3")
print("mp3 created succesfully")
os.system("sample.mp3")