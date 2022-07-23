import time
import math

class Game:
    words = ["Hello", "world", "test", "this", "app"]
    last_word = str()
    
    @classmethod
    def start_game(cls):
        start_time = time.time()
        words_count = len(cls.words)
        counter = 0
        
        while counter < words_count:
            cls.__prompt_words()
            cls.__user_input()
            
            if cls.words[counter] == cls.last_word:
                counter += 1
                
        total_time = time.time() - start_time
        total_time = "{:.3f}".format(total_time)
        
        words_per_minute = math.ceil(60 / float(total_time) * words_count)
        
        print(f"Total time: {total_time} seconds")
        print(f"WPM: {words_per_minute}")
                
    @classmethod
    def __prompt_words(cls):
        words_to_sentence = ' '.join(cls.words)
        print(words_to_sentence)
        
    @classmethod
    def __user_input(cls):
        cls.last_word = input(">>> ")
        cls.delete_prompt()
        cls.delete_prompt()
        
    @staticmethod
    def delete_prompt():
        CURSOR_UP_ONE = '\x1b[1A'
        ERASE_LINE = '\x1b[2K'
        print(f"{CURSOR_UP_ONE}{ERASE_LINE}", end="")
        
    
        

Game.start_game()