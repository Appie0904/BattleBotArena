# BattleBotArena
Concepts of Programming Languages Assignment 3

1. Project Summary (for PDF)

BattleBot Arena is a Python-based object-oriented combat simulator where players design, upgrade, and battle high-tech robots in a virtual arena. Each robot (or “bot”) has combat stats like power, speed, armor, and health. Different bot types (TankBot and SpeedBot) have unique behaviors and strategies. Players can equip bots with weapons and upgrades that modify performance. Battles are turn-based and managed through the Arena class, which determines attack order, damage, and victory. This project uses OOP principles like inheritance, encapsulation, decorators, and operator overloading to create a modular and expandable codebase.

2. Class Diagram – Overview

(For your UML diagram)

	•	BattleBot: base class
 
 	•	TankBot and SpeedBot: derived from BattleBot
 
	•	Weapon: used by bots, created separately
 
	•	Player: owns and manages bots
 
	•	Arena: runs battles between bots


3. Student Division

Student A

Implements: BattleBot, TankBot, SpeedBot, Weapon

Checklist 1 (All Required):

	•	3+ classes: BattleBot, TankBot, SpeedBot
	•	5+ methods: init, attack, equip_weapon, take_damage, str
	•	3 encapsulated attributes:
	•	Private: __name
	•	Protected: _armor
	•	Public: power
	•	Decorators: @property for HP, @staticmethod in Weapon
	•	__str__() in BattleBot
	•	Meets all separation of concerns and is fully testable

Checklist 2 (Pick at least 2):

	•	Inheritance + Overridden Methods: TankBot, SpeedBot override attack(), special_move()
	•	Operator Overloading:
	•	+: Equip weapon
	•	-: Damage calculation
	•	==: Compare bots by total power

Student B

Implements: Player, Arena, main simulation logic

Checklist 1 (All Required):

	•	3+ classes: Player, Arena, possibly a helper like BattleLog
	•	5+ methods: add_bot, start_battle, compare_players, get_scoreboard, str
	•	3 encapsulated attributes:
	•	Private: __player_name
	•	Protected: _bots
	•	Public: score
	•	Decorators: @classmethod to create a player from string, @staticmethod in Arena for utility functions
	•	__str__() in Player

Checklist 2 (Pick at least 2):

	•	Class/static methods
	•	Operator Overloading:
	•	>: Compare players by score
	•	+=: Add a bot to the player
	•	!=: Check if bots are different

4. Shared Files:
	•	main.py: Both students contribute tests and simulate a battle between their bots.
	•	project_description.pdf: Shared content
	•	UML Diagram: Both students share the diagram.

7. Files in Final Zip (OOP_Project.zip)

	•	main.py
	•	battlebot.py
	•	tankbot.py
	•	speedbot.py
	•	weapon.py
	•	player.py
	•	arena.py
	•	project_description.pdf
