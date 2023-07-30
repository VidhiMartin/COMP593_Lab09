'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_into() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_names():
    """Gets a list of all Pokemon names from the PokeAPI.

    Returns:
        list: List of Pokemon names, if successful. Otherwise an empty list.
    """
    print('Getting a list of all Pokemon names...', end='')
    url = POKE_API_URL + '?limit=10000'  # The API limits the number of results to 10,000
    resp_msg = requests.get(url)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        pokemon_list = resp_msg.json().get('results', [])
        pokemon_names = [pokemon['name'] for pokemon in pokemon_list]
        print('success')
        return pokemon_names
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return []

def get_pokemon_info(pokemon):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter by:
    # - Converting to a string object,
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon = str(pokemon).strip().lower()

    # Check if Pokemon name is an empty string
    if pokemon == '':
        print('Error: No Pokemon name specified.')
        return

    # Send GET request for Pokemon info
    print(f'Getting information for {pokemon.capitalize()}...', end='')
    url = POKE_API_URL + pokemon
    resp_msg = requests.get(url)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')

    # TODO: Define function that gets a list of all Pokemon names from the PokeAPI
    print('Getting a list of all Pokemon names...', end='')
    url = POKE_API_URL + '?limit=10000'  # The API limits the number of results to 10,000
    resp_msg = requests.get(url)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        pokemon_list = resp_msg.json().get('results', [])
        pokemon_names = [pokemon['name'] for pokemon in pokemon_list]
        print('success')
        return pokemon_names
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return []
    

    # TODO: Define function that downloads and saves Pokemon artwork

def get_pokemon_artwork_url(pokemon):
    """Gets the URL for the official artwork of a specified Pokemon from the PokeAPI.

    Args:
        pokemon (str): Pokemon name (or Pokedex number)

    Returns:
        str: URL of the Pokemon's official artwork, if successful. Otherwise None.
    """
    # Cleaning the Pokemon name parameter in the same way as in get_pokemon_info()
    pokemon = str(pokemon).strip().lower()

    # Check if Pokemon name is an empty string
    if pokemon == '':
        print('Error: No Pokemon name specified.')
        return

    # Send GET request for Pokemon info
    print(f'Getting artwork URL for {pokemon.capitalize()}...', end='')
    url = POKE_API_URL + f'{pokemon}/'
    resp_msg = requests.get(url)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        pokemon_info = resp_msg.json()
        artwork_url = pokemon_info.get('sprites', {}).get('other', {}).get('official-artwork', {}).get('front_default')
        print('success')
        return artwork_url
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return None



if __name__ == '__main__':
    main()