from google.colab import files
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, Image


    

# Upload the CSV file
uploaded = files.upload()

# Load the dataset
pokemon_data = pd.read_csv(next(iter(uploaded)))


# Type advantage table
type_advantages = { 'Normal': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1, 'Ice': 1, 'Fighting': 2, 'Poison': 1, 'Ground': 1, 'Flying': 1, 'Psychic': 1, 'Bug': 1, 'Rock': 0.5, 'Ghost': 0, 'Dragon': 1, 'Dark': 1, 'Steel': 0.5, 'Fairy': 1},
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
}  # Your type advantages dictionary

# Function to calculate type advantage
def calculate_type_advantage(attack_type, defense_type):
    return type_advantages.get(attack_type, {}).get(defense_type, 1)



#SNS VERSION
from google.colab import files
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, Image

# Function to calculate synergy score
def calculate_synergy_score(pokemon1, pokemon2):
    synergy_score = 0

    # Calculate type advantage score
    type_advantage_score = calculate_type_advantage(pokemon1['Type_1'], pokemon2['Type_1'])
    synergy_score += type_advantage_score

    # Consider Type 2 if present
    if 'Type_2' in pokemon1 and 'Type_2' in pokemon2:
        type_advantage_score = calculate_type_advantage(pokemon1['Type_2'], pokemon2['Type_2'])
        synergy_score += type_advantage_score

    # Consider stats (e.g., defense)
    synergy_score += (pokemon2['Defense'] - pokemon1['Defense']) / 100

    return synergy_score



# Function to create UI and handle recommendations
def recommend_pokemon_ui():
    # Input widgets
    input1 = widgets.Text(description="Enter Pokemon 1:")
    input2 = widgets.Text(description="Enter Pokemon 2:")

    # Output widget
    output = widgets.Output()

    # Button to trigger the recommendation
    button = widgets.Button(description="Recommend")

    # Function to be called when the button is clicked
    def on_button_click(_):
        with output:
            output.clear_output()

            # Get user inputs
            user_input1 = input1.value.strip()
            user_input2 = input2.value.strip() if input2.value else None

            # Recommendations
            recommendation1, info1 = recommend_pokemon_info(user_input1)
            recommendation2, info2 = recommend_pokemon_info(user_input2) if user_input2 else (None, None)

            # Display information
            display_pokemon_info(recommendation1, info1)
            if recommendation2 is not None:
                display_pokemon_info(recommendation2, info2)

    # Set the function to be called on button click
    button.on_click(on_button_click)

    # Display the widgets
    display(widgets.VBox([input1, input2, button, output]))

# Function to recommend Pokemon and return information
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
def display_pokemon_info(recommendation, info):
    if recommendation is not None:
        print(f"Recommended Pokemon: {info['Name']}")
        display(Image(url=info['Sprite_URL'], format='png', width = 100))

        print("\nPokemon Information:")
        print(f"Type 1: {info['Type_1']}")
        print(f"Type 2: {info['Type_2']}")

        # Plotting bar chart for stats using Seaborn
        stats = info['Stats']
        stats.index = ['Hp', 'Attack', 'Defense', 'Sp. Attack', 'Sp. Defense', 'Speed']  # Update index names
        plt.figure(figsize=(8, 5))
        sns.barplot(x=stats.index, y=stats.values)
        plt.title("Pokemon Stats")
        plt.xlabel("Stat")
        plt.ylabel("Value")
        plt.xticks(rotation=45)
        plt.show()
        print("\nStats:")
        print(stats)

# Run the UI
recommend_pokemon_ui()


