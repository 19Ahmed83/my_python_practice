

def main():
    text = "May 8, 1975"
    new_text = text.replace(",","").replace(" ","-")
    month, day, year = new_text.split("-")
    day = int(day)
    return f"{year}-{month}-{day:02}"

if __name__ == "__main__":
    print(main())