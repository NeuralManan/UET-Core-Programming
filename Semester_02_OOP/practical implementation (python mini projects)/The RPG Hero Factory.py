class Hero:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} attacks with fists!")

    def heal(self): 
        print(f"{self.name} drinks a potion. Health is now 100.")


class Warrior(Hero):
    def __init__(self, name, shield):
     Hero.__init__(self, name)
     self.shield = shield

    def attack(self):
        if self.shield == True:
         print(f"{self.name} bashes with shield!") 

        else:
           print(f"{self.name} swings a sword!")

class Mage(Hero):
   def __init__(self, name, mana):
     Hero.__init__(self, name)
     self.mana = mana
   def attack(self):
      print(f"{self.name} casts a fireball! Mana left: {self.mana - 10}")
      self.mana -= 10


class Paladin(Warrior, Mage):
   def __init__(self, name):
      # 1. Manually initialize Warrior (giving it the shield it needs)
      Warrior.__init__(self, name, shield = True)
      # 2. Manually initialize Mage (giving it the mana it needs)
      Mage.__init__(self, name, mana = 50)

   def holy_strike(self):
      print(f"{self.name} strikes with holy light!")



# --- WRITE YOUR CLASSES HERE ---

# (Hero, Warrior, Mage, Paladin)

# -------------------------------

# --- TEST CODE (Do not change) ---
if __name__ == "__main__":
    print("--- 1. Single Inheritance ---")
    w = Warrior("Arthur", shield=True)
    m = Mage("Merlin", mana=100)

    w.attack() # Should print: Arthur bashes with shield!
    m.attack() # Should print: Merlin casts a fireball! Mana left: 90
    
    print("\n--- 2. Parent Logic ---")
    w.heal() # Should print: Arthur drinks a potion... (Inherited from Hero)

    print("\n--- 3. Multiple Inheritance (The Paladin) ---")
    p = Paladin("Uther")
    
    p.holy_strike() # Own method
    p.heal()        # Inherited from Grandparent (Hero)
    
    # THE BIG TEST: Which attack does it use?
    # Because Paladin(Warrior, Mage), Warrior comes first.
    print(f"MRO Order: {Paladin.mro()}")
    p.attack() # Should use Warrior's attack logic? Or Mage's?

      
   


"""
**MRO** stands for **Method Resolution Order**.

In simple terms, it is the **Queue** (or waiting line) that Python creates for every class. It tells Python **exactly which order** to search for methods or attributes.

When you call `p.attack()`, Python doesn't guess. It looks at the MRO list and asks:

1.  Does the Child have `attack`? (No? Go to next)
2.  Does Parent A have `attack`? (No? Go to next)
3.  Does Parent B have `attack`? (Yes\! Run it and **STOP**).

-----

### 1\. The "Golden Rule" of MRO

Python uses an algorithm called **C3 Linearization** (you don't need to memorize the math, just the behavior).

The rule is: **"Children First, then Left-to-Right, but Parents Last."**

If you have:


class Paladin(Warrior, Mage):
    pass


The MRO will be:

1.  **Paladin** (The Child)
2.  **Warrior** (The First Parent - Left side)
3.  **Mage** (The Second Parent - Right side)
4.  **Hero** (The Grandparent - kept for last)
5.  **object** (The base of all Python things)

-----

### 2\. The "Super()" Surprise (Why your code crashed)

This is the most important concept to unlearn:

  * **Myth:** `super()` calls the **Parent**.
  * **Reality:** `super()` calls the **Next Class in the MRO list**.

This distinction is why your code crashed earlier.

#### The Scenario:

You had a hierarchy like this: `Paladin(Warrior, Mage)`.
The MRO was: `[Paladin, Warrior, Mage, Hero]`.

1.  You were inside **Warrior**.
2.  You called `super().__init__()`.
3.  You *thought* it would go to **Hero** (Warrior's parent).
4.  **BUT**, because the object was a **Paladin**, Python looked at the MRO list.
5.  Who is next after Warrior in the Paladin list? **Mage**.
6.  So, `super()` inside Warrior actually called **Mage**.
7.  **Crash:** Warrior sent 0 arguments, but Mage expected `mana`.

**Visualizing the Trap:**

```text
      [Hero]
      /    \
[Warrior]  [Mage]  <-- Warrior's super() jumps SIDEWAYS to Mage!
      \    /
     [Paladin]
```

-----

### 3\. How to See the MRO

You can verify this "Queue" anytime by printing the `.__mro__` attribute or calling the `.mro()` method.

**Try running this small script:**


class A: pass
class B(A): pass
class C(A): pass

# D inherits from B and C
class D(B, C): pass

print(D.mro())


**Output:**

[
 <class '__main__.D'>,  # 1. Check D first
 <class '__main__.B'>,  # 2. Check B (Left parent)
 <class '__main__.C'>,  # 3. Check C (Right parent)
 <class '__main__.A'>,  # 4. Check A (Grandparent - only once!)
 <class 'object'>       # 5. The end
]


### Summary

1.  **MRO** is the "Line of Succession."
2.  **`super()`** is a traveler that moves one step forward in that line.
3.  In Multiple Inheritance, `super()` can jump **sideways** (from one sibling to another) before it goes up to the grandparent.

This is why, for your **Project 2**, we switched to **Manual Calling** (`Hero.__init__`). It ignores the MRO line and calls exactly who you tell it to call.
"""
               

           


    


    