chicken_menu_cnt = int(input())
fish_menu_cnt = int(input())
vegetarian_menu_cnt = int(input())

menus_price = chicken_menu_cnt * 10.35 + fish_menu_cnt * 12.40 + vegetarian_menu_cnt * 8.15
dessert_price = menus_price * 0.2

print(round(menus_price + dessert_price + 2.50, 2))
