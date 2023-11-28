from google.colab import files
import os
import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, Image

uploaded = files.upload()

uploaded_filename = next(iter(uploaded))
pokemon_data = pd.read_csv(uploaded_filename)

type_advantages = {
    'Normal': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 2, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 0.5, 'Ghost': 0, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1},
    'Fire': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 1, 'Grass': 2, 'Ice': 2, 'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 2, 'Rock': 0.5, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 0.5, 'Fairy': 2},
    'Water': {'Normal': 1, 'Fire': 2, 'Water': 0.5, 'Electric': 1, 'Grass': 0.5, 'Ice': 1, 'Fighting': 1, 'Poison': 1, 'Ground': 2, 'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 2, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 1, 'Fairy': 1},
    'Electric': {'Normal': 1, 'Fire': 1, 'Water': 2, 'Electric': 0.5, 'Grass': 0.5, 'Ice': 1, 'Fighting': 1, 'Poison': 1, 'Ground': 0, 'Flying': 2, 'Psychic': 1, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 1, 'Fairy': 1},
    'Grass': {'Normal': 1, 'Fire': 0.5, 'Water': 2, 'Electric': 0.5, 'Grass': 0.5, 'Ice': 1, 'Fighting': 1, 'Poison': 0.5, 'Ground': 2, 'Flying': 0.5, 'Psychic': 1, 'Bug': 2, 'Rock': 1, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1},
    'Ice': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 1, 'Grass': 2, 'Ice': 0.5, 'Fighting': 1, 'Poison': 1, 'Ground': 2, 'Flying': 2, 'Psychic': 1, 'Bug': 1, 'Rock': 2, 'Ghost': 1, 'Dragon': 2, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1},
    'Fighting': {'Normal': 2, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 2, 'Fighting': 1, 'Poison': 0.5, 'Ground': 1, 'Flying': 0.5, 'Psychic': 0.5, 'Bug': 0.5, 'Rock': 2, 'Ghost': 0, 'Dragon': 1, 'Dark': 2, 'Steel': 2, 'Fairy': 0.5},
    'Poison': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 2, 'Ice': 1, 'Fighting': 1, 'Poison': 0.5, 'Ground': 0.5, 'Flying': 1, 'Psychic': 1, 'Bug': 0.5, 'Rock': 0.5, 'Ghost': 0.5, 'Dragon': 1, 'Dark': 1, 'Steel': 0, 'Fairy': 2},
    'Ground': {'Normal': 1, 'Fire': 2, 'Water': 1, 'Electric': 2, 'Grass': 0.5, 'Ice': 1, 'Fighting': 1, 'Poison': 2, 'Ground': 1, 'Flying': 0, 'Psychic': 1, 'Bug': 0.5, 'Rock': 2, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 2, 'Fairy': 1},
    'Flying': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 0.5, 'Grass': 2, 'Ice': 1, 'Fighting': 2, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 2, 'Rock': 0.5, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1},
    'Psychic': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 0.5, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 0.5, 'Bug': 2, 'Rock': 1, 'Ghost': 2, 'Dragon': 1, 'Dark': 0, 'Steel': 0.5, 'Fairy': 1},
    'Bug': {'Normal': 1, 'Fire': 0.5, 'Water': 1, 'Electric': 1, 'Grass': 2, 'Ice': 1, 'Fighting': 0.5, 'Poison': 0.5, 'Ground': 1, 'Flying': 0.5, 'Psychic': 2, 'Bug': 1, 'Rock': 1, 'Ghost': 0.5, 'Dragon': 1, 'Dark': 2, 'Steel': 0.5, 'Fairy': 0.5},
    'Rock': {'Normal': 1, 'Fire': 2, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 2, 'Fighting': 0.5, 'Poison': 1, 'Ground': 0.5, 'Flying': 2, 'Psychic': 1, 'Bug': 2, 'Rock': 1, 'Ghost': 1, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1},
    'Ghost': {'Normal': 0, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 0.5, 'Poison': 0.5, 'Ground': 1, 'Flying': 1, 'Psychic': 2, 'Bug': 1, 'Rock': 1, 'Ghost': 2, 'Dragon': 1, 'Dark': 0.5, 'Steel': 0.5, 'Fairy': 1},
    'Dragon': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Grass': 0.5, 'Ice': 2, 'Fighting': 1, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 1, 'Ghost': 1, 'Dragon': 2, 'Dark': 1, 'Steel': 0.5, 'Fairy': 0},
    'Dark': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 2, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 2, 'Bug': 1, 'Rock': 1, 'Ghost': 2, 'Dragon': 1, 'Dark': 0.5, 'Steel': 1, 'Fairy': 0.5},
    'Steel': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Grass': 1, 'Ice': 2, 'Fighting': 1, 'Poison': 0, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 2, 'Ghost': 1, 'Dragon': 0.5, 'Dark': 1, 'Steel': 0.5, 'Fairy': 2},
    'Fairy': {'Normal': 1, 'Fire': 0.5, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 2, 'Poison': 0.5, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 0.5, 'Rock': 1, 'Ghost': 1, 'Dragon': 2, 'Dark': 2, 'Steel': 0.5, 'Fairy': 1},
}


def calculate_type_advantage(attack_type, defense_type):
    if pd.isna(attack_type) or pd.isna(defense_type):
        return 1
    return type_advantages[attack_type][defense_type]

def calculate_synergy_score(pokemon1, pokemon2):
    synergy_score = 0
    type_advantage_score = calculate_type_advantage(pokemon1['Type_1'], pokemon2['Type_1'])
    synergy_score += type_advantage_score
    if 'Type_2' in pokemon1 and 'Type_2' in pokemon2:
        type_advantage_score = calculate_type_advantage(pokemon1['Type_2'], pokemon2['Type_2'])
        synergy_score += type_advantage_score
    synergy_score += (pokemon2['Defense'] - pokemon1['Defense']) / 100
    return synergy_score

def recommend_pokemon_info(user_input):
    user_pokemon = pokemon_data[pokemon_data['Name'] == user_input]

    if user_pokemon.empty:
        return f"Error: Pokemon '{user_input}' not found in the dataset.", None

    user_pokemon = user_pokemon.iloc[0]

    if pd.isna(user_pokemon['Type_1']):
        return f"Error: Pokemon '{user_input}' has missing type information.", None

    synergy_scores = pokemon_data.apply(lambda x: calculate_synergy_score(user_pokemon, x), axis=1)
    best_match_index = synergy_scores.idxmax()
    best_match = pokemon_data.loc[best_match_index]

    info = {
        "Name": best_match["Name"],
        "Type_1": best_match["Type_1"],
        "Type_2": best_match["Type_2"] if 'Type_2' in best_match else "N/A",
        "Stats": best_match[["Hp", "Attack", "Defense", "Sp_Attack", "Sp_Defense", "Speed"]],
        "Sprite_URL": best_match["Sprite URL"],
    }

    return best_match, info

# Function to display Pokemon information
# Function to display Pokemon information
def display_pokemon_info(recommendation, info):
    if recommendation is not None:
        print(f"Recommended Pokemon: {info['Name']}")
        display(Image(url=info['Sprite_URL'], format='png'))

        print("\nPokemon Information:")
        print(f"Type 1: {info['Type_1']}")
        print(f"Type 2: {info['Type_2']}")
        
        # Plotting bar chart for stats
        stats = info['Stats']
        fig, ax = plt.subplots(figsize=(8, 5))
        stats.plot(kind='bar', ax=ax)
        plt.title("Pokemon Stats")
        plt.xlabel("Stat")
        plt.ylabel("Value")
        plt.show()
        print("\nStats:")
        print(stats)
    else:
        print(recommendation)  # Print the error message


# Function to create UI and handle recommendations
def recommend_pokemon_ui():
    # Input widgets
    input1 = widgets.Text(description="Enter Pokemon 1:")
    input2 = widgets.Text(description="Enter Pokemon 2:")

    # Output widget
    output = widgets.Output()

    # Button to trigger the recommendation
    button = widgets.Button(description="Recommend")

    def on_button_click(_):
        with output:
            output.clear_output()

            user_input1 = input1.value.strip()
            user_input2 = input2.value.strip() if input2.value else None

            
            recommendation1, info1 = recommend_pokemon_info(user_input1)
            recommendation2, info2 = recommend_pokemon_info(user_input2) if user_input2 else (None, None)

            display_all_pokemon_info(user_input1, info1, user_input2, info2)

    def display_all_pokemon_info(user_input1, info1, user_input2, info2):
      display_single_pokemon_info("User Input", user_input1, info1)
      display_single_pokemon_info("Recommendation", info1['Name'], info1)

      if user_input2 and info2:
          display_single_pokemon_info("User Input", user_input2, info2)
          display_single_pokemon_info("Recommendation", info2['Name'], info2)




    def display_single_pokemon_info(title, user_input, info):
        print(f"{title}: {user_input}")
        display(Image(url=info['Sprite_URL'], format='png'))

        print("\nPokemon Information:")
        print(f"Type 1: {info['Type_1']}")
        print(f"Type 2: {info['Type_2']}")
        
        # Plotting bar chart for stats
        stats = info['Stats']
        fig, ax = plt.subplots(figsize=(8, 5))
        stats.plot(kind='bar', ax=ax)
        plt.title("Pokemon Stats")
        plt.xlabel("Stat")
        plt.ylabel("Value")
        plt.show()
        print("\nStats:")
        print(stats)
        print("\n" + "-"*50) 

    button.on_click(on_button_click)

    display(widgets.VBox([input1, input2, button, output]))

recommend_pokemon_ui()

