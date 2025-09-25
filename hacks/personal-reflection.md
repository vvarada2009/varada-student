---
title: Individual Review Progress Blog
permalink: /individual-review-progress/
---
# 🕹️ Coding Language Identification Game

## 🎮 Game Summary

We created an **interactive coding game** designed specifically for **new coders**. The goal of the game is to help players **recognize different programming languages** by looking at small code snippets and identifying which language it is. This allows beginners to **start understanding coding syntax, structure, and vocabulary** in a fun and interactive way.  

The game consists of **three levels**:  

1. **Level 1 (Easy):** Simple and common code snippets to get players comfortable.  
2. **Level 2 (Medium):** Slightly more complex examples to challenge understanding.  
3. **Level 3 (Hard):** The most advanced snippets where players need to pay attention to subtle details in syntax and structure.  

The main purpose of this game is to **help new coders gain confidence**, start noticing patterns in different programming languages, and gradually learn coding concepts while having fun.  

### ✨ Key Features

- **📊 Progress Bar:** Players can see how far they’ve progressed in the game.  
- **⚡ Three Difficulty Levels:** Gradually increases complexity to challenge players.  
- **📈 Statistics Tracker:** Shows how many questions were answered correctly and incorrectly for each language, allowing players to identify areas for improvement.  
- **💡 Explanations After Each Question:** After answering, a clear explanation appears to teach why the answer is correct and what clues to look for.  

---

## 🛠️ My Contributions

My main contribution to the project was **adding explanations to Level 3**, which is the hardest level. These explanations help players learn even when they make mistakes and provide insight into the syntax and structure of each language.  

Here’s an example of how I adjusted the code to include explanations:

# Function to show explanation after a Level 3 question
def show_explanation(language):
    explanations = {
        "Python": "🐍 Python uses indentation to define code blocks and has simple, readable syntax.",
        "Java": "☕ Java uses semicolons and curly braces to define code blocks. It is statically typed.",
        "JavaScript": "🟨 JavaScript often runs in the browser, uses functions and objects, and has flexible syntax."
    }
    print("💡 Explanation:", explanations.get(language, "No explanation available."))

# Example of usage after player answers a Level 3 question
player_answer = get_player_answer()  # hypothetical function
show_explanation(player_answer)

# 📚 Lessons

As part of the project, our group was assigned **three programming lessons** to integrate as questions into the game. These lessons not only teach coding concepts but also allow players to practice **identifying the correct language while applying their knowledge**.

## 🔁 Iterations

- **Definition:** Iterations allow a block of code to repeat multiple times, usually using loops like `for` or `while`.
- **Team Members:** Nick and Anwita are helping create this lesson.
- **Game Integration:** Players may see code snippets with loops and must identify which language it is while understanding how iterations work.

## ✅ Boolean

- **Definition:** Boolean values are either `True` or `False` and are often used in conditional statements to control the flow of a program.
- **Team Members:** Varada (me) and Aashika are creating this lesson.
- **Game Integration:** Code snippets will contain Boolean logic (`if` statements, comparisons, etc.), challenging players to recognize both the language and the concept.

## 📋 Lists

- **Definition:** Lists are ordered collections of items that can hold multiple values, which can be accessed by index. Lists can also be modified by adding, removing, or changing elements.
- **Team Members:** Ethan and Adhav are creating this lesson.
- **Game Integration:** Snippets may show lists in action, allowing players to understand syntax differences across languages while answering correctly.

**Overall Idea:** These lessons are designed to **teach programming concepts** while simultaneously testing **language identification skills**, making learning engaging and practical.

---

# 🎯 Individual Goals

Here are my **personal goals** for the next steps of this project:

1. **Create a blog-style lesson for Boolean concepts** before integrating it into the game. This will ensure I fully understand the lesson and can explain it clearly to players.
2. **Learn about Iterations and Lists lessons** that my group members are developing, as well as additional programming lessons outside our group. This will help me expand my understanding and bring new ideas to the game.
3. **Expand the game** by potentially adding more levels, incorporating new lessons, and making the game more challenging and educational. This could include new code snippets, more difficult questions, and additional explanations to help beginners learn faster.

By achieving these goals, I hope to contribute to a **comprehensive and fun learning tool** for beginner coders that combines **gameplay, education, and interactive learning**.
