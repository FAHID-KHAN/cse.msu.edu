#vehicle rental billing program 



def main():
    BUDGET_DAILY = 40.00
    BUDGET_PER_MILE = 0.25

    DAILY_BASE = 60.00
    DAILY_FREE_MPD = 100
    PER_MILE_CHARGE = .25 

    WEEKLY_BASE = 190.00
    WEEKLY_TIER1_MAX = 900
    WEEKLY_TIRE2_MAX = 1500
    WEEKLY_TIRE2_FEE = 100.00
    WEEKLY_TIRE3_FEE = 200.00

    ODOMETER_MOD = 1_000_000

    #--- Helpers (nested; close over constants above) ---

    def compute_miles(odo_start: int,odo_end:int) -> float:
        """Compute miles driven given start/end odometer readings in tenth of a mile """
        if odo_end >= odo_start:
            tenths = odo_end - odo_start
        else:
            tenths = (odo_end + ODOMETER_MOD) - odo_start
        return tenths/10.00
    
    def weeks_covered(days:int) -> int:
        """Return number of weeks(or fraction thereof) as whole weeks"""
        return (days + 6) // 7
    
    def charge_budget(days:int,miles: float) -> float:
        base = BUDGET_DAILY * days
        mileage = BUDGET_PER_MILE * miles 
        return base + mileage
    
    def charge_daily(days:int,miles:float) -> float:
        base = DAILY_BASE * days
        free = DAILY_FREE_MPD * days 
        excess = max(0.0, miles - free)
        mileage = PER_MILE_CHARGE * excess
        return base + mileage
    
    def charge_weekly(days:int,miles:float) -> float:
        w = weeks_covered(days)
        if w == 0:
            return 0.0
        base = WEEKLY_BASE * W
        avg_per_week = miles/ w
        if avg_per_week <= WEEKLY_TIER1_MAX:
            mileage = 0.0
        elif avg_per_week <= WEEKLY_TIRE2_MAX:
            mileage =WEEKLY_TIRE2_FEE * w 
        else:
            over_cap_miles = miles - (WEEKLY_TIRE2_MAX * w)
            mileage = WEEKLY_TIRE3_FEE * w + PER_MILE_CHARGE * over_cap_miles
        return base + mileage

    def compute_charge(code: str,days:int,miles:float) -> float:
        u = code.upper()
        if u=='B':
            return charge_budget(days,miles)
        if u=='D':
            return charge_daily(days,miles)
        if u == 'W':
            return charge_weekly(days,miles)
        return 0.0
    
    def print_summary(code: str, days: int, odo_start: int, odo_end: int, miles: float, amount: float) -> None:
        print("Customer summary:")
        print(f"  Classification code: {code}")
        print(f"  Number of days: {days}")
        print(f"  Odometer reading at start: {odo_start}")
        print(f"  Odometer reading at end:   {odo_end}")
        print(f"  Number of miles driven: {miles:.1f}")
        print(f"  Amount billed: ${amount:.2f}")
        print()
    while True:
        code = input("Enter customer code (Q to quit): ").strip()
        if code.lower() == 'q':
            break

        days = int(input("Number of days the vehicle was rented: ").strip())
        odo_start = int(input("Odometer reading at the start: ").strip())
        odo_end = int(input("Odometer reading at the end: ").strip())

        miles = compute_miles(odo_start, odo_end)

        if code.upper() not in {'B', 'D', 'W'}:
            print("ERROR: Invalid customer classification code.")

        amount = compute_charge(code, days, miles)
        print_summary(code, days, odo_start, odo_end, miles, amount)


if __name__ == "__main__":
    main()