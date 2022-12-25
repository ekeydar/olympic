import csv
import json

PATH = 'data2/results.json'

def get_10000():
    with open(PATH) as fh:
        all_data = json.load(fh)
    data = all_data[0]
    assert data['name'] == '10000M Men'
    return data

def get_games():
    data = get_10000()
    assert data['gender'] == 'M'
    assert data['name'] == '10000M Men'
    return data['games']

def flat_game(game):
    record = {
        'year': game['year'],
        'location': game['location']
    }
    results = game['results']
    assert len(results) == 3, game['results']
    assert {r['medal'] for r in results} == {'G', 'B', 'S'}
    by_medal = {
        result['medal']: result
        for result in results
    }
    for medal in ['G', 'S', 'B']:
        for key in ['name', 'nationality', 'result']:
            record[f'{medal}_{key}'] = by_medal[medal][key]
    return record

def prepare_lines():
    games = get_games()
    lines = [flat_game(g) for g in games]
    lines.sort(key=lambda g: g['year'])
    return lines

def to_csv():
    lines = prepare_lines()
    out = 'out/10000_medals.csv'
    with open(out, 'w') as fh:
        writer = csv.DictWriter(fh, fieldnames=list(lines[0].keys()))
        writer.writeheader()
        for line in lines:
            writer.writerow(line)
    print(f'Wrote to {out}')    

if __name__ == '__main__':
    to_csv()
