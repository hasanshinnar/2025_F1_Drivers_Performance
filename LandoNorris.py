import fastf1
import pandas as pd
import os
cache_dir = './f1_cache'
os.makedirs(cache_dir, exist_ok=True)
fastf1.Cache.enable_cache('f1_cache')

year = 2025
driver_code = 'NOR'
all_laps = []
schedule = fastf1.get_event_schedule(year)

for index, event in schedule.iterrows():
    round_num = event['RoundNumber']
    if round_num == 0: continue  # Skip pre-season testing

    try:
        print(f"Loading Round {round_num}: {event['EventName']}...")
        session = fastf1.get_session(year, round_num, 'R')  # 'R' for Race
        session.load()

        nor_laps = session.laps.pick_drivers(driver_code)

        nor_laps['RaceName'] = event['EventName']
        nor_laps['EventDate'] = event['EventDate']
        nor_laps['Round'] = round_num
        nor_laps['FinishPosition'] = session.results.loc[
            session.results['Abbreviation'] == driver_code, 'Position'
        ].values[0]
        nor_laps['Points'] = session.results.loc[
            session.results['Abbreviation'] == driver_code, 'Points'
        ].values[0]
        time_cols = ['LapTime', 'Sector1Time', 'Sector2Time', 'Sector3Time']
        for col in time_cols:
            nor_laps[col] = nor_laps[col].dt.total_seconds()

        all_laps.append(nor_laps)

    except Exception as e:
        print(f"Could not load Round {round_num}: {e}")
nor_2025_season = pd.concat(all_laps, ignore_index=True)
consistency = nor_2025_season.groupby('Round')['LapTime'].std()
nor_2025_season.groupby(['Round', 'Compound'])['LapTime'].mean()
points_per_round = nor_2025_season.groupby('Round')['Points'].max()

nor_2025_season.to_csv('Norris_2025_development.csv', index=False)
print("Success! Data saved to Norris_2025_development.csv")