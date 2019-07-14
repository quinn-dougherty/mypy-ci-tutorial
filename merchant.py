#!/usr/bin/env python

from typing import Optional, Tuple, Callable
from dataclasses import dataclass

@dataclass
class Player: 
    name: str
    gold: int

Location = Callable[[Optional[Player]], str]

# let's compare merchant greetings in world of warcraft
def elwynn(player: Optional[Player]) -> str:
    ''' the merchant greeting in elwynn forest '''
    base = "I buy and trade"
    return f"{base}, {player.name}" if player else base

def tirisfal(player: Optional[Player]) -> str:
    ''' the merchant greeting in tirisfal glades '''
    base = "I haven't got all day"
    return f"{base}, {player.name}" if player else base

def buy_bread(player: Player, location: Location): 
    ''' prints a greeting and mutates the amount of gold the player has''' 
    print(location(player))
    player.gold -= 5
    pass

def bump(location: Location): 
    ''' bump into a merchant but don't buy anything''' 
    print(location(None))
    pass


if __name__=='__main__':
    leroy = Player("leroy", 100)
    jenkins = Player("jenkins", 99)
    
    buy_bread(leroy, elwynn)

    buy_bread(jenkins, tirisfal)

    bump(tirisfal)
    bump(elwynn)

    print(leroy)
    print(jenkins)
