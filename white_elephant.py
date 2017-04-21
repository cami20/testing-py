import random
import doctest

def white_elephant(guests_gifts):
    """Play white elephant game

    >>> guests_gifts = {'kiko': 'rock', 'camille': 'cupcake', 'Ahmed': 'book', 'sammie': 'flower'}
    >>> white_elephant(guests_gifts)
    {'camille': 'rock', 'kiko': 'book', 'Ahmed': 'flower', 'sammie': 'cupcake'}

    """

    new_gifts = {}
    # gifts = guests_gifts.values()
    # for guest in guests_gifts:
    #     gift = random.choice(gifts)
    #     new_gifts[guest] = gift
    #     while guests_gifts[guest] == new_gifts[guest]:
    #         gift = random.choice(gifts)
    #         new_gifts[guest] = gift
    #     gifts.remove(gift)

    guests = guests_gifts.keys()
    gifts = guests_gifts.values()
    for i in range(len(guests)):
        if i == len(guests) - 1:
            new_gifts[guests[i]] = gifts[0]
        else:
            new_gifts[guests[i]] = gifts[i+1]

    return new_gifts


if __name__ == "__main__":
    doctest.testmod()