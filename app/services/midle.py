# noqa
import csv


def parameter_averaging(file_path):
    summ_height = 0
    summ_weight = 0
    with open(file_path, newline="") as file:
        reader = csv.DictReader(
            file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL, escapechar="\\"
        )

        for row in reader:
            index = row["Index"]
            # comment = row["Comment"]
            height = float(row["Height(Inches)"])
            # extra = row["Extra"]
            weight = float(row["Weight(Pounds)"])

            summ_height += height
            summ_weight += weight

        md_he_inc = summ_height / float(index)
        md_he_cm = round(md_he_inc * 2.54, 2)
        md_we_pound = summ_weight / float(index)
        md_we_kg = round(md_we_pound / 2.205, 2)
        return {"height": md_he_cm, "weight": md_we_kg}
