# Python Card Comparison

A small object-oriented Python project that models playing cards and simple card game rounds.

## Features

* Card comparison using operator overloading
* Rank and suit based ordering
* High Card game mode
* Low Card game mode
* Inheritance and polymorphism
* Type hints

## Card Ranking

Ranks are ordered from lowest to highest:

```text
2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < Jack < Queen < King < Ace
```

Suits are ordered from lowest to highest:

```text
Clubs < Diamonds < Hearts < Spades
```

If two cards have the same rank, suit is used as a tie-breaker.

## Example

```python
ace_spades = Card("Ace", "Spades")
king_hearts = Card("King", "Hearts")

print(ace_spades > king_hearts)
# True
```

## Project Structure

### Card

Represents a playing card and supports:

* Equality comparison (`==`)
* Less-than comparison (`<`)
* Greater-than comparison (`>`)

### Round

Base class for card game rounds.

### HighCardRound

The player with the higher card wins.

### LowCardRound

The player with the lower card wins.

## Concepts Demonstrated

* Classes and objects
* Inheritance
* Method overriding
* Operator overloading
* Polymorphism
* Type hints

## Running the Project

```bash
python main.py
```

