aliens = []
for alien_num in range(30):
	new_alien={'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
#显示前五个
for alien in aliens[0:5]:
	print(alien)
print("...")
