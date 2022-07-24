class Colorizer:
    @staticmethod
    def colored_text(text, color):
        colors = {
            "endc": "\033[0m",
            "green": "\033[92m",
            "red": "\033[91m",
            "cyan": "\033[96m",
            "underline": "\033[4m",
        }
        
        text = colors[color] + text + colors["endc"]
        return text

    @staticmethod
    def multi_colored_text(text, chosen_colors):
        colors = {
            "endc": "\033[0m",
            "green": "\033[92m",
            "red": "\033[91m",
            "cyan": "\033[96m",
            "underline": "\033[4m",
        }
        
        for color in chosen_colors:
            text = colors[color] + text
        text += colors["endc"]
        return text