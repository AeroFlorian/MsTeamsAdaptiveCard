import requests


class ActivitySection:
    def __init__(self) -> None:
        self._title = None
        self._activityTitle = None
        self._activitySubtitle = None
        self._activityImage = None

    def title(self, title):
        self._title = title

    def activityTitle(self, activityTitle):
        self._activityTitle = activityTitle

    def activitySubtitle(self, activitySubtitle):
        self._activitySubtitle = activitySubtitle

    def activityImage(self, activityImage):
        self._activityImage = activityImage

    def to_json(self):
        elements = [
            {"type": "Container",
             "separator": "true",
             "items": [
                 {"type": "TextBlock",
                  "text": self._title,
                  "weight": "bolder",
                  "size": "medium",
                  "style": "heading"},
                 {"type": "ColumnSet",
                  "columns": [{
                      "type": "Column",
                      "width": "medium",
                      "items": [
                          {
                              "type": "Image",
                              "url": self._activityImage,
                              "size": "medium"
                          }
                      ]
                  },
                      {
                          "type": "Column",
                          "width": "stretch",
                          "items": [
                              {
                                  "type": "TextBlock",
                                  "text": self._activityTitle,
                                  "weight": "bolder",
                                  "size": "medium"
                              },
                              {
                                  "type": "TextBlock",
                                  "text": self._activitySubtitle
                              }
                          ]
                      }]
                  }
             ]}
        ]
        return elements


class CardSection:
    def __init__(self):
        self._text = None
        self._facts = []
        self._button = None
        self._title = None

    def title(self, title):
        self._title = title

    def addFact(self, name, value, color="Default"):
        self._facts.append((name, value, color))

    def addLinkButton(self, name, url):
        self._button = (name, url)

    def text(self, text):
        self._text = text

    def to_json(self):
        elements = []
        if self._title:
            elements.append(
                {"type": "TextBlock",
                 "text": self._title,
                 "weight": "bolder",
                 "size": "medium",
                 "style": "heading"})

        if self._text:
            lines = self._text.split("\n")
            items_lines = [
                {"type": "TextBlock",
                 "text": line,
                 "wrap": "true"}
                for line in lines
            ]
            elements.append(
                {
                    "type": "Container",
                    "separator": "true",
                    "style": "emphasis",
                    "fontType": "Monospace",
                    "items": items_lines
                })

        if self._facts:
            items_title = [
                {"type": "TextBlock",
                 "text": fact[0],
                 "weight": "bolder",
                 "size": "medium",
                 "color": "Default"}
                for fact in self._facts]

            items_value = [
                {"type": "TextBlock",
                 "text": value,
                 "weight": "bolder",
                 "size": "medium",
                 "color": color}
                for _, value, color in self._facts]

            elements.append(
                {"type": "ColumnSet",
                 "columns": [{"type": "Column",
                              "separator": "true",
                              "width": "medium",
                              "items": items_title
                              },
                             {"type": "Column",
                              "separator": "true",
                              "width": "stretch",
                              "items": items_value
                              }]
                 })

        if self._button:
            elements.append(
                {"type": "ActionSet",
                 "actions": [{"type": "Action.OpenUrl", "title": self._button[0], "url": self._button[1]}]})

        return [{"type": "Container",
                 "separator": "true",
                 "items": elements}]


def tableCell(text):
    return {
        "type": "TableCell",
        "items": [
            {
                "type": "TextBlock",
                "text": text
            }
        ]
    }


class TableSection:
    def __init__(self, title=None, table=[], with_headings=True):
        self.with_headings = with_headings
        self.rows = table
        self._title = title

    def addRow(self, *args):
        if len(self.rows):
            if len(args) != len(self.rows[0]):
                print(f"Failed to add row, expected {len(self.rows[0])} items, got {len(args)} ")
                return
        self.rows.append(args)

    def to_json(self):
        section_elements = []
        if not len(self.rows):
            print("Error: Using to_json for a TableSection but no rows added")
            return
        if self._title:
            section_elements.append(
                {"type": "TextBlock",
                 "text": self._title,
                 "weight": "bolder",
                 "size": "medium",
                 "style": "heading"})
        rows = []
        for row in self.rows:
            table_cells = [tableCell(text) for text in row]
            rows.append({"type": "TableRow", "cells": table_cells})

        if self.with_headings:
            for elem in rows[0]["cells"]:
                elem["style"] = "emphasis"

        table = {
            "type": "Table",
            "columns": [{"width": 3} for i in range(len(self.rows[0]))],
            "rows": rows
        }
        section_elements.append(table)
        return [{"type": "Container",
                 "separator": "true",
                 "items": section_elements}]


class AdaptiveCard:
    def __init__(self, url):
        self.url = url
        self._title = None
        self._summary = "No Summary"
        self.sections = []
        self._color = "0078D7"

    def title(self, title):
        self._title = title

    def summary(self, summary):
        self._summary = summary

    def addSection(self, section):
        self.sections.append(section)

    def color(self, color):
        self._color = color

    def to_json(self):
        section_list = []
        if self._title:
            section_list.append(
                {"type": "TextBlock",
                 "text": self._title,
                 "weight": "bolder",
                 "size": "large",
                 "style": "heading"})
        for section in self.sections:
            section_list += section.to_json()
        return {
            "type": "AdaptiveCard",
            "version": "1.4",
            "themeColor": self._color,
            "msteams": {
                "width": "Full"
            },
            "body": section_list
        }

    def printme(self):
        message_body = {
            'type': 'message',
            'attachments': [
                {
                    'contentType': "application/vnd.microsoft.teams.card.adaptive",
                    'version': '1.4',
                    'summary': self._summary,
                    'content': self.to_json()
                }
            ]
        }
        print(message_body)

    def send(self):
        header = {
            "Content-Type": "application/json"
        }
        data = self.to_json()
        message_body = {
            'type': 'message',
            'attachments': [
                {
                    'contentType': "application/vnd.microsoft.teams.card.adaptive",
                    'version': '1.4',
                    'summary': self._summary,
                    'content': data
                }
            ]
        }
        response = requests.post(self.url, json=message_body, headers=header)
        if 200 <= response.status_code <= 202:
            print("Adaptive Card sent!")
        else:
            print("Error while sending adaptive card")
            print(f"Response status code: {response.status_code}")
            print(f"Response text: {response.text}")
