# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
from email.message import Message
from importlib.resources import path
import json
from msilib.schema import ComboBox
from time import sleep
from bat import BAT
from msword import MSWORD
from odt import ODT
from qr_code import QR_Code
from msexcel import MSEXCEL
from server_management import start_server, stop_server
from ods import ODS
# sys.path.append

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////

from pkg_resources import EGG_DIST
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from session_class import Session
from session_from_file import import_session_from_file
from sh import SH
from url import URL
from . functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
    

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_proc.svg",
            "btn_id" : "btn_server",
            "btn_text" : "Server Management",
            "btn_tooltip" : "Server Management",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_session.svg",
            "btn_id" : "btn_session",
            "btn_text" : "Session Management",
            "btn_tooltip" : "Session Management",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_token.svg",
            "btn_id" : "btn_token",
            "btn_text" : "Create Tokens",
            "btn_tooltip" : "Create Tokens",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_mail.svg",
            "btn_id" : "btn_message",
            "btn_text" : "Message Center",
            "btn_tooltip" : "Message Center",
            "show_top" : True,
            "is_active" : False
        },
        # # # # {
        # # # #     "btn_icon" : "icon_folder_open.svg",
        # # # #     "btn_id" : "btn_open_file",
        # # # #     "btn_text" : "Open File",
        # # # #     "btn_tooltip" : "Open file",
        # # # #     "show_top" : True,
        # # # #     "is_active" : False
        # # # # },
        {
            "btn_icon" : "icon_floppy.svg",
            "btn_id" : "btn_save",
            "btn_text" : "Save Current Session",
            "btn_tooltip" : "Save Current Session",
            "show_top" : False,
            "is_active" : False
        },
        # # # # {
        # # # #     "btn_icon" : "icon_info.svg",
        # # # #     "btn_id" : "btn_info",
        # # # #     "btn_text" : "Information",
        # # # #     "btn_tooltip" : "Open informations",
        # # # #     "show_top" : False,
        # # # #     "is_active" : False
        # # # # },
        # # # # {
        # # # #     "btn_icon" : "icon_settings.svg",
        # # # #     "btn_id" : "btn_settings",
        # # # #     "btn_text" : "Settings",
        # # # #     "btn_tooltip" : "Open settings",
        # # # #     "show_top" : False,
        # # # #     "is_active" : False
        # # # # }
    ]


     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        # {
        #     "btn_icon" : "icon_search.svg",
        #     "btn_id" : "btn_search",
        #     "btn_tooltip" : "Search",
        #     "is_active" : False
        # },
        # {
        #     "btn_icon" : "icon_settings.svg",
        #     "btn_id" : "btn_top_settings",
        #     "btn_tooltip" : "Top settings",
        #     "is_active" : False
        # }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_server)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # # # # # LEFT COLUMN
        # # # # # ///////////////////////////////////////////////////////////////

        #### SERVER PAGE
        self.line_edit_ip = PyLineEdit(
            text = "",
            place_holder_text = "IP Address",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit_ip.setMinimumHeight(30)
        self.ui.load_pages.server_layout.addWidget(self.line_edit_ip)

        self.line_edit_port = PyLineEdit(
            text = "",
            place_holder_text = "Port",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit_port.setMinimumHeight(30)
        self.ui.load_pages.server_layout.addWidget(self.line_edit_port)


        self.toggle_button_console_on_off = PyToggle(
            width = 50,
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )
        self.toggle_button_console_on_off.setMinimumHeight(30)
        self.ui.load_pages.server_buttons_layout.addWidget(self.toggle_button_console_on_off)

        self.server_button = PyPushButton(
            text="Start Server",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.server_button.setMinimumHeight(40)
        self.ui.load_pages.server_buttons_layout.addWidget(self.server_button)
        
        self.buttons = {}

        def start_server_in(position, port, ip = None):
            if position <= 13:
                console = 0
            else:
                console = 1
            
            if ip == "":
                pid = start_server(console, int(port))
            else:
                pid = start_server(console, int(port), str(ip))

            self.buttons["button{}".format(pid)] = PyPushButton(
                text="Stop Server on port " + str(port),
                radius=8,
                color=self.themes["app_color"]["text_foreground"],
                bg_color=self.themes["app_color"]["dark_one"],
                bg_color_hover=self.themes["app_color"]["dark_three"],
                bg_color_pressed=self.themes["app_color"]["red"]
            )

            self.buttons["button{}".format(pid)].setMinimumHeight(40)
            self.ui.load_pages.stop_server_layout.addWidget(self.buttons["button{}".format(pid)])
            self.buttons["button{}".format(pid)].clicked.connect(lambda: stop_server_in(pid))
            self.line_edit_ip.clear()
            self.line_edit_port.clear()


        def stop_server_in(pid):
            try:
                stop_server(pid)
            except:
                self.buttons["button{}".format(pid)].setText("Server already down!") # nie dziala
                #sleep(2)
            self.ui.load_pages.stop_server_layout.removeWidget(self.buttons["button{}".format(pid)])
            self.buttons["button{}".format(pid)].deleteLater()
            self.buttons["button{}".format(pid)] = None
            


        self.server_button.clicked.connect(lambda: start_server_in(self.toggle_button_console_on_off.position, self.line_edit_port.text(), self.line_edit_ip.text()))
        

        #### SESSION PAGE
        self.current_session = None
        self.session_names = {}

        def get_session_names():
            directory = os.path.abspath(os.getcwd()) + "/sessions"  # !!!
            self.session_names = {}
            for filename in os.listdir(directory):
                session = import_session_from_file(os.path.join(directory, filename))
                self.session_names[str(session.name)] = os.path.join(directory, filename)
                # print(self.session_names)
            

        def refresh_dropdown_session_names():
            try:
                self.ui.load_pages.session_names_dropdown_menu_layout.removeWidget(self.session_load_dropdown_menu)
                self.session_load_dropdown_menu.deleteLater()
                self.session_load_dropdown_menu = None
            except:
                print('First generation')
            self.session_load_dropdown_menu = QComboBox(self)
            self.session_load_dropdown_menu.setMinimumHeight(40)
            self.session_load_dropdown_menu.setStyleSheet("background-color: #1b1e23; border-bottom-right-radius: 8px; border-bottom-left-radius: 8px; border-top-right-radius: 8px; border-top-left-radius: 8px; padding-left: 10px; margin: 2px;")
            get_session_names()
            token_list = self.session_names.keys()
            # adding list of items to combo box
            self.session_load_dropdown_menu.addItems(token_list)
            self.ui.load_pages.session_names_dropdown_menu_layout.addWidget(self.session_load_dropdown_menu)



        self.current_session_info = QLabel("Current Session: None")
        self.current_session_info.setAlignment(Qt.AlignCenter)
        self.current_session_info.setStyleSheet('font-size: 15px;')
        self.ui.load_pages.session_info_layout.addWidget(self.current_session_info)
        
        self.current_session_info_id = QLabel("ID: None")
        self.current_session_info_id.setAlignment(Qt.AlignCenter)
        self.current_session_info_id.setStyleSheet('font-size: 15px;')
        self.ui.load_pages.session_info_layout.addWidget(self.current_session_info_id)

            # SESSION INFO FOR TOKEN PAGE

        self.current_session_info_2 = QLabel("Current Session: None")
        self.current_session_info_2.setAlignment(Qt.AlignCenter)
        self.current_session_info_2.setStyleSheet('font-size: 15px;')
        self.ui.load_pages.session_info_layout_2.addWidget(self.current_session_info_2)
        
        self.current_session_info_id_2 = QLabel("ID: None")
        self.current_session_info_id_2.setAlignment(Qt.AlignCenter)
        self.current_session_info_id_2.setStyleSheet('font-size: 15px;')
        self.ui.load_pages.session_info_layout_2.addWidget(self.current_session_info_id_2)

        def show_tokens():
            for row_number in range (self.table_widget.rowCount()):
                self.table_widget.removeRow(0)

            for token in self.current_session.generated_tokens:
                print(token.name)
                row_number = self.table_widget.rowCount()
                self.table_widget.insertRow(row_number)
                self.table_widget.setItem(row_number, 0, QTableWidgetItem(str(token.name)))
                self.table_widget.setItem(row_number, 1, QTableWidgetItem(str(token.description)))
                self.table_widget.setItem(row_number, 2, QTableWidgetItem(str(token.path)))

            # ////////////////////////////

            # MESSAGES LOAD
            
        def load_messages():
            items = (self.ui.load_pages.messages_layout.itemAt(i).widget() for i in range(self.ui.load_pages.messages_layout.count()))
            for widget in items:
                self.ui.load_pages.stop_server_layout.removeWidget(widget)
                widget.deleteLater()
                widget = None

            labels = {}
            for token in self.current_session.generated_tokens:
                logs = token.get_token_logs()
                for log in logs:
                    label = QLabel(f'''
NAME: {log['token_name']}
ID: {log['token_id']}
DESCRIPTION: {log['description']}
MESSAGE: {log['message']}
FROM: {log['ip']}
AT: {log['time']}
USER-AGENT: {log['user-agent']}
                    ''')
                    # TOKEN NAME: {log['token_name']}
                    label.setWordWrap(True)
                    label.setStyleSheet("background-color: #1b1e23; border-radius: 8; font-size: 8; padding-left: 15px; padding-right: 15px;")
                    labels[log['time_epoch']] = label
                    #label.setAlignment(Qt.AlignCenter)

            labels = sorted(labels.items(), reverse=True) # dict to tuple
            #print(labels)
            for label in labels:
                self.ui.load_pages.messages_layout.addWidget(label[1])
           
            # ////////////////////////////  


        self.line_edit_session_create = PyLineEdit(
            text = "",
            place_holder_text = "Session Name",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit_session_create.setMinimumHeight(30)
        self.ui.load_pages.create_session_layout.addWidget(self.line_edit_session_create)

        self.line_edit_session_create_ip= PyLineEdit(
            text = "",
            place_holder_text = "IP Address",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit_session_create_ip.setMinimumHeight(30)
        self.ui.load_pages.create_session_layout.addWidget(self.line_edit_session_create_ip)

        self.line_edit_session_create_port = PyLineEdit(
            text = "",
            place_holder_text = "Port",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit_session_create_port.setMinimumHeight(30)
        self.ui.load_pages.create_session_layout.addWidget(self.line_edit_session_create_port)

        self.session_create_button = PyPushButton(
            text="Create Session",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.session_create_button.setMinimumHeight(40)
        self.ui.load_pages.create_session_layout.addWidget(self.session_create_button)

        self.line_edit_session_load = PyLineEdit(
            text = "",
            place_holder_text = "Session Path",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit_session_load.setMinimumHeight(30)
        #self.ui.load_pages.load_session_layout.addWidget(self.line_edit_session_load)
        refresh_dropdown_session_names()

        self.session_load_button = PyPushButton(
            text="Load Session",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.session_load_button.setMinimumHeight(40)
        self.ui.load_pages.load_session_layout.addWidget(self.session_load_button)

        def create_session(name):
            if name == "":
                return
            self.current_session = Session(str(name), self.line_edit_session_create_ip.text(), self.line_edit_session_create_port.text())
            self.line_edit_session_create.clear()
            self.line_edit_session_create_ip.clear()
            self.line_edit_session_create_port.clear()
            name = self.current_session.name
            id = self.current_session.session_id
            self.current_session_info.setText("Current Session: " + name + ' [' + self.current_session.ip + ':' + self.current_session.port + ']')
            self.current_session_info_id.setText("ID: " + id)

            self.current_session_info_2.setText("Current Session: " + name + ' [' + self.current_session.ip + ':' + self.current_session.port + ']')
            self.current_session_info_id_2.setText("ID: " + id)

            self.save_current_session()
            show_tokens()
            refresh_dropdown_session_names()

        def load_session(path):
            try:
                # self.current_session = import_session_from_file(path)
                # print(self.token_dropdown_menu.currentText())
                self.current_session = import_session_from_file(self.session_names[self.session_load_dropdown_menu.currentText()])
                name = self.current_session.name
                id = self.current_session.session_id
                print(name)
                self.line_edit_session_load.clear()
                self.current_session_info.setText("Current Session: " + name + ' [' + self.current_session.ip + ':' + self.current_session.port + ']')
                self.current_session_info_id.setText("ID: " + id)

                self.current_session_info_2.setText("Current Session: " + name + ' [' + self.current_session.ip + ':' + self.current_session.port + ']')
                self.current_session_info_id_2.setText("ID: " + id)
                
                show_tokens()
                load_messages()
            except:
                self.line_edit_session_load.clear()
                print("Error: File not found or format not right.")

        self.session_create_button.clicked.connect(lambda: create_session(self.line_edit_session_create.text()))
        self.session_load_button.clicked.connect(lambda: load_session(self.line_edit_session_load.text()))


        ### TOKEN PAGE

        def generate_token(token_id, name, description = None, message = None):
            try:
                if token_id == 0: # URL
                    token = URL(self.current_session, name, description, message)
                    token.create_token(self.current_session.ip, self.current_session.port)
                elif token_id == 1: # QR Code
                    token = QR_Code(self.current_session, name, description, message)
                    token.create_token(self.current_session.ip, self.current_session.port)
                elif token_id == 2: # MS Word
                    token = MSWORD(self.current_session, name, description, message)
                    token.create_token(self.current_session.ip, self.current_session.port)
                elif token_id == 3: # MS Excel
                    token = MSEXCEL(self.current_session, name, description, message)
                    token.create_token(self.current_session.ip, self.current_session.port)
                elif token_id == 4: # ODT
                    token = ODT(self.current_session, name, description, message)
                    token.create_token(self.current_session.ip, self.current_session.port)
                elif token_id == 5: # ODC
                    token = ODS(self.current_session, name, description, message)
                    token.create_token(self.current_session.ip, self.current_session.port)
                elif token_id == 6: # .bat
                    token = BAT(self.current_session, name, description, message)
                    token.create_token(self.current_session.ip, self.current_session.port)
                elif token_id == 7: # .sh
                    token = SH(self.current_session, name, description, message)
                    token.create_token(self.current_session.ip, self.current_session.port)
                self.line_edit_token_name.clear()
                self.line_edit_token_description.clear()
                self.line_edit_token_message.clear()
                show_tokens()
            except:
                print("Error: No session loaded")
            
        self.token_dropdown_menu = QComboBox(self)
        self.token_dropdown_menu.setMinimumHeight(40)
        self.token_dropdown_menu.setStyleSheet("background-color: #1b1e23; border-bottom-right-radius: 8px; border-bottom-left-radius: 8px; border-top-right-radius: 8px; border-top-left-radius: 8px; padding-left: 10px; margin: 2px;")
        token_list = ["URL Token", "QR Code Token", "Microsoft Word Document", "Microsoft Excel Document", "Open Document Text", "Open Document Calc", "Batch File (.bat)", "Shell Script (.sh)"]
        # adding list of items to combo box
        

        self.token_dropdown_menu.addItems(token_list)
        self.ui.load_pages.token_choice_layout.addWidget(self.token_dropdown_menu)

        self.line_edit_token_name = PyLineEdit(
            text = "",
            place_holder_text = "Token Name",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )

        self.line_edit_token_description = PyLineEdit(
            text = "",
            place_holder_text = "Desctiption",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )

        self.line_edit_token_message = PyLineEdit(
            text = "",
            place_holder_text = "Message",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )

        self.line_edit_token_name.setMinimumHeight(30)
        self.ui.load_pages.token_create_button_layout.addWidget(self.line_edit_token_name)

        self.line_edit_token_description.setMinimumHeight(30)
        self.ui.load_pages.token_create_button_layout.addWidget(self.line_edit_token_description)

        self.line_edit_token_message.setMinimumHeight(30)
        self.ui.load_pages.token_create_button_layout.addWidget(self.line_edit_token_message)

        self.token_create_button = PyPushButton(
            text="Create Token",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.token_create_button.setMinimumHeight(40)
        self.ui.load_pages.token_create_button_layout.addWidget(self.token_create_button)


        def test():
            print(self.token_dropdown_menu.currentText())
            print(self.token_dropdown_menu.currentData())
            print(self.token_dropdown_menu.currentIndex())

        self.token_create_button.clicked.connect(lambda: generate_token(self.token_dropdown_menu.currentIndex(), self.line_edit_token_name.text(), self.line_edit_token_description.text(), self.line_edit_token_message.text()))


        # TABLE WIDGETS
        self.table_widget = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_widget.setColumnCount(3)
        self.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table_widget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("Token Name")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("Description")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("Token Path")

        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)

        self.ui.load_pages.token_table_layout.addWidget(self.table_widget)
        
        
        ### MESSAGE PAGE

        self.searchbar = PyLineEdit(
            text = "",
            place_holder_text = "Search",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.searchbar.setMinimumHeight(30)
        self.ui.load_pages.searchbar_layout.addWidget(self.searchbar)

        def search_messages():
            items = (self.ui.load_pages.messages_layout.itemAt(i).widget() for i in range(self.ui.load_pages.messages_layout.count()))
            for widget in items:
                if self.searchbar.text().lower() not in widget.text().lower():
                    widget.hide()
                else:
                    widget.show()
        
        self.searchbar.textChanged.connect(search_messages)


        self.load_messages_button = PyPushButton(
            text="Refresh Messages",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.load_messages_button.setMinimumHeight(40)
        self.ui.load_pages.load_messages_button_layout.addWidget(self.load_messages_button)

        self.load_messages_button.clicked.connect(load_messages)


    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)