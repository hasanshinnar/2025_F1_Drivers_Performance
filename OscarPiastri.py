import fastf1
import pandas as pd
import os
cache_dir = './f1_cache'
os.makedirs(cache_dir, exist_ok=True)
fastf1.Cache.enable_cache('f1_cache')

year = 2025
driver_code = 'PIA'
all_laps = []
schedule = fastf1.get_event_schedule(year)

for index, event in schedule.iterrows():
    round_num = event['RoundNumber']
    if round_num == 0: continue  # Skip pre-season testing

    try:
        print(f"Loading Round {round_num}: {event['EventName']}...")
        session = fastf1.get_session(year, round_num, 'R')  # 'R' for Race
        session.load()

        pia_laps = session.laps.pick_drivers(driver_code)

        pia_laps['RaceName'] = event['EventName']
        pia_laps['EventDate'] = event['EventDate']
        pia_laps['Round'] = round_num
        pia_laps['FinishPosition'] = session.results.loc[
            session.results['Abbreviation'] == driver_code, 'Position'
        ].values[0]
        pia_laps['Points'] = session.results.loc[
            session.results['Abbreviation'] == driver_code, 'Points'
        ].values[0]
        time_cols = ['LapTime', 'Sector1Time', 'Sector2Time', 'Sector3Time']
        for col in time_cols:
            pia_laps[col] = pia_laps[col].dt.total_seconds()

        all_laps.append(pia_laps)

    except Exception as e:
        print(f"Could not load Round {round_num}: {e}")
pia_2025_season = pd.concat(all_laps, ignore_index=True)
consistency = pia_2025_season.groupby('Round')['LapTime'].std()
pia_2025_season.groupby(['Round', 'Compound'])['LapTime'].mean()
points_per_round = pia_2025_season.groupby('Round')['Points'].max()

pia_2025_season.to_csv('Piastri_2025_development.csv', index=False)
print("Success! Data saved to Piastri_2025_development.csv")