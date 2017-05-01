from tkinter import Menu


class MainMenubar(Menu):

    def __init__(self, tk_root):
        super().__init__(tk_root, name='main_menubar')
        self.tk_root = tk_root
        menu_bar = Menu(self, name='main_menubar_menus')
        tk_root.config(menu=menu_bar)
        self._create_file_menu(menu_bar)

    def _create_file_menu(self, menu_bar):
        file_menu = Menu(menu_bar, name='file_menu', tearoff=0)
        file_menu.add_command(label='Exit', command=self.file_menu_exit_command)
        menu_bar.add_cascade(label='File', menu=file_menu)

    def file_menu_exit_command(self):
        self.tk_root.quit()
        return 'Bye.'
