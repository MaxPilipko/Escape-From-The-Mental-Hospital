import button.buttons as buttons


def show_buttons(screen):
    buttons.dict_buttons['Play'].show(screen)
    buttons.dict_buttons['Continue'].show(screen)
    buttons.dict_buttons['Help'].show(screen)
    buttons.dict_buttons['Authors'].show(screen)
    buttons.dict_buttons['Exit'].show(screen)

def action_buttons(funcs_dict):
    buttons.dict_buttons['Play'].action(function=funcs_dict['Play'])
    buttons.dict_buttons['Continue'].action(function=funcs_dict['Continue'])
    buttons.dict_buttons['Help'].action(function=funcs_dict['Help'])
    buttons.dict_buttons['Authors'].action(function=funcs_dict['Authors'])
    buttons.dict_buttons['Exit'].action(function=funcs_dict['Exit'])
    

def update(screen, funcs_dict):
    show_buttons(screen)
    action_buttons(funcs_dict)

def play_game():
    print('play')

def continue_game():
    print('continue')

def help_game():
    print('help')

def authors_game():
    print('authors')

def exit_game():
    print('exit')

funcs_dict = {
    'Play': play_game,
    'Continue': continue_game,
    'Help': help_game,
    'Authors': authors_game,
    'Exit': exit_game
}