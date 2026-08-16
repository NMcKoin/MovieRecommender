3 Ideas
1.	Movie or Game Recommender 
•	Recommend items based on user preferences.
•	If user likes “action + sci-fi”, recommend The Matrix
•	If user likes “low dialogue + fast pacing”, recommend certain games
How it works
•	Decision trees
•	Scoring rules
•	Rule weighting


2.	Meal or Recipe recommender
•	Suggest meals based on dietary rules/available ingredients
•	If vegetarian -> exclude meat dishes
•	If user wants “quick” -> only recipes under 20 minutes
•	If user wants “High protein” -> include eggs, beans, chicken
How it works
•	Rule filtering
•	Multi-criteria logic

3.	Fitness Routine Selector
•	Recommend workouts based on goals.
•	Goal = strength -> weightlifting plan
•	Goal = fat loss -> HIIT + cardio
•	Injury = knee -> avoid squats, add upper body focus
How it works
•	Decision trees
•	Rule sets
•	Scoring and weighted results
•	Rule filtering


I chose the movie/game recommender, because I find myself consistently scrolling through streaming platforms and my library of videogames looking for something to pass the time when I have downtime. Often times, by the time I choose a game/movie, my down time is just about over.

•	Detectable Catergories
•	Genre Keywords – action, adventure, horror, comedy, drama, sci-fi, fantasy thriller, RPG, FPS, strategy, sandbox
•	Tone Keywords – dark, lighthearted, serious, goofy, emotional, gritty
•	Pacing Keyworks – fast-paced, slow-burn, dialogue-heavy, story-driven
•	Content keywords – magic, space, zombies, romance, cyberpunk, medieval, superheroes
•	Gameplay preferences (games only) – multiplayer, single-player, co-op, competitive, casual, open-world
•	Restrictions – no gore, no horror, family friendly, short, long, low-violence

Example input:
User says: “I want a dark fantasy game, story-heavy, but not too slow.”
Parsed: genre=fantasy, tone =dark, pacing = story-heavy, avoid = slow pacing.


REFLECTION:

My recommender works by taking in natural language user input and matching it against a structured JSON database. Instead of relying on machine learning, the system uses explicit rules and keyword matching to determine what the user is asking for. When the user types a sentence into GUI, the program extracts keywords
such as genres, tones, pacing, and content themes. It also detects whether the user wants a game or movie based on the keywords used in the sentence. After filtering the user input, each item in the JSON is scored based on how many of the user's keywords it matches. The highest scoring item are returned as recommendations,
with the GUI displaying the top 10 results.
One challenge I encountered while prompting the AI to assist with the design and code was balancing simplicity with functionality. I needed the system to remain rule‑based for the assignment, but I also wanted it to feel natural and flexible for the user. The AI often suggested more advanced techniques, like fuzzy matching
or machine‑learning‑style keyword expansion, which I had to steer away from to stay within the project requirements. Another challenge was making sure the GUI stayed clean and intuitive while still supporting the underlying logic. The AI helped refine the interface by removing clutter, adding examples, and improving the 
flow of user interaction. Overall, prompting the AI required clear instructions and iterative refinement, but it ultimately helped me build a system that feels both simple and effective.

