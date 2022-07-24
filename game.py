import time
import math
import readline
import random
from colorizer import Colorizer
from words_generator import WordsGenerator
# TODO: Create somewhat of a webcrawler that gets sentences from the web and create a words list from it
class Game:
    sentences = random.randint(1, 4)
    words = WordsGenerator.generate(sentences).split(' ')
    last_word = str()

    @classmethod
    def start_game(cls):
        start_time = time.time()
        words_count = len(cls.words)
        correct = None
        current_word_index = 0
        
        while current_word_index < words_count:
            cls.__prompt_words(current_word_index)
            cls.__user_input(correct)
            if cls.words[current_word_index] == cls.last_word:
                cls.last_word = str()
                correct = True
                current_word_index += 1
            else:
                correct = False

                
                                
        total_time = time.time() - start_time
        total_time = "{:.3f}".format(total_time)
        
        words_per_minute = math.ceil(60 / float(total_time) * words_count)
        
        print(f"Total time: {total_time} seconds")
        print(f"WPM: {words_per_minute}")
                
    @classmethod
    def __prompt_words(cls, current_word_index):
        current_word = cls.words[current_word_index]
        cls.words[current_word_index] = Colorizer.multi_colored_text(current_word, ["cyan", "underline"])
        words_to_sentence = ' '.join(cls.words)
        cls.words[current_word_index] = current_word
        print(words_to_sentence)
        
    @classmethod
    def __user_input(cls, correct):
        if correct == None:
            cls.last_word = input(">>> ")
        else:
            cls.last_word = cls.input_with_prefill(correct, cls.last_word)
        
        # Delete the sentences
        for sentence in range(cls.sentences):
            cls.delete_prompt()
        # Delete the old prompt
        cls.delete_prompt()
        
    @staticmethod
    def delete_prompt():
        CURSOR_UP_ONE = '\x1b[1A'
        ERASE_LINE = '\x1b[2K'
        print(f"{CURSOR_UP_ONE}{ERASE_LINE}", end="")
        
    @staticmethod
    def input_with_prefill(correct, prefilled_text):
        def hook():
            readline.insert_text(prefilled_text)
            readline.redisplay()
        readline.set_pre_input_hook(hook)
        color = "green" if correct else "red"
        result = input(Colorizer.colored_text(">>> ", color))
        readline.set_pre_input_hook()
        return result
        

Game.start_game()