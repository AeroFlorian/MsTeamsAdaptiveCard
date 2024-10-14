import pyadaptivecard


if __name__ == "__main__":
    url="https://prod-65.westeurope.logic.azure.com:443/workflows/35784db583e04c63b86931caaa6f7053/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=-3a66FlJfqI2wFj7prD_7vRo2huTXXeElt0Qvk4RMTs"
    card = pyadaptivecard.AdaptiveCard(url)
    card.title("Commit Card")
    card.summary("I got a lot of tables")

    first_section = pyadaptivecard.CardSection()
    first_section.addFact("Project", f"[MsTeamsAdaptiveCards](https://github.com/AeroFlorian/MsTeamsAdaptiveCard)")
    first_section.addFact("Lines inserted", "86", "Good")
    first_section.addFact("Lines deleted", "72", "Attention")
    card.addSection(first_section)
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



    card.send()
