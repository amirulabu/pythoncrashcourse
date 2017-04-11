alien_color = 'green'

if alien_color == 'green':
	print("+5 points")

if alien_color == 'yellow':
	print("no points for you")

if alien_color == 'green':
	print("+5 points")
else: 
	print("+10 points")

alien_color = 'yellow'

if alien_color == 'green':
	print("+5 points")
elif alien_color == 'yellow':
	print("+10 points")
elif alien_color == 'red':
	print("+15 points")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0['speed'] = 'medium'
print("Original x-position: " + str(alien_0['x_position']))

# move the alien to the right
# determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# this must be a fast alien
	x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

print(alien_0)
del alien_0['points']
print(alien_0)