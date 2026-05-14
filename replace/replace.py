def format_date(text:str) -> str:
    return text.replace(".","/")

if __name__ == "__main__":
    result = format_date("12.05.2026")
    print(result)