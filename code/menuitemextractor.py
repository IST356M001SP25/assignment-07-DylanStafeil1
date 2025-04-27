if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from menuitem import MenuItem


def clean_price(price:str) -> float:
    price = price.replace('$', '')
    price = price.replace(',', '')
    return price

def clean_scraped_text(scraped_text: str) -> list[str]:
    lines = scraped_text.splitlines()
    result = []
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue
        if stripped_line.startswith("NEW"):
            continue
        if stripped_line in {"GS", "V", "S", "P"}:
            continue
        result.append(stripped_line)
    return result

def extract_menu_item(title: str, scraped_text: str) -> MenuItem:
    contents = clean_scraped_text(scraped_text)
    menu_item = MenuItem(category=title, name="", price=0.0, description="")
    
    if contents:
        menu_item.name = contents[0]
    if len(contents) > 1:
        menu_item.price = clean_price(contents[1])
    if len(contents) > 2:
        menu_item.description = contents[2]
    else:
        menu_item.description = "No description available."
    
    return menu_item



if __name__=='__main__':
    pass
