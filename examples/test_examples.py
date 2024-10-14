import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyadaptivecard
import json

def test_commit_card():
    card = pyadaptivecard.AdaptiveCard("Check How To get Webhook URL")
    card.title("Commit Card")

    first_section = pyadaptivecard.CardSection()
    first_section.addFact("Project",  f"[MsTeamsAdaptiveCards](https://github.com/AeroFlorian/MsTeamsAdaptiveCard)")
    first_section.addFact("Lines inserted", "86", "Good")
    first_section.addFact("Lines deleted", "72", "Attention")
    card.addSection(first_section)
    with open("commit_card.json", "w") as f:
        f.write(json.dumps(card.to_json(), indent=4))

def test_bug_card():
    card = pyadaptivecard.AdaptiveCard("Check How To get Webhook URL")
    card.title("Bug Card")

    bug_section = pyadaptivecard.ActivitySection()

    bug_section.title("**Detected Bug**")
    bug_section.activityTitle("Detected bug by AeroFlorian!")
    bug_section.activitySubtitle("**Severity**: High")
    bug_section.activityImage('https://w7.pngwing.com/pngs/51/498/png-transparent-insect-cartoon-drawing-bug-animals-insects-painting-thumbnail.png')

    card.addSection(bug_section)

    button_section = pyadaptivecard.CardSection()
    button_section.addLinkButton("Open Bug", "https://github.com/AeroFlorian/MsTeamsAdaptiveCard/issues")

    card.addSection(button_section)
    with open("bug_card.json", "w") as f:
        f.write(json.dumps(card.to_json(), indent=4))

def test_text_card():
    card = pyadaptivecard.AdaptiveCard("Check How To get Webhook URL")
    card.title("Text Card")

    text_section = pyadaptivecard.CardSection()
    text_section.text("This is a simple text card")
    card.addSection(text_section)
    with open("text_card.json", "w") as f:
        f.write(json.dumps(card.to_json(), indent=4))

def test_multi_section_card():
    card = pyadaptivecard.AdaptiveCard("Check How To get Webhook URL")
    card.title("Multi Section Card")

    first_section = pyadaptivecard.CardSection()
    first_section.title("**Commit Summary**")
    first_section.addFact("Project",  f"[MsTeamsAdaptiveCards](https://github.com/AeroFlorian/MsTeamsAdaptiveCard)")
    first_section.addFact("Lines inserted", "86", "Good")
    first_section.addFact("Lines deleted", "72", "Attention")
    card.addSection(first_section)
    bug_section = pyadaptivecard.ActivitySection()

    bug_section.title("**Bug Summary**")
    bug_section.activityTitle("Detected bug by AeroFlorian!")
    bug_section.activitySubtitle("**Severity**: High")
    bug_section.activityImage('https://w7.pngwing.com/pngs/51/498/png-transparent-insect-cartoon-drawing-bug-animals-insects-painting-thumbnail.png')

    card.addSection(bug_section)

    button_section = pyadaptivecard.CardSection()
    button_section.addLinkButton("Open Bug", "https://github.com/AeroFlorian/MsTeamsAdaptiveCard/issues")

    card.addSection(button_section)

    text_section = pyadaptivecard.CardSection()
    text_section.title("Text Summary")
    text_section.text("This is a simple text card")
    card.addSection(text_section)

    with open("multi_section_card.json", "w") as f:
        f.write(json.dumps(card.to_json(), indent=4))

def test_table_card():
    card = pyadaptivecard.AdaptiveCard("Check How To get Webhook URL")
    card.title("Table Card")
    card.summary("I got a lot of tables")
    table_section = pyadaptivecard.TableSection("My Table Section")

    table_section.addRow("Column 1", "Column 2", "Column 3")
    table_section.addRow("Value 1", "Value 2", "Value 3")
    table_section.addRow("Value 4", "Value 2", "Value 3")
    table_section.addRow("Value 5", "Value 7", "Value 9")
    table_section.addRow("Value 6", "Value 8", "Value 3")
    card.addSection(table_section)

    table = [
        ["Values", "for", "days"],
        ["Values", "for", "days"],
        ["Values", "for", "days"],
        ["Values", "for", "days"],
        ["Values", "for", "days"]
    ]

    table_section2 = pyadaptivecard.TableSection("My Table Without Headings", table, False)
    card.addSection(table_section2)
    with open("table_card.json", "w") as f:
        f.write(json.dumps(card.to_json(), indent=4))


if __name__ == "__main__":
    test_commit_card()
    test_bug_card()
    test_text_card()
    test_multi_section_card()
    test_table_card()
    print("Cards created successfully!")