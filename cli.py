'''
Created on Feb 19, 2019

@author: mgnem

DO NOT NAME MODULE CMD.PY; RUN TIME ERROR, 'AttributeError: module 'cmd' has no attribute 'Cmd'
'''

import oxo_ui, oxo_logic
import cmd
import argparse as ap


class Oxo_cmd(cmd.Cmd):
    intro = "Enter a command: new, resume, quit. Type 'help' or '?' for help"
    prompt = " (oxo)  "
    game = ""
    
    def do_new(self, arg):
        self.game = oxo_logic.newGame()
        oxo_ui.playGame(self.game)
        
      
    def do_resume(self, arg):
        self.game = oxo_logic.restoreGame()
        oxo_ui.playGame(self.game)
        
        
    def do_quit(self, arg):
        print('goodbye...')
        raise SystemExit
    
    
def main():
    game = Oxo_cmd().cmdloop()

if __name__ == '__main__':
    main()