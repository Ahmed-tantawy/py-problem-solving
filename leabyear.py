leab_year=int(input("Enter the year: "))

def checkleab(leab_year):
    if leab_year == 2000 or leab_year == 2400:
        print(f"This {leab_year} it's a leab year")
    elif leab_year % 4 == 0 and leab_year % 100 != 0:
        print(f"This {leab_year} it's a leab year")
    else:
        print(f"This {leab_year} it's not a leab year")
        
checkleab(leab_year)
