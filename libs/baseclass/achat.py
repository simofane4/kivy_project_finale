from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton

from kivymd.uix.dialog import MDDialog


class ContenttBox(BoxLayout):
    pass
class ContBox(BoxLayout):
    pass

class MainAppAchat(MDScreen):
    
    
    def on_enter(self):
        data_tables = MDDataTable(
            size_hint=(0.9, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            rows_num=10,
            column_data=[
                ("Id Command", dp(60)),
                ("ID Fournisseur", dp(40)),
                ("Date Command", dp(40)),
                ("Quntité de produit", dp(40)),


            ],
            row_data=[
                
                # -------------------------------------------------------------
                ("Yogurt", "159", "6.0", "24", "4.0", "87", "14%", "1%"),
                ("Cream", "23", "8.0", "67", "9.0", "187", "24%", "1%"),
                ("Eclair", "159", "180", "6.1", "4.4", "90", "18%", "0.1%"),
                ("Cupcake", "204", "7.0", "32", "5.0", "100", "9%", "2%"),
                ("Gingerbread", "302", "12.1", "89", "8.2", "95", "24%", "2%"),
                ("Jelly bean", "436", "7.3", "76", "6.7", "365", "0.6%", "3%"),
                ("Lollipop", "235", "6.0", "21", "0.0", "99", "6%", "1%"),
                ("KitKat", "445", "9.8", "123", "7.0", "324", "13%", "12%"),
                ("Honeycomb", "332", "1.8", "23", "1.0", "655", "43%", "2%"),
                ("Donut", "215", "2.4", "43", "2.0", "24", "1%", "0.3%"),
                
                
            ],
        )
        data_tables.ids.container.add_widget(
            Widget(size_hint_y=None, height="5dp")
        )
        data_tables.ids.container.add_widget(
            MDRaisedButton(
                text="CLOSE",
                pos_hint={"right": 1},
                on_release=lambda x: self.remove_widget(data_tables),
            )
        )
        self.add_widget(data_tables)


    app = ObjectProperty()
    custom_page = None

    def show_example_custom_dialog(self):
        if not self.custom_page:
            self.custom_page = MDDialog(
                title="Ajouter Un Achat :",
                type="custom",
                content_cls=ContenttBox(),
                buttons=[
                    MDFlatButton(
                        text="Enregistre",
                        
                    ),
                    MDFlatButton(
                        text="Annuler",
                    ),
                ],
            )
    
        self.custom_page.open()



