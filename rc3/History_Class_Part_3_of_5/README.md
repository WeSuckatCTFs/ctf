# History Class Part (3/5)

For this challege we were given a family crest and a set of numbers.

![The crest](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Coat_of_Arms_of_Benjamin_Franklin.svg/593px-Coat_of_Arms_of_Benjamin_Franklin.svg.png)

230, 613, 489, 541, 253, 655, 40, 498, 341, 284, 613

First of all we googled the numbers, but nothing of value came up. So then we used google to image search the crest: turns out that it belongs to Benjamin Franklin! Next up, googling 'Benjamin Franklin Cipher'.

This is where it started making sense; Franklin used a cipher called Dumas' Cipher, to send a letter in 1776 which was recently decoded.

The cipher uses a key text, and the numbers written correspond to the letter at that position in the text.

Using the text, I made a small python script to print out the corresponding letters.

```python
key = "Voulez=vous sentir la difference? Jettez les yeux sur le continent septentrional de l'amerique. Dans les resolutions vigoureuses de ces braves colons vous reconnoitrez la voix de la vraie liberte * aux prises avec l'oppression. Vous fremirez, vous vous revolte= rez contre la morgue & la durete inconcevable de ceux, qui, jaloux a l'extreme de leur propre liberte, pensent de pouvoir devenir plus puissants, de pouvoir rester libres eux=memes en asservissant leurs freres. Vous ne pourrez vous empecher de faire votre cause de celle de ces peuples, de leur savoir gre de leur fermete, de trem= bler qu'ils ne suciombent sous la massue levee du pouvoir, qui veut ou les gouverner arbitrairement, ou les ecraser, en fin de leur sou= haiter avec le genereux d. der. tout le succes possible dans leur juste resistance."
key = key.replace(' ','')

positionsToGet = [230, 613, 489, 541, 253, 655, 40, 498, 341, 284, 613]
text = ''
for i in positionsToGet:
    text += key[i-1]
print (text)
```
The code printed out the result: 'thepoiymath' and after google autocorrected that to 'The Polymath', we got the flag!


RC3-2017{thepolymath}
