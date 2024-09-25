import sys,os,time
from core.headers import headers
from core.token import get_token
from core.info import get_info, get_info_energy, get_user_dao, get_username, banner
from core.task import Task
from threading import Thread
from datetime import datetime

class Game:
    def __init__(self):
        self.data_file = self.file_path(file_name="data.txt")
        
    def file_path(self, file_name: str):
        # Get the directory of the file that called this method
        caller_dir = os.path.dirname(
            os.path.abspath(sys._getframe(1).f_code.co_filename)
        )

        # Join the caller directory with the file name to form the full file path
        file_path = os.path.join(caller_dir, file_name)

        return file_path

    def clear_terminal(self):
        """Clears the terminal screen."""
        if os.name == 'nt':
            os.system('cls')  # For Windows
        else:
            os.system('clear')  # For Linux/Unix
    
    def check_and_mine(self,token,info):
        task = Task([token])
        for attempt in range(5):
            energy = get_info_energy(token=token)
            print(f"Attempt {attempt +1}: Energy:{energy}")
            if energy >= 5:
                print(f'Starting task for: {info}')
                print(f"Process Mining...")
                task.start_mining()
                return True
            time.sleep(5)
        return False
                    
    def main(self):
        while True:
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
            data = open(self.data_file, "r").read().splitlines()
            tokens = []
            
            for data_entry in data:
                token = get_token(data=data_entry)
                # print(f"Token:{token}")
                if token:
                    tokens.append(token)
                    info = get_info(token=token)
                    username = get_username(token=token)
                    print("===============================")
                    print(f"{dt_string}")
                    print(f"Info: {info}")
                    
                    if self.check_and_mine(token, info):
                        print("Mining successful.")
 
                    else:
                        print(f"Energy is too low after 5 attempts, skipping to next user.")
                        print(f"Info: {info}")
                        print("===============================")
                    
            print(f"{dt_string}")  
            print("All users have low energy, pausing for 1 hour...")
            time.sleep(3600)
            self.clear_terminal()
                        
                    

if __name__ == "__main__":
    banner()
    try:
        game = Game()
        game.main()
    except KeyboardInterrupt:
        sys.exit()