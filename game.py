import time
import math
import readline

class Game:
    GREEN = "\033[92m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    LINE = ">>> "
    words = ["Hello", "world", "test", "this", "app"]
    prompt = {
        "start": LINE,
        "correct": GREEN + LINE + ENDC,
        "incorrect": RED + LINE + ENDC
    }
    last_word = str()

    @classmethod
    def start_game(cls):
        start_time = time.time()
        words_count = len(cls.words)
        prompt_type = "start"
        counter = 0
        
        while counter < words_count:
            cls.__prompt_words()
            cls.__user_input(prompt_type)
            # TODO: Add word highlighting for current word
            # TODO: Create somewhat of a webcrawler that gets sentences from the web and create a words list from it
            if cls.words[counter] == cls.last_word:
                cls.last_word = str()
                prompt_type = "correct"
                counter += 1
            else:
                prompt_type = "incorrect"

                
                                
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
    def __user_input(cls, prompt_type):
        cls.last_word = cls.input_with_prefill(cls.prompt[prompt_type], cls.last_word)
        cls.delete_prompt()
        cls.delete_prompt()
        
    @staticmethod
    def delete_prompt():
        CURSOR_UP_ONE = '\x1b[1A'
        ERASE_LINE = '\x1b[2K'
        print(f"{CURSOR_UP_ONE}{ERASE_LINE}", end="")
        
    @staticmethod
    def input_with_prefill(prompt, text):
        def hook():
            readline.insert_text(text)
            readline.redisplay()
        readline.set_pre_input_hook(hook)
        result = input(prompt)
        readline.set_pre_input_hook()
        return result
        

Game.start_game()