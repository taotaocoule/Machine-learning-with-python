# -*- coding: utf-8 -*-  

import requests
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set_color_codes()
sns.set_style("white")

url="http://stats.nba.com/stats/locations_getmoments/?eventid=300&gameid=0041400235"
response=requests.get(url)
#print response.json().keys()
home=response.json()["home"]
visitor=response.json()["visitor"]
moments=response.json()["moments"]

headers=["team_id","player_id","x_loc","y_loc","radius","moment","game_clock","shock_clokc"]

play_moments=[]
for moment in moments:
	for player in moment[5]:
		player.extend((moments.index(moment),moment[2],moment[3]))
		play_moments.append(player)

df=pd.DataFrame(play_moments,columns=headers)


players=home["players"]
players.extend(visitor["players"])

id_dict={}
for player in players:
	id_dict[player['playerid']]=[player["firstname"]+" "+player["lastname"],player["jersey"]]

id_dict.update({-1:['ball',np.nan]})

df['palyer_name']=df.player_id.map(lambda x:id_dict[x][0])
df['palyer_jersey']=df.player_id.map(lambda x:id_dict[x][1])

print df.head(10)

