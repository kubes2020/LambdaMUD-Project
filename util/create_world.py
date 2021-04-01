from django.contrib.auth.models import User 
from adventure.models import Player, Room


Room.objects.all().delete()

r_outside = Room(title="Outside Cave Entrance", description="North of you, the cave mount beckons")

r_foyer = Room(title="Foyer", description="""Dim light filters in from the south. Dusty passages run north and east.""")

r_overlook = Room(title="Grand Overlook", description="""A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""")

r_narrow = Room(title="Narrow Passage", description="""The narrow passage bends here from west to north. The smell of gold permeates the air.""")

r_treasure = Room(title="Treasure Chamber", description="""You've found the long-lost treasure chamber! Sadly, it has already been completely emptied byearlier adventurers. The only exit is to the south.""")
# new rooms start here
r_lake = Room(title="Treasure Lake", description="""You've found a crystal clear lake surrounded by precipices.""") 
r_river = Room(title="Treasure River", description="""You've found the mighty river filled with spawning fish.""") 
r_mountain = Room(title="Mountain", description="""You've found the highest mountain in all of the land.""") 
r_plateau = Room(title="Plateau", description="""You've found a nice flat area that overlooks treasure and East of you is the 2nd highest peak in all the world.""") 
r_peak2 = Room(title="Peak2", description="""You've found the second highest peak.""") 
r_peak1 = Room(title="Peak1", description="""You've found the number 1 highest peak in the world, 29k feet.""") 
r_snow = Room(title="Snow", description="""You've found snow at 15k feet.""") 
r_slush = Room(title="Slush", description="""You've found slush at 5k feet that feeds into Treasure Lake.""") 
r_mud = Room(title="Mud", description="""You've found mud and trickles of fresh water coming from the nearby mountainside.""") 
r_rafting = Room(title="Rafting Outfitters", description="""You've found white water rafts for rent.""")

r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
# new saves start here
r_lake.save()
r_river.save()
r_mountain.save()
r_plateau.save()
r_peak2.save()
r_peak1.save()
r_snow.save()
r_slush.save()
r_mud.save()
r_rafting.save()

# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")
#new room conne start here
r_treasure.connectRooms(r_lake, "n")
r_lake.connectRooms(r_treasure, "s")

r_lake.connectRooms(r_river, "w")
r_river.connectRooms(r_lake, "e")

r_lake.connectRooms(r_mountain, "e")
r_mountain.connectRooms(r_lake, "w")

r_mountain.connectRooms(r_plateau, "s")
r_plateau.connectRooms(r_mountain, "n")

r_treasure.connectRooms(r_plateau, "e")
r_plateau.connectRooms(r_treasure, "w")

r_plateau.connectRooms(r_peak2, "e")
r_peak2.connectRooms(r_plateau, "w")

r_peak2.connectRooms(r_peak1, "n")
r_peak1.connectRooms(r_peak2, "s")

r_peak1.connectRooms(r_mountain, "w")
r_mountain.connectRooms(r_peak1, "e")

r_peak1.connectRooms(r_snow, "n")
r_snow.connectRooms(r_peak1, "s")

r_snow.connectRooms(r_slush, "w")
r_slush.connectRooms(r_snow, "e")

r_mud.connectRooms(r_slush, "e")
r_slush.connectRooms(r_mud, "w")

r_mud.connectRooms(r_lake, "s")
r_lake.connectRooms(r_mud, "n")

r_rafting.connectRooms(r_river, "s")
r_river.connectRooms(r_rafting, "n")





players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()


