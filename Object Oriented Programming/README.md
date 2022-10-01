## **Infinite Runner Game in C++**

---

* ### **Prerequisites**
    * Visual Studio is the easiest approach to build this
    * SFML Library download from [here](https://www.sfml-dev.org/)
    * C++14 or higher 
    * Basic knowledge of debugging incase of problems
* ### **Introduction**
    This program was an attempt to develop a 2D infinite platform running game using C++ and the well known SFML (Simple Fast MultiMedia Library).
    
* ### **Planning**
    We have designed an infinite run and jump game where the goal of the player is to stay on one side of the screen and dodge obstacles that are coming their way by jumping over them. The main goal of the game is to survive the longest and attain the highest score possible.

* ### **Development**
  Used *Object Oriented Programming* to plan out the game. We also used the features of *Model View Control* pattern to distribute the application code:

    We divided the code into several modules (OOP approach). Each part of the game (player, obstacle, text) was separated into an object (a separate class).

    We distributed the code into
     * Model group *(which contains the Functionality and logic)*
    
     * View group *(The render engine which renders everything to the screen)* 
    
     * Control group *(Code that controls the running of the game and its logic and keeps everything in sync)* 
  
  This separation was done using the fundamental concept of MVC designs

* ### **Testing & Debugging**
  The code files are well documented and explained. For futher information you can run the debugger and pause processing at specific parts to better understand the code execution

* ### **Licensing**
  All resources used are our own by either me or my project members enlisted in several places through the code. if credits are not mentioned appropriately, please ask.