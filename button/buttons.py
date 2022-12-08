from button.class_button import Button
from button import settings
from paths import play_button_path


dict_buttons = {
    'Play': None,
    'Continue': None,
    'Help': None,
    'Authors': None,
    'Exit': None
}

temp_y = settings.y
for button_name in dict_buttons.keys():
    dict_buttons[button_name] = Button(x=settings.x,
                                       y=temp_y,
                                       width=settings.width,
                                       height=settings.height,
                                       image_path=play_button_path
                                       )
    temp_y += settings.height + settings.spacing
    # count += 1                          


# print(dict_buttons['Play'].rect.bottom)
# print(800 - dict_buttons['Exit'].rect.y)
