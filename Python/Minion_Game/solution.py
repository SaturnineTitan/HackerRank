def minion_game(string):
    # List of possible vowels
    vowels = ['A', 'E', 'I', 'O', 'U']
    # Calculate maximum score 
    max_score = (len(string) * (len(string) + 1)) // 2
    # Calculate substrings beginning with vowels
    vowel_words = [len(string) - i for i,char in enumerate(string) if char in vowels]
    # Sum substrings beginning with vowels (Kevin's score)
    kevin_score = sum(vowel_words)
    # Calculate Stuart's score 
    stuart_score = max_score - kevin_score
    # Compare Kevin and Stuart's scores 
    if kevin_score > stuart_score:
        # Kevin wins 
        print(f'Kevin {kevin_score}')
    elif kevin_score < stuart_score:
        # Stuart wins 
        print(f'Stuart {stuart_score}')
    # If Kevin and Stuart have the same score, it's a draw 
    else:
        print("Draw")
    # Return to caller 
    return
