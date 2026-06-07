#!/bin/bash

echo "A long time ago in a galaxy far, far away..."
echo "You are a young pilot on the desert planet of Tatooine. Your rusty landspeeder has broken down."
echo "You see a settlement in the distance and a mysterious cave nearby."
echo ""
echo "What do you do?"
echo "1. Head towards the settlement, hoping to find parts."
echo "2. Investigate the mysterious cave."
echo "3. Try to repair the landspeeder with limited tools."
echo ""

read -p "Enter your choice (1, 2, or 3): " choice

if [ "$choice" == "1" ]; then
    echo ""
    echo "You head towards the settlement of Mos Eisley. The sun beats down on you as you walk."
    echo "Suddenly, a group of Tusken Raiders emerges from behind a dune, blocking your path!"
    echo ""
    echo "What do you do?"
    echo "1. Attempt to negotiate with them."
    echo "2. Try to run past them."
    echo "3. Prepare for a fight."
    echo ""
    read -p "Enter your choice (1, 2, or 3): " choice2

    if [ "$choice2" == "1" ]; then
        echo ""
        echo "You try to speak to the Tusken Raiders, but they only respond with guttural roars and raise their gaderffii sticks."
        echo "They are not interested in negotiation. You are quickly overwhelmed."
        echo "--- GAME OVER: Captured by Tusken Raiders ---"
    elif [ "$choice2" == "2" ]; then
        echo ""
        echo "You make a desperate dash past the Raiders. One of them swings a stick, but you manage to duck under it."
        echo "You reach the outskirts of Mos Eisley, out of breath but safe for now."
        echo "--- YOU SURVIVE: You reached Mos Eisley ---"
    elif [ "$choice2" == "3" ]; then
        echo ""
        echo "You ready yourself for a fight, but realize you are heavily outnumbered and outmatched."
        echo "The Tusken Raiders quickly subdue you."
        echo "--- GAME OVER: Overwhelmed by Tusken Raiders ---"
    else
        echo "Invalid choice. The Tusken Raiders don't wait for you to decide."
        echo "--- GAME OVER ---"
    fi

elif [ "$choice" == "2" ]; then
    echo ""
    echo "You decide to investigate the mysterious cave. As you cautiously enter, the air grows colder."
    echo "You hear a faint humming sound and see a faint blue glow deeper within."
    echo ""
    echo "What do you do?"
    echo "1. Proceed deeper into the cave to investigate the light."
    echo "2. Decide it's too dangerous and turn back."
    echo ""
    read -p "Enter your choice (1 or 2): " choice2

    if [ "$choice2" == "1" ]; then
        echo ""
        echo "You carefully move deeper, and the blue glow intensifies. You find an ancient, deactivated lightsaber!"
        echo "As you touch it, you feel a strange surge of power. This could change everything."
        echo "--- YOU WIN: You found a lightsaber! ---"
    elif [ "$choice2" == "2" ]; then
        echo ""
        echo "You decide the cave is too creepy and turn back. You are back where you started, but now it's getting dark."
        echo "--- GAME OVER: Lost in the darkness ---"
    else
        echo "Invalid choice. The mystery of the cave remains unsolved as darkness falls."
        echo "--- GAME OVER ---"
    fi

elif [ "$choice" == "3" ]; then
    echo ""
    echo "You try to repair the landspeeder with your limited tools. After some struggle, you manage to get the engine sputtering."
    echo "It's not perfect, but it's enough to get you to the next outpost."
    echo "--- YOU SURVIVE: Landspeeder Repaired ---"
else
    echo "Invalid choice. The sun sets, and you are stranded."
    echo "--- GAME OVER ---"
fi
