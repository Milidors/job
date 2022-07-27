from dadata import Dadata
import settings as s

 
class Work_with_menu:
    
    def search_successful_addres_suggest(self, dadata, address, user_name):
        try:
            lan = s.select_langue(user_name)
            return dadata.suggest(name="address", query=address, language=lan)
        except Exception:
            print("UNCORRECT TOKEN OR SECRET KEY")
    def output_all_address(self, result):
        try:
            for item in range(len(result)):
                print(f"{item+1}) {result[item].get('unrestricted_value')}")
        except Exception:
            print("Upss...\nError")
    def search_coords_lat(self, dadata, correct_addr):
        try:
            return dadata.clean(name="address", source=correct_addr).get('geo_lat')\
                if dadata.clean(name="address", source=correct_addr).get('geo_lat') !=  None\
                else "I dont know where this is place"
        except Exception:
            print("UNCORRECT TOKEN OR SECRET KEY")


    def search_coords_lon(self, dadata, correct_addr):
        try:
            return dadata.clean(name="address", source=correct_addr).get('geo_lon')\
                if dadata.clean(name="address", source=correct_addr).get('geo_lon') != None\
                else "I dont know where this is place"
        except Exception:
            print("UNCORRECT TOKEN OR SECRET KEY")

    def output_settings_menu(self):
        print("1 - Change langue\n2 - Update token and secret key\n3 - back")

    def choose_item_from_settings_menu(self, user_name):
        print(f"Token: {s.checking_on_reg_return_token(user_name)}\nSecret key: {s.checking_on_reg_return_sec_key(user_name)}")
        item = int(input())
        lan = "ru"
        if item == 1:
            print("How langue you want\nenglish - en \nRussia - ru")
            lan = input()
            s.update_lan_in_db(user_name, lan)
        elif item == 2:
            token = input("Please input your api token: ")
            secret_key = input("\nPlease input your secret key: ")
            s.update_data_in_db(token, secret_key, user_name)


class Menu(Work_with_menu):
    def __init__(self, dadata, user_name, correct_addr, flag):
        self.dadata = dadata
        self.user_name = user_name
        self.correct_addr = correct_addr
        self.flag = flag

    def output_menu(self):
        print("\n1 - Enter your address\n2 - Settings\n3 - Exit ") 

    
    def choose_item_from_menu(self):
        try:
            choose = input()
            if choose == "1":
                print("Enter address: ")
                address = input()
                coords = []
                result = super().search_successful_addres_suggest(self.dadata, address, self.user_name)
                super().output_all_address(result)
                print("\nChoose address: ")
                addres = int(input())
                self.correct_addr = result[addres-1].get("unrestricted_value")
                print(self.correct_addr)
                coords.append(super().search_coords_lat(self.dadata, self.correct_addr))
                coords.append(super().search_coords_lon(self.dadata, self.correct_addr))
                print("COORDS\nlat: ", coords[0]," lon: ", coords[1]) if coords[0] != 'I dont know where this is place' else print(coords[0])
                return self.flag
            elif choose == "2":
                super().output_settings_menu()
                super().choose_item_from_settings_menu(self.user_name)
                return self.flag
            elif choose == "3":
                self.flag = 0
                return self.flag
            else:
                print("There is no such option")
                return self.flag
        except Exception:
            return 0
   

if __name__ == "__main__":
    correct_addr = ""
    flag = 1
    name_usr = input("What is your name?\n")
    dadata= None
    if s.return_info_about_name(name_usr) == None:
        token = input("Please input your api token: ")
        secret_key = input("\nPlease input your secret key: ")
        dadata = Dadata(token, secret_key)
        s.insert_data(name_usr, token, secret_key, "ru")
    else:
        print(f"\nHello {name_usr}\n")
        token = s.checking_on_reg_return_token(name_usr)
        secret_key = s.checking_on_reg_return_sec_key(name_usr)
        dadata = Dadata(token, secret_key)
    while flag:
        menu = Menu(dadata, name_usr, correct_addr, flag)
        menu.output_menu()
        flag = menu.choose_item_from_menu()

