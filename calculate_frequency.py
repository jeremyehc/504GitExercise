def count_frequencies(sequence):
    """
    Count the frequency of each character in the sequence.

    Parameters:
    sequence (str): The input string for which to count character frequencies.

    Returns:
    dict: A dictionary with characters as keys and their frequencies as values.
    """
    frequency_dict = dict()
    
    for character in sequence:
        if character not in frequency_dict:
            frequency_dict[character] = 1
        else:
            frequency_dict[character] += 1
    
    return frequency_dict

def print_normalized_frequencies(frequency_dict):
    """
    Print the normalized frequency of each character in the frequency dictionary.

    Parameters:
    frequency_dict (dict): A dictionary with characters as keys and their frequencies as values.
    """
    print('Character Frequencies:')
    
    # Calculate the total frequency for normalization
    total_freq = float(sum(frequency_dict.values()))
    
    for character, frequency in frequency_dict.items():
        normalized_freq = frequency / total_freq
        print(f"{character}: {normalized_freq:.3f}")

# Example usage
sequence = 'ATCTGACGCGCGCCGC'
frequency_dict = count_frequencies(sequence)
print_normalized_frequencies(frequency_dict)