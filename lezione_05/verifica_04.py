def blackjack_hand_total(cards: list[int]) -> int:
    total = 0
    aces = 0

    for card in cards:
        if card == 11:
            aces += 1
        total += card

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total