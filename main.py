# Convert from VCF v3.0 to CSV (Postable headers)
import pandas as pd



def create_cards_list(fileName):
    file = open(fileName, "r")
    file_content = file.read()
    return file_content.split("END:VCARD")


def create_cards_df(card_list):
    db = pd.DataFrame(card_list)
    return db


def read_card(item):
    info = {}
    lines = item.split('\n')  # if not l.startswith('#')]
    tup_lin = [tuple(li.split(":")) for li in lines]
    for d in tup_lin:
        if d[0] == "N" or "ADR;type=HOME" in d[0]:
            items = d[1].split(";")

            if d[0] == "N":
                info["First Name"] = items[1]
                info["Last Name"] = items[0]

            if "ADR;type=HOME" in d[0]:
                info["Address1"] = items[2]
                info["City"] = items[3]
                info["State"] = items[4]
                info["Zip"] = items[5]
                if len(items) == 7:
                    info["Country"] = items[6]

    return info


def convert(fileName):
    print(f'Grabbing data from, {fileName}')
    card_list = create_cards_list(fileName)
    d_list = [read_card(item) for item in card_list]
    df = create_cards_df(d_list)
    df.to_csv('toPostable.csv', index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert('ChristmasCards.vcf')

