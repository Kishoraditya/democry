import networkx as nx
import plotly.graph_objects as go
from datetime import datetime

data = [
    ["0x2e750e9f2e0db61747fb89de3fba1d720f2bcc15", "2024-01-12 13:01:59", "0xde30da39c46104798bb5aa3fe8b9e0e1f348163f"],
    ["0x2e750e9f2e0db61747fb89de3fba1d720f2bcc15", "2024-01-12 13:02:11", "0x6b175474e89094c44da98b954eedeac495271d0f"],
    ["0x2e750e9f2e0db61747fb89de3fba1d720f2bcc15", "2024-01-12 13:02:23", "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"],
    ["0x2e750e9f2e0db61747fb89de3fba1d720f2bcc15", "2024-01-12 13:03:59", "0xdac17f958d2ee523a2206206994597c13d831ec7"],
    ["0x2e750e9f2e0db61747fb89de3fba1d720f2bcc15", "2024-01-12 13:04:23", "0xe8a99699dd566df02b18e80a420ddc2b0ff2ab69"],
    ["0xe8a99699dd566df02b18e80a420ddc2b0ff2ab69", "2024-01-12 13:06:11", "0x3c11f6265ddec22f4d049dde480615735f451646"],
    ["0xe8a99699dd566df02b18e80a420ddc2b0ff2ab69", "2024-01-12 13:07:11", "0x3c11f6265ddec22f4d049dde480615735f451646"],
    ["0xe8a99699dd566df02b18e80a420ddc2b0ff2ab69", "2024-01-12 13:07:59", "0x3c11f6265ddec22f4d049dde480615735f451646"],
    ["0xe8a99699dd566df02b18e80a420ddc2b0ff2ab69", "2024-01-12 13:08:59", "0x3c11f6265ddec22f4d049dde480615735f451646"],
    ["0xe8a99699dd566df02b18e80a420ddc2b0ff2ab69", "2024-01-12 13:15:11", "0x14b50b15c932ef9565ffaf5c55a638f239c0e225"],
    ["0x14b50b15c932ef9565ffaf5c55a638f239c0e225", "2024-01-12 13:17:11", "0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4"],
    ["0x14b50b15c932ef9565ffaf5c55a638f239c0e225", "2024-01-12 13:17:59", "0x366dd2b536d257fd5faa118e7503de1bf02b1fda"],
    ["0xe8a99699dd566df02b18e80a420ddc2b0ff2ab69", "2024-01-12 13:26:35", "0xd85cfb69b876a6ad88aeaae5bd8a7082389b6062"],
    ["0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4", "2024-01-12 13:26:47", "0xb6fcac9a67417005e5e57255e19301e365303a09"],
    ["0xd85cfb69b876a6ad88aeaae5bd8a7082389b6062", "2024-01-12 13:54:11", "0xe02fa844494a8567ac1971922b9d8271f69abf3b"],
    ["0xe02fa844494a8567ac1971922b9d8271f69abf3b", "2024-01-12 14:06:47", "0x45300136662dd4e58fc0df61e6290dffd992b785"],
    ["0xb6fcac9a67417005e5e57255e19301e365303a09", "2024-01-12 15:29:59", "0x084d2a5d8de539d7fe91b91cc6c9ff943ca786fe"],
    ["0xb6fcac9a67417005e5e57255e19301e365303a09", "2024-01-12 15:36:59", "0x084d2a5d8de539d7fe91b91cc6c9ff943ca786fe"],
    ["0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4", "2024-01-12 17:56:23", "0x6417aa568d4fcd55d369b24144b8419ad0817c82"],
    ["0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4", "2024-01-12 17:57:23", "0xfff5f74d0e1881e2409df922bf4f02976398f8cf"],
    ["0xfff5f74d0e1881e2409df922bf4f02976398f8cf", "2024-01-12 17:59:59", "0xc2360d8254b321cef71ce040799e1fbd69fb2415"],
    ["0xc2360d8254b321cef71ce040799e1fbd69fb2415", "2024-01-12 18:15:11", "0xf89d7b9c864f589bbf53a82105107622b35eaa40"],
    ["0x084d2a5d8de539d7fe91b91cc6c9ff943ca786fe", "2024-01-12 18:23:59", "0x0c74d8d5f4ccf5465bc092f2780c6e44b6bed771"],
    ["0x6417aa568d4fcd55d369b24144b8419ad0817c82", "2024-01-12 18:26:47", "0x42a9c606e25dfeb0ab10e0aea4c9336f687a8618"],
    ["0x42a9c606e25dfeb0ab10e0aea4c9336f687a8618", "2024-01-12 18:30:11", "0x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88"],
    ["0x6417aa568d4fcd55d369b24144b8419ad0817c82", "2024-01-12 18:40:11", "0x79f6c9b67ffa16c66b0c921816ed8afcee1eef7c"],
    ["0x084d2a5d8de539d7fe91b91cc6c9ff943ca786fe", "2024-01-12 18:42:59", "0x0c74d8d5f4ccf5465bc092f2780c6e44b6bed771"],
    ["0x0c74d8d5f4ccf5465bc092f2780c6e44b6bed771", "2024-01-13 1:02:11", "0x45300136662dd4e58fc0df61e6290dffd992b785"],
    ["0x6417aa568d4fcd55d369b24144b8419ad0817c82", "2024-01-13 6:49:59", "0x1fbe48d514b77ac89875195e20960da07204d3c7"],
    ["0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4", "2024-01-14 13:01:23", "0x89bd3d2420e592d878ff4f71b5250b7c9a710673"],
    ["0x6417aa568d4fcd55d369b24144b8419ad0817c82", "2024-01-14 13:17:35", "0x76e4ae98568b03468b9ad3f3d4238b9fb0545a62"],
    ["0x6417aa568d4fcd55d369b24144b8419ad0817c82", "2024-01-14 13:40:11", "0x76e4ae98568b03468b9ad3f3d4238b9fb0545a62"],
    ["0x76e4ae98568b03468b9ad3f3d4238b9fb0545a62", "2024-01-14 13:42:11", "0x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88"],
    ["0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4", "2024-01-14 14:05:59", "0x858738791ebd442ba032fa81ade2a1ea3d073b73"],
    ["0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4", "2024-01-14 14:07:23", "0xfff5f74d0e1881e2409df922bf4f02976398f8cf"],
    ["0x6417aa568d4fcd55d369b24144b8419ad0817c82", "2024-01-14 17:04:35", "0x53bc23489b005dda3faf3e49fa4ee678a7086752"],
    ["0x53bc23489b005dda3faf3e49fa4ee678a7086752", "2024-01-14 17:30:59", "0x28c6c06298d514db089934071355e5743bf21d60"],
    ["0x858738791ebd442ba032fa81ade2a1ea3d073b73", "2024-01-14 17:54:59", "0x0c74d8d5f4ccf5465bc092f2780c6e44b6bed771"],
    ["0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4", "2024-01-14 18:12:59", "0x7a54d89c6205c0046aa71dccd096ea109868bf14"],
    ["0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4", "2024-01-14 18:13:35", "0xd9847682322362e1e431d1025752f933a3b30c44"],
    ["0x0c74d8d5f4ccf5465bc092f2780c6e44b6bed771", "2024-01-15 1:02:11", "0x45300136662dd4e58fc0df61e6290dffd992b785"],
    ["0x89bd3d2420e592d878ff4f71b5250b7c9a710673", "2024-01-15 3:59:23", "0x92fc3a842d393e476076677adffeda6a416261a8"],
    ["0x6417aa568d4fcd55d369b24144b8419ad0817c82", "2024-01-15 4:06:47", "0xae7ab96520de3a18e5e111b5eaab095312d7fe84"],
    ["0x6417aa568d4fcd55d369b24144b8419ad0817c82", "2024-01-15 4:29:35", "0xae7ab96520de3a18e5e111b5eaab095312d7fe84"],
    ["0xd9847682322362e1e431d1025752f933a3b30c44", "2024-01-15 11:58:23", "0x0c74d8d5f4ccf5465bc092f2780c6e44b6bed771"],
    ["0x0c74d8d5f4ccf5465bc092f2780c6e44b6bed771", "2024-01-16 1:02:11", "0x45300136662dd4e58fc0df61e6290dffd992b785"],
    ["0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4", "2024-01-16 19:36:35", "0x26e632c18ace2d6380196a7770034204cefbea64"],
    ["0x26e632c18ace2d6380196a7770034204cefbea64", "2024-01-17 15:22:23", "0x757ab746dbcf046cab99ff23c8e98584eb6f8b0d"],
    ["0x6417aa568d4fcd55d369b24144b8419ad0817c82", "2024-01-17 16:48:35", "0x76b81378fba2849ecb02b0db988079fa257ae8a2"],
    ["0x76b81378fba2849ecb02b0db988079fa257ae8a2", "2024-01-17 17:09:47", "0x45300136662dd4e58fc0df61e6290dffd992b785"],
    ["0x26e632c18ace2d6380196a7770034204cefbea64", "2024-01-17 17:29:47", "0xe34e6cff4cb81669728a56c7c55d932309b29727"],
    ["0x26e632c18ace2d6380196a7770034204cefbea64", "2024-01-17 17:52:35", "0xe160f77b85baa24da2a3f7390b469e3567757a03"],
    ["0xe34e6cff4cb81669728a56c7c55d932309b29727", "2024-01-17 20:05:35", "0x45300136662dd4e58fc0df61e6290dffd992b785"],
    ["0xe160f77b85baa24da2a3f7390b469e3567757a03", "2024-01-17 20:05:47", "0x45300136662dd4e58fc0df61e6290dffd992b785"],
    ["0x757ab746dbcf046cab99ff23c8e98584eb6f8b0d", "2024-01-18 19:37:47", "0x7913b6897338767fc92628c89558feb8d6e485d5"],
    ["0x7913b6897338767fc92628c89558feb8d6e485d5", "2024-01-18 19:38:59", "0x4e5b2e1dc63f6b91cb6cd759936495434c7e972f"],
    ["0x1fbe48d514b77ac89875195e20960da07204d3c7", "2024-01-20 18:26:23", "0x76e4529ade26e042fac43b3f2c398c6f6faf8cea"],
    ["0x76e4529ade26e042fac43b3f2c398c6f6faf8cea", "2024-01-20 18:32:59", "0x1689a089aa12d6cbbd88bc2755e4c192f8702000"],
    ["0x79f6c9b67ffa16c66b0c921816ed8afcee1eef7c", "2024-01-21 15:56:47", "0xf15c5869f11b137d002ebec96d0775d642e2dab8"],
    ["0xf15c5869f11b137d002ebec96d0775d642e2dab8", "2024-01-21 16:00:11", "0x75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88"],
    ["0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4", "2024-01-21 18:49:11", "0x81cb00aa6e12c17e94869c649b622ea17bac10df"],
    ["0x7a54d89c6205c0046aa71dccd096ea109868bf14", "2024-01-22 9:44:47", "0xe34e6cff4cb81669728a56c7c55d932309b29727"],
    ["0xe34e6cff4cb81669728a56c7c55d932309b29727", "2024-01-22 11:05:35", "0x45300136662dd4e58fc0df61e6290dffd992b785"],
    ["0x5c221727ed7151bcd1b5319e10a5650c6a18e5c4", "2024-01-23 18:30:47", "0x112fd4ad955a6f56712d3754f58df0f27a33a40a"],
    ["0x112fd4ad955a6f56712d3754f58df0f27a33a40a", "2024-01-23 18:36:35", "0xbf94f0ac752c739f623c463b5210a7fb2cbb420b"],
    ["0x6417aa568d4fcd55d369b24144b8419ad0817c82", "2024-01-24 12:57:11", "0x1b6f0646a68abbde3fdc09f45978ad2e9928f1ec"],
    ["0x1b6f0646a68abbde3fdc09f45978ad2e9928f1ec", "2024-01-25 1:27:35", "0x45300136662dd4e58fc0df61e6290dffd992b785"]
]
# Extract unique addresses
unique_addresses = set()
for transaction in data:
    unique_addresses.add(transaction[0])
    unique_addresses.add(transaction[2])

# Create a directed graph using NetworkX
G = nx.DiGraph()

# Add nodes (addresses)
for address in unique_addresses:
    G.add_node(address)

# Add edges (transactions)
for transaction in data:
    G.add_edge(transaction[0], transaction[2], time=datetime.strptime(transaction[1], "%Y-%m-%d %H:%M:%S"))

# Calculate the total time from the first to the last transaction
total_time = max(G.edges(data=True), key=lambda x: x[2]['time'])[-1]['time'] - min(G.edges(data=True), key=lambda x: x[2]['time'])[-1]['time']

# Create the plot
fig = go.Figure()

# Add vertical pillars for each address
for i, address in enumerate(unique_addresses):
    fig.add_trace(go.Bar(
        x=[address],
        y=[total_time.total_seconds() / 3600],  # Convert total time to hours
        orientation='v',
        name=f'{address}_pillar'
    ))

# Add arrows for transactions
for transaction in G.edges(data=True):
    start_address, end_address, time = transaction
    time_diff = time['time'] - min(G.edges(data=True), key=lambda x: x[2]['time'])[-1]['time']
    fig.add_trace(go.Scatter(
        x=[start_address, end_address],
        y=[time_diff.total_seconds() / 3600, time_diff.total_seconds() / 3600],
        mode='lines+text',
        line=dict(width=2, color='blue'),
        text=[],
        name=f'{start_address}_to_{end_address}_arrow'
    ))

    # Add arrowhead at the end of the line
    fig.add_trace(go.Scatter(
        x=[end_address],
        y=[time_diff.total_seconds() / 3600],
        mode='markers',
        marker=dict(color='blue', symbol='arrow-up'),
        text=[],
        name=f'{end_address}_arrowhead'
    ))

# Update layout
fig.update_layout(
    barmode='stack',
    xaxis=dict(title='Addresses'),
    yaxis=dict(title='Timeline (hours)'),
    showlegend=False
)

# Show the plot
fig.show()

