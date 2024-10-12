# MsTeamsAdaptiveCard


## Description
Python lib to move from ConnectorCards to AdaptiveCards in MS Teams
As O365 Connectors will be deprecated, new usage is via Workflows/Power Automate

## Documentation and Examples
Documentation and Examples are available at [GitHub](https://github.com/AeroFlorian/MsTeamsAdaptiveCard)

## Installation
This lib is available in PyPi, you can install it via pip:
```pip install PyMsTeamsAdaptiveCard```

## Usage
```python import pyadaptivecard```


## Getting your New Connector Url
To get your connector url, you must create a flow in Workflows/Power Automate.

Trigger to choose is `When a Teams webhook request is received`
If you used O365 connectors without authentication, you must set `Anyone` as `Who can trigger the flow?`

![Trigger Workflows](https://github.com/AeroFlorian/MsTeamsAdaptiveCard/blob/master/doc/trigger_workflows.png?raw=true)

Usage with this library is to create an action `Apply to each`, select `attachments` (dynamic content) as input.
Link with the action `Post card in a chat or channel`
As opposed to previous Connectors that only existed in Teams Channels, you can publish your cards in Group Chats as well.

![Post to Channel or Chat](https://github.com/AeroFlorian/MsTeamsAdaptiveCard/blob/master/doc/post_to_channel_or_chat.png?raw=true)

You must fill the following fields:
Adaptive Card: `items('Apply_to_each_2')?['content']` (replace with the name of your action)
Summary: `items('Apply_to_each_2')?['summary']` (replace with the name of your action)

After saving, Workflows/Power Automate will give you your `HTTP POST URL`:

![Http Post Url](https://github.com/AeroFlorian/MsTeamsAdaptiveCard/blob/master/doc/http_post_url.png?raw=true)

## Using AdaptiveCards
You can refer to the examples for usage of AdaptiveCard, CardSection and ActivitySection
All outputs are displayed as images
Example of a Multi Section Card:

![Multi Section Card](https://github.com/AeroFlorian/MsTeamsAdaptiveCard/blob/master/examples/multi_section_card.png?raw=true)


instead of printing the contents of the cards, just do `card.send()` and check the result of your workflow!




