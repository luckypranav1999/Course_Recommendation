import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# -----------------------------
# CONFIG
# -----------------------------
NUM_USERS = 200
NUM_ITEMS = 50
NUM_INTERACTIONS = 1000

roles = ["Coach", "Medic", "Volunteer", "Referee", "Player"]
skill_levels = ["Beginner", "Level_1", "Level_2", "UEFA_A"]

categories = [
    "Coaching",
    "Safeguarding",
    "Refereeing",
    "Medical",
    "Fitness",
    "Youth Development"
]

interaction_weights = {
    "viewed": 1,
    "enrolled": 3,
    "completed": 5
}

# -----------------------------
# USERS
# -----------------------------
users = []
for i in range(NUM_USERS):
    user_id = f"FAN_{100000 + i}"
    role = random.choice(roles)
    skill = random.choice(skill_levels)
    profile_score = round(random.uniform(0.3, 0.95), 2)

    users.append([user_id, role, skill, profile_score])

users_df = pd.DataFrame(
    users,
    columns=["user_id", "role", "skill_level", "profile_score"]
)

# -----------------------------
# ITEMS (Courses + Programs)
# -----------------------------
items = []
for i in range(NUM_ITEMS):
    item_id = f"C_{2000 + i}"
    item_type = random.choice(["course", "program"])
    category = random.choice(categories)
    difficulty = random.choice(skill_levels)

    items.append([item_id, item_type, category, difficulty])

items_df = pd.DataFrame(
    items,
    columns=["item_id", "item_type", "category", "difficulty"]
)

# -----------------------------
# INTERACTIONS
# -----------------------------
interactions = []

start_date = datetime(2023, 1, 1)

for _ in range(NUM_INTERACTIONS):
    user = users_df.sample(1).iloc[0]
    item = items_df.sample(1).iloc[0]

    interaction = random.choices(
        ["viewed", "enrolled", "completed"],
        weights=[0.5, 0.3, 0.2]
    )[0]

    weight = interaction_weights[interaction]

    timestamp = start_date + timedelta(
        days=random.randint(0, 600)
    )

    interactions.append([
        user["user_id"],
        item["item_id"],
        interaction,
        weight,
        timestamp
    ])

interactions_df = pd.DataFrame(
    interactions,
    columns=["user_id", "item_id", "interaction", "weight", "timestamp"]
)

# -----------------------------
# SAVE FILES
# -----------------------------
users_df.to_csv("users.csv", index=False)
items_df.to_csv("items.csv", index=False)
interactions_df.to_csv("interactions.csv", index=False)

print("Datasets created:")
print("users.csv:", users_df.shape)
print("items.csv:", items_df.shape)
print("interactions.csv:", interactions_df.shape)
