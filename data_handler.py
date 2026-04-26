import csv
import os

class DataHandler:
    def __init__(self, filename="leaderboard.csv"):
        self.filename = filename

    def save_score(self, player_name, score):
        file_exists = os.path.isfile(self.filename)
        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Name", "Score"])
            writer.writerow([player_name, score])

    def get_top_scores(self, limit=5):
        scores = []
        if not os.path.isfile(self.filename):
            return scores

        try:
            with open(self.filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    scores.append({"Name": row["Name"], "Score": int(row["Score"])})
            scores.sort(key=lambda x: x["Score"], reverse=True)
            return scores[:limit]
        except (FileNotFoundError, KeyError, ValueError):
            return []