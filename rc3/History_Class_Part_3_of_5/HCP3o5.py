key = "Voulez=vous sentir la difference? Jettez les yeux sur le continent septentrional de l'amerique. Dans les resolutions vigoureuses de ces braves colons vous reconnoitrez la voix de la vraie liberte * aux prises avec l'oppression. Vous fremirez, vous vous revolte= rez contre la morgue & la durete inconcevable de ceux, qui, jaloux a l'extreme de leur propre liberte, pensent de pouvoir devenir plus puissants, de pouvoir rester libres eux=memes en asservissant leurs freres. Vous ne pourrez vous empecher de faire votre cause de celle de ces peuples, de leur savoir gre de leur fermete, de trem= bler qu'ils ne suciombent sous la massue levee du pouvoir, qui veut ou les gouverner arbitrairement, ou les ecraser, en fin de leur sou= haiter avec le genereux d. der. tout le succes possible dans leur juste resistance."
key = key.replace(' ','')

positionsToGet = [230, 613, 489, 541, 253, 655, 40, 498, 341, 284, 613]
text = ''
for i in positionsToGet:
    text += key[i-1]

print (text)
