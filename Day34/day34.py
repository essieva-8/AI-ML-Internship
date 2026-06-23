#Task 3

#1. Create student marks dataset

import pandas as pd

data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6],
    'Marks': [30, 45, 55, 70, 80, 90]
}

df = pd.DataFrame(data)
print(df)

#2. Identify Features and Labels

X = df[['Study_Hours']]   # Feature
y = df['Marks']           # Label

print("Features:")
print(X)

print("\nLabels:")
print(y)

#3. Explain prediction logic

#The model learns that marks generally increase as study hours increase. Using this relationship, it predicts marks for new study hours.
#Example:If a student studies for 7 hours, the model may predict around 95 marks.


#Task 4

#1. Customer Grouping Example

#A shopping mall wants to group customers based on their monthly spending habits.
data = {
    'Customer': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
    'Monthly_Spending': [1000, 1200, 1500, 5000, 5500, 6000]
}

df = pd.DataFrame(data)

print(df)

#2. Pattern finding example

#A supermarket analyzes customer purchases and finds that customers who buy bread often buy butter as well.

#3. Clustering example

#An e-commerce company groups customers into: Budget shoppers, Regular shoppers, Premium shoppers without any predefined labels.


#Task 5

#1. Robot learning example

#A robot learns to walk by trying different movements. Correct movements earn rewards, while incorrect movements receive penalties.
actions = ['Correct Move', 'Wrong Move', 'Correct Move']

reward = 0

for action in actions:

    if action == 'Correct Move':
        reward += 10
        print("Reward +10")

    else:
        reward -= 10
        print("Penalty -10")

print("Final Score:", reward)

#2. AI Game Example

#An AI learns to play chess by receiving rewards for winning moves and penalties for losing moves.
game_results = ['Win', 'Lose', 'Win']

points = 0

for result in game_results:

    if result == 'Win':
        points += 20

    else:
        points -= 10

print("Game AI Score:", points)

#3. Reward/penalty explanation

#Reward: Positive feedback for a correct action.
#Penalty: Negative feedback for a wrong action.

#Example:
#Robot moves correctly → Reward +10
#Robot falls down → Penalty −10

