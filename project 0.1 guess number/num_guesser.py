import numpy as np

def number_guesser(number_min:int=1, number_max:int=100) -> int:
    """Function generates random number in some range (defaults 1..100) and try to find it.
    Each try to guess halves range for unknown number.

    Args:
        number_min (int, optional): minimum number. Defaults to 1.
        number_max (int, optional): maximum number. Defaults to 100.

    Returns:
        int: guesses count
        
    """
    random_number = np.random.randint(number_min, number_max+1)
    guess_count = 0
    
    while True:
        guess_count += 1
        range_half = (number_max-number_min)//2
        estimated_number = number_min + range_half
        
        if estimated_number > random_number:          
            number_max = estimated_number
        elif estimated_number < random_number:
            if range_half != 0:
                number_min = estimated_number 
            else:
                number_min += 1
        else:
            break
        
    return guess_count


def quality_tester(func,test_count:int=1000) -> float:
    """Quality tester for function number_guesser(). 
    Runs the function, records it result and calculates mean value 

    Args:
        func : tested function
        test_count (int, optional): number of test runs. Defaults to 1000.

    Returns:
        float: test runs mean value
        
    """
    score_list = []
    for iteration in range(test_count):
        score = func()
        score_list.append(score)
        
    mean_score = np.mean(score_list)    
    return mean_score
   

if __name__ == "__main__":   
    print('Среднее число попыток для угадывания', quality_tester(number_guesser))

